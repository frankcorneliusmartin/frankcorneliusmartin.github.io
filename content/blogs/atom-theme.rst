Atom Blog Theme
===============

:title: Atom Blog Theme
:date: 2025-09-01 9:00
:tags: python, pelican, html
:category: tech
:slug: atom-theme
:authors: Frank Martin
:summary: I've made the theme that I created for this blog open source.
:cover: /images/atom-theme/pelican-logo2.png

.. sectnum::

.. contents::

When I started this blog I first looked for a static site generator. A static
website generator is useful for generating static html from text files. As I was
already familiar with Python and
`rst <https://en.wikipedia.org/wiki/ReStructuredText>`_ I found that
`Pelican <https://getpelican.com/>`_ suited my needs. The only issue I had with
it where the very basic themes which did not fit my brand. This is why I decided
to write my own theme and why not share it with others.

.. container:: scrollx

    .. figure:: https://raw.githubusercontent.com/pelican-themes/atom/main/showcase2.png
        :alt: atom theme
        :align: center
        :width: 600px

        It's a responsive theme

In this short blogpost I will highlight the available options in the theme. You
can find the source code of this theme on the official Pelican
`Github <https://github.com/pelican-themes/atom>`_, feel free to use and/or
modify it.

Basic settings
--------------
These are the mandatory basic settings used by the theme, this can be combined
with the
`Pelican settings <https://docs.getpelican.com/en/latest/settings.html#basic-settings>`_

.. code-block:: python

    # Used by other settings and used to generate absolute paths for images, so
    # make sure this is the public site URL
    SITEURL = "http://localhost:8000"


    # This theme supports writing you blog in multiple languages. This
    # specifies the default language when opening the blog for the first time.
    DEFAULT_LANG = "En"

    # Displayed as the title of the website both in the browser tab and in the
    # top menu bar of the blog.
    SITENAME = "Franky.Codes"

    # In case you want to show some ascii art in the left bar you can use the
    # following. You can see this blog post how to create such a picture
    # yourself:
    # https://franky.codes/ascii-picture.html
    # with open('content/extra/me.txt', 'r') as f:
    #     ASCII_PICTURE = f.read()

    # How many blog items should be displayed on the home page.
    DEFAULT_PAGINATION = 10

    # Used in embeddings when you share a link on social media and in the meta
    # data of your website. It is not shown anywhere in the frontend.
    DESCRIPTION = "hello world"

    # Used in the copyright notification in the bottom bar, leaving it like this
    # will always use the year of the latest builds, however you are free to
    # define it statically.
    YEAR = date.today().year

About
-----
These are all the options for the about section of the blog. The about section
is in the left bar. Containing a picture (or ASCII art), your name, a single
line of text and some icons to link to your socials.

.. code-block:: python

    # In case ASCII_PICTURE is not defined you can also provide an image to be
    # shown in the left bar..
    PICTURE = "images/me.jpg"

    # Used in the left bar underneath the author image.
    AUTHOR = "Frank Martin"

    # Used in the left bar underneath the author
    HEADLINE = "Biomedical Engineer &amp; Software Engineer"

    # Used in the left bar underneath the headline. It shows as a list of icons.
    # The keys of this dictionary are the names of font-awesome class names.
    SOCIALS = {
        "github": "https://github.com/frankcorneliusmartin",
        "linkedin": "https://www.linkedin.com/in/frankcorneliusmartin",
        "facebook": None,
        "pinterest": None,
    }

Menu bar
--------
These settings control the top menu bar. You can create a link to basically
anywhere. In the example bellow the default *tag* and *category* pages from
pelican are shown.

By default a Franky Codes icon is shown in the menu bar, you can change this
with a `font-awesome <https://fontawesome.com/>`_ or custom icon.

.. code-block:: python

    # Setting this to true wil display the `SITENAME` in the header next to
    # the logo.
    DISLAY_SITE_NAME_IN_HEADER = True

    # The items shown in the top menu bar.
    # TAGS_URL = "tags.html"
    # CATEGORIES_URL = "categories.html"
    MENU_ITEMS = (
        ("Projects", SITEURL),
        ("Curriculum Vitae", f"{SITEURL}/pages/curriculum-vitae.html"),
        ("Voorwaarden", f"{SITEURL}/pages/terms-and-conditions.html"),
        # ('Topics', f'{SITEURL}/{TAGS_URL}'),
        # ('Categories', f'{SITEURL}/{CATEGORIES_URL}'),
        ("Hire Me", f"{SITEURL}/pages/hire-me.html"),
    )

    # By default the 32x32 favicon is used. In case you want to use a
    # different one, provide the path to a (square) image.
    # MENU_ICON = 'images/me.jpg'

    # In case you want a font-awesome icon to be displayed next to the menu
    # item, provide the name of the icon here.
    # FA_MENU_ICON = 'home'

RSS and Atom feed
-----------------
It is possible to define custom endpoints for your RSS and Atom feeds.

.. code-block:: python



    # Relative urls to the generated atom feeds. ALL contains all blog post
    # and the CATEGORY and TAG contains filtered list of blogs linked to the
    # category or tag.
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
    TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"

    # Relative urls to the generated RSS feeds. ALL contains all blog post
    # and the CATEGORY and TAG contains filtered list of blogs linked to the
    # category or tag.
    FEED_ALL_RSS = "feeds/all.rss.xml"
    CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
    TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"


Homepage tiles
--------------
Each blogpost gets a tile on the homepage. These tiles can be customized. For
example each post can have an optional cover image with a certain hover effect.
The category and all the tags can also be hidden on the tiles.

.. code-block:: python


    # Disable the use of tags, these are shown for each post on the index
    # pages (e.g home and the tags page) and shown above each post on the
    # post page.
    SHOW_TAGS = True

    # Disable the use of categories, these are shown for each post on the
    # index pages (e.g home and the tags page) and shown above each post on
    # the post page.
    SHOW_CATEGORIE = True

    # Show cover pictures in the blog index. This requires the use of the
    # `cover`` metadata in the post. In case you do not provide it a placeholder
    # will be shown.
    SHOW_COVERS = True

    # Apply a css filter to the cover image. You can use "grayscale",
    # "grayscale-75", "grayscale-50" and "opacity"
    COVER_FILTER = "opacity"
