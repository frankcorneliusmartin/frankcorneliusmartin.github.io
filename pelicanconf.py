from datetime import date
from pathlib import Path


SITENAME = "Franky.Codes"
SITEURL = "http://localhost:8000"

AUTHOR = "Frank Martin"
HEADLINE = "Biomedical Engineer &amp; Software Engineer"
DESCRIPTION = ""

PATH = "content"
TIMEZONE = "Europe/Amsterdam"
YEAR = date.today().year

DEFAULT_LANG = "En"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"
AUTHOR_FEED_RSS = None

# the key of this dict are the font-awesome classname
# TODO convert these to a list of tuples
SOCIALS = {
    "github": "https://github.com/frankcorneliusmartin",
    "linkedin": "https://www.linkedin.com/in/frankcorneliusmartin",
    "facebook": None,
    "pinterest": None,
}



DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {"images/favicon": {"path": "favicon/"}}
# Theme

THEME = Path(".") / "atom"

DESCRIPTION = "hello world"

# Disable the use of tags, these are shown for each post on the index
# pages (e.g home and the tags page) and shown above each post on the
# post page.
SHOW_TAGS = True

# Disable the use of categories, these are shown for each post on the
# index pages (e.g home and the tags page) and shown above each post on
# the post page.
SHOW_CATEGORIE = True

# Setting this to true wil display the site name in the header next to
# the logo
DISLAY_SITE_NAME_IN_HEADER = True

# default tags url
TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"

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

PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# Show cover pictures in the blog index. This requires the use of the
# `cover`` metadata in the post.
SHOW_COVERS = True

# with open('content/extra/me.txt', 'r') as f:
#     ASCII_PICTURE = f.read()

PICTURE = "images/me.jpg"

# Apply a filter to the cover image.
COVER_FILTER = "opacity"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
