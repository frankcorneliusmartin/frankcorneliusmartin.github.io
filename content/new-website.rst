A new home
==========

:date: 2022-09-04 20:34
:tags: www
:category: tech
:slug: new-homepage
:authors: Frank Martin
:summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam quis ornare diam, quis ultrices purus. Donec vel ligula luctus, condimentum magna in, scelerisque augue.

.. figure:: {filename}/images/website-is-done-meme.jpg
   :alt: website is never done meme
   :align: center
   :width: 100%


.. We want to tell how we setup the project and what we want to do.

.. .. code-block:: python

   from pelican import create_my_website

   create_my_website(auto_content=True)

.. Wow, that was easy.. Ok that was a lie. But let's document here how this
   site evolved using `Pelican <http://pelicam.com>`_.

.. Initial page
.. ------------
.. I downloaded Pelican and their theme suite, wrote a single article,
.. created a personal github pages project, connected my DNS.. and pushed
.. the project using :code:`make github`

.. .. figure:: {filename}/images/initial-page.png
..    :alt: very first look at the pelican generated website with monospace
..          theme
..    :width: 100%

.. One thing annoyed me already about this theme. It does not cover all rst
.. items. For example it does not have styling for inline code-blocks..