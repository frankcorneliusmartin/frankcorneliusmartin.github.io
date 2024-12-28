A new approach for the BlueBerry registry using vantage7
========================================================

:title: A new approach for the BlueBerry registry using vantage6
:date: 2024-12-20 9:00
:tags: python, vantage6, OHDSI, streamlit
:category: vantage6
:slug: sarcoma-registry-update
:authors: Frank Martin
:summary: A new approach for the BlueBerry registry using vantage6
:cover: /images/lego-alpaca/my-alpaca.png


.. sectnum::

.. contents::

The `BlueBerry project <https://euracan.eu/registries/blueberry/>`_ was a two-year
initiative to develop a blueprint for a sustainable, scalable, and impactful data
infrastructure for rare cancers in Europe. In the context of
`IKNL <https://iknl.nl/en/news/blueberry-is-now-really-taking-off!-building-a-blu>`_, I
have been involved in extending the `vantage6 <https://vantage6.ai>`_ software to be
able to connect to `OMOP data sources <https://www.ohdsi.org/data-standardization/>`_.

When the project finished in September 2024, it was decided to continue with the
registry to use it for research. However, several challenges needed to be addressed
before it could be used for research:

* The user interface that has been developed for vantage6 lacked the components that
  made working with the OMOP data source easy. It still required an engineer to operate
  the system.
* The computation of the output was rather slow as the original data source was visited
  for each computation call. This included creating the cohort and querying the selected
  features.
* Only `Crosstabulation <https://github.com/IKNL/v6-crosstab-on-ohdsi-py>`_ and
  `Kaplan-Meier curve <https://github.com/IKNL/v6-kaplan-meier-on-ohdsi-py>`_ have been
  extended to work in the registry. There were some experiments with the OHDSI tools,
  but these were difficult to operate.

I was asked to work together with `BIOMERIS <https://www.biomeris.it/en/>`_ on
addressing these issues to enable researchers using the platform for gaining meaningful
insights.

In this blog post, I will explain first how I address performance issue as this
influences how the user interface is designed. Then, I will explain how the user
interface is designed to support the workflow of the researcher.

Local Data Storage
------------------

Typically in vanilla vantage6, the data is fetched from the data source for each
computation call. This made computations slow as the OMOP query was typically time
consuming. To speed up the computations, I decided to fetch the data once for each
cohort and store it local in the vantage6 node.

.. container:: uml

    .. code::

        ┌──────────┐   ┌────────────┐   ┌────────────┐
        │ OMOP     │   │ Query      │   │ Local DB   │
        │ Database ├──►│ Algorithm  ├──►│ Parquet    │
        └──────────┘   └────────────┘   └────────────┘


The ``Query Algorithm`` is a vantage6 algorithm that is responsible for fetching the
data from the OMOP database. It creates the ATLAS cohort and reads the patient features.
The data is stored by this algorithm in a `Parquet <https://parquet.apache.org/>`_ file.
This Parquet file is then used by the other algorithms to perform the analytics.

.. container:: uml

    .. code::

        ┌────────────┐   ┌────────────┐   ┌───────────┐
        │ Local DB   │   │ vantage6   │   │ Algorithm │
        │ Parquet    ├──►│ Algorithm  ├──►│ Output    │
        └────────────┘   └────────────┘   └───────────┘

.. note::

    In the future, I would like to extend the system so that these Parquet files can also be
    modified by the user. For example, the user can create new variables.

There are some challenges with this approach:

* When a node is offline when a new cohort is created it will not be able to fetch the
  data. In this case, the node will create the cohort data it comes online. The user
  can work with the other nodes in the meantime.
* When the data source is updated, the Parquet files need to be updated as well. This
  is currently a manual process as the user needs to trigger the Query Algorithm to
  fetch the data again.
* The Parquet files need to have the same variables and the same value types for these
  variables. This should be guaranteed by the ``Query Algorithm``. Especially when the
  cohorts are not created at the same time (e.g. when a node was offline when it was
  created).

When a node is offline when a new cohort is created it will not be able to fetch the
data. In this case, the node will create the cohort data it comes online. The user can
work with the other nodes in the meantime.

.. note::

    An additional benefit of this approach is that algorithms do no longer have the
    logic to fetch the data from the OMOP database. So the vantage6 community algorithms
    can be used without (much) modification.

Researcher User Interface
-------------------------
The official vantage6 User Interface (UI) is developed as a general-purpose vantage6 UI.

.. figure:: {static}/images/sarcoma/screenshots-v6-ui.png
   :alt: vantage6 user interface
   :align: center
   :width: 800px

   The official vantage6 user interface from vantage6 (from https://vantage6.ai).

If a new feature is to be added in this interface, it needs to be compatible with other
projects from the community as well. This has two major disadvantages:

* It feels overcomplicated for the user as it contains features that are not relevant
  for the BlueBerry registry and it is not tailored to the workflow of the researcher.
* Adding new features to the UI is time-consuming as it needs to be compatible with
  other projects and requires approval from the vantage6 community.

For these two reasons, I decided it would be better to create a separate, dedicated UI
for the BlueBerry registry. This way, I can tailor the workflow exactly as it should be
and I don't have to consider other projects when adding new features.

.. important::

    As the proposed dedicated UI is aimed to support the workflow of the researcher, it
    is not going to contain all the features that the official vantage6 UI has. The
    official vantage6 UI is still available for the BlueBerry registry. It is possible
    to switch between the two UIs.

    For example, the official vantage6 UI is still used for the management of the
    collaborations and studies.


To improve the development speed, I used `Streamlit <https://streamlit.io/>`_. This
framework brought the following advantages:

* I (mostly) do not have to worry about front-end code as the front-end code is
  generated from Python code.
* It comes with a lot of built-in data science components like tables, graphs, controls,
  etc.

It does, however, create an additional backend component, the one that renders the
front end. And of course, the way the app looks needs to be something that you like,
although there are possibilities to customize it a little.

This newly developed UI should support the workflow of the researcher in a better way.
The first thing after logging in is to select the collaboration and optionally the
study it wants to work with. Once the collaboration/study is selected, the user can view
the online organizations within the collaboration or study. The user is at this point
able to create sub selections of the organizations it wants to work with.

.. container:: scrollx

   .. list-table::
      :widths: 50 50
      :header-rows: 1
      :align: center

      * - Collaboration & Study selection
        - Node status
      * - .. figure:: {static}/images/sarcoma/collaboration_and_study.jpeg
            :alt: users can select their collaboration and study
            :align: center
            :width: 400px

            Users first need to select the collaboration and optionally the study they
            want to work with. Some metadata is shown about the selected collaboration
            and study.

        - .. figure:: {static}/images/sarcoma/node_status_redacted.jpeg
            :alt: users can check the status of the nodes
            :align: center
            :width: 400px

            Once the collaboration is selected, the user can view the online
            organizations. It is possible to create a sub selection of the organizations
            the user wants to work with.


Once the organizations are selected, the system checks which cohorts are available for
the selected organizations. The UI then determines automatically which cohorts are ready
for analysis, it validates that:

1. All the (online) organizations have the cohort available.
2. The minimal number of patients threshold is met at each organization.
3. All the organizations have the same variables and have the same value types for these
   variables.

By default, all the *healthy* cohorts are selected. The user can also make a sub
selection of the cohorts it wants to work with. It is also possible to create a new
cohort based on the `ATLAS <https://atlas-demo.ohdsi.org/>`_ cohort definitions.

.. container:: scrollx

   .. list-table::
      :widths: 50 50
      :header-rows: 1
      :align: center

      * - Cohort selection
        - Cohort creation
      * - .. figure:: {static}/images/sarcoma/healthy_cohorts.jpeg
            :alt: users can select the cohorts they want to work with
            :align: center
            :width: 400px

            Users can select the cohorts they want to work with. By default, all the
            healthy cohorts are selected. In this case none of the cohorts are healthy.

        - .. figure:: {static}/images/sarcoma/healthy_cohorts_2.jpeg
            :alt: users can create a new cohort
            :align: center
            :width: 400px

            Before the user can continue all the selected organizations need to have the
            cohort available. The user is able to select the cohorts and from there
            automatically select the organizations that passed the validation.

Once the cohorts have been selected the user can continue to the analytics part of the
application. The first analytics that is available is the summary statistics. This gives
an overview of all selected cohorts and its variables. It reports some basic statistics
like missing, mean, standard deviation, etc.

The second analytics that is available is the crosstabulation. This is a useful tool
to compare the distribution of two categorical variables. The user can select the
variables it wants to compare and the crosstabulation is calculated for all selected
cohorts.

The third analytics that is available is the Kaplan-Meier curve. This is can be used
to compare the survival between cohorts. The dataset contains the survival time and
the event indicator, so these are already preselected.

.. container:: scrollx

   .. list-table::
      :widths: 33 33 33
      :header-rows: 1
      :align: center

      * - Summary statistics
        - Crosstabulation
        - Kaplan-Meier curve
      * - .. figure:: {static}/images/sarcoma/summary_stats.jpeg
            :alt: users can view the summary statistics of all selected cohorts
            :align: center
            :width: 266px

            Users can view the summary statistics of all selected cohorts. The summary
            statistics are calculated for all selected cohorts.

        - .. figure:: {static}/images/sarcoma/crosstabs.jpeg
            :alt: users can compare the distribution of two variables
            :align: center
            :width: 266px

            Users can compare the distribution of two variables. The crosstabulation is
            calculated for all selected cohorts.

        - .. figure:: {static}/images/sarcoma/kaplan_meier.jpeg
            :alt: users can compare the survival of two cohorts
            :align: center
            :width: 266px

            Users can compare the survival of two cohorts. The Kaplan-Meier curve is
            calculated for all selected cohorts.

Future work
-----------
This project is still in development throughout 2025. There are still several features
that need to be added to the system. The following features are planned:

1. The current algorithms need to be extended to support additional features like
   stratification.
2. Currently in development are some more advanced analytics like the Cox proportional
   hazard model and the propensity score matching.

.. note::

    In the future the `Local Data Storage`_ will be no longer be necessary as this
    feature will be build into the vantage6 core (This feature is called sessions and
    is available from `version 5+ <https://github.com/vantage6/vantage6/issues/943>`_).

    This might be added to the final stages of the project.


