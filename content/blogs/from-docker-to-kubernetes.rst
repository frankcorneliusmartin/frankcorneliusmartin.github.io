From Docker to Kubernetes
==========================

:title: From Docker to Kubernetes
:date: 2025-02-13 9:00
:tags: kubernetes, docker, tech, vantage6
:category: tech
:slug: from-docker-to-kubernetes
:authors: Frank Martin
:summary: Why we are moving from Docker to Kubernetes in version 5
:cover: /images/docker-to-kubernetes.png


The vantage6 infrastructure has a tight coupling with Docker since the beginning of vantage6 in 2017. The node component relies on the Docker API to start the containers that do the computation on the privacy sensitive data. At the time, Docker was a solid choice as it had development tooling and was free to use even for big commercial projects. Since then a few things have changed:

* Docker changed it license policy: in some cases, a license is now required to use Docker.
* Alternative container technologies caught up with Docker in terms of functionality and tooling, for example, Podman and Singularity.

Back in 2017 we also considered using the Kubernetes API instead of the Docker API for starting the computation containers. In this case, we still would have used the Docker engine for running the containers, but Kubernetes would be the interface for managing them (starting, stopping, etc.). This would have been a valid choice, however it was not implemented at the time as there were more pressing things on the roadmap.

Since 2017, vantage6 itself has also changed considerably. Where once every major component (client, node, server) consisted of one component it now consists of several. In the future, more components will be added in a similar way. Working with a microservice architecture has many advantages (if you are interested, they are listed here).

Challenges
----------
While developing vantage6 further, we were starting to hit the limitations of Docker. We then created our own tooling, packages and features for use cases that were already supported in Kubernetes. Let us highlight a few important points.

Security
~~~~~~~~
In the vantage6 node, we mount the Docker socket so that we can create containers that perform the computation from the vantage6 node application. The Docker daemon process on the host runs as root. This effectively means that the vantage6 node has root access to the host machine. This security issue should be considered by data parties when setting up a vantage6 node.

The necessity for root access could be dropped by using Docker's rootless mode, but that requires more complex configuration steps during node installation, and the vantage6 node will still have unlimited permissions to create containers.

.. note::

    When moving to Kubernetes we no longer need the Docker socket, so the security model is much more transparent and can be controlled by configuring the Kubernetes API access.

Node-to-node communication
~~~~~~~~~~~~~~~~~~~~~~~~~~
There is a large community out there creating privacy enhancing (or maybe even preserving) algorithms. For example Flower, ScaleMamba, MPyC, Substra, and the list goes on. All these libraries are great and would it not be awesome if we could use them in vantage6 without modifying the libraries? In this scenario, vantage6 is the mechanism to use these libraries over distributed centers in a secure way.

However, all these libraries require addresses (IP + port) to communicate with the other parties. This is something that lacked in vantage6. In version 3, we have implemented a port and ip protocol using EduVPN. This worked perfectly (thanks Djura, Lourens and Bart), but we later realized that this mechanism, which essentially installs a VPN client in the node, could be considered a backdoor by system administrators.

To establish node-to-node communication, we therefore need a more transparent and manageable implementation.

.. note::

    Instead of implementing a complicated node-to-node VPN network protocol we can rely on service mesh solutions like Istio to handle secure mutual TLS traffic between algorithm containers in different centers. This would be transparent and much more reliable than building our own solution.

Specialized computation jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Many different algorithms are used within vantage6, from traditional statistical models to machine learning and image processing. These require different computation resources. Vantage6 in its current form requires the computation to take place on the same machine as where the vantage6 node is running. This requires you to install the vantage6 node directly into the machine that has sufficient resources (GPU, CPU, RAM).

.. note::

    Using Kubernetes and its capability to span multiple workers (HPC) we can start Kubernetes jobs (vantage6 algorithm computations) in different machines with different hardware configurations.

External data sources
~~~~~~~~~~~~~~~~~~~~~
In early versions of vantage6, we could only connect to file-based databases which were copied into the node. In the past couple of releases of vantage6, we have worked on ways to connect the vantage6 node instance to external data sources. For this purpose we have released the SSH tunnel, whitelisting and docker-services features.

.. note::

    Even though these features work and provide the access, Kubernetes provides similar, though more advanced, functionality that is supported by a much larger community. Using such battle-tested and transparent technology should be accepted with more confidence by system administrators than an implementation built by a small team such as ours. Also, maintaining code around the Kubernetes communication protocols is less work managing these features ourselves in the vantage6 code base - giving us more time to work on other features.

Alternative container technologies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Docker containers are not always the most appropriate technology to run containers, especially when considering security and privacy. Describing the differences is outside of the scope of this blog post, but there are valid reasons to choose one from:

* WebAssembly
* Apptainer (formely known as Singularity)
* Podman
* Docker

.. note::

    Instead of implementing each container technology API separately we can use the Kubernetes API to start a container regardless of the underlying engine.

Container Health
~~~~~~~~~~~~~~~~
We all hate dying nodes, it requires to visit the data station and diagnose what went wrong. Often, we just perform a restart and move on.

.. note::

    Kubernetes would allow us to check the health of a container (by our own defined health checks) and restart by policy if needed.

Resource Management
~~~~~~~~~~~~~~~~~~~
The vantage6 node will spin up unlimited containers until it starts breaking down, resulting in connection loss and a dead node.

.. note::

    Kubernetes monitors resources and has mechanisms to deploy only when there is sufficient resources available. So this deadlock will be automatically prevented.

Simplified Deployment
~~~~~~~~~~~~~~~~~~~~~
Deploying a server in vantage6 can be quite cumbersome, there are many components that need to be installed and configured separately.

On the node, system administrators want to have a better insight in how containers interact with one another using a standardized tool.

.. note::

    Using helm charts to deploy the server in Kubernetes should drastically simplify the server deployment process.

    Kubernetes provides many tools for administrators for monitoring and managing the application. They therefore no longer require in-depth vantage6 knowledge to analyze container interaction.

Development environment
~~~~~~~~~~~~~~~~~~~~~~~
Since we are dealing with many services, testing and developing changes became ever more difficult. We solved most of these issues by creating our own tooling to do so, but this requires effort to maintain and is not easily transferable to other developers.

.. note::

    By using `devspace <https://devspace.sh/>`_ we can remove all our previous tooling for development and use a standardized way to share test and development environments.

Kubernetes
----------
Now that we have established that Kubernetes is a must to continue the development of vantage6, we will explain why we will not support both options of using the Docker API and Kubernetes API.

Why not keep Docker (API)
~~~~~~~~~~~~~~~~~~~~~~~~~
Kubernetes is not an alternative for Docker. We still need an engine to run containers, and we see that in many cases this still will be Docker. The functionality provided by the Kubernetes API is different and much more extensive than the one of docker. Think about networking boxed in services, replication of containers, self-healing when a container is unhealthy, etc.

In theory, we could implement these Kubernetes features ourselves, in fact, we did! For example, we have build a retry-mechanism to restart algorithm containers that have crashed. But we should not forget that we are a small development team with big ambitions. Why would we replicate something that is already out there, for free, created and maintained by 3760 contributors, used by the biggest companies in the world?

The effort to support a Docker-based node would be large. We would essentially be creating a second vantage6 node without the features described above, as well as a duplicate CLI to manage both Kubernetes and Docker configuration. Having two versions means that:

* The entire vantage6 network needs to consider that there may be two different types of nodes
* We maintain twice as much as code for the node and the CLI
* Node features need to be implemented twice
* Bug fixes may need to be applied in two places
* Algorithm developers have to ensure their algorithm works on both a Docker node and a Kubernetes node

These disadvantages make that maintaining both Docker and Kubernetes is not a viable option.

Kubernetes installation @ Data Stations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Kubernetes can be installed in many ways. At one end you have the fully managed multi cluster Kubernetes that hosts many enterprise applications and on the other end you can already run a single cluster instance directly from Docker Desktop.

When vantage6 is running using Kubernetes, it will be easy to support all of these scenarios. We consider a vantage6 node an edge device, so we don't need a big Kubernetes cluster. In its minimal form you install `microk8s` + `docker` in a VM, making the installation very similar to its current form.
