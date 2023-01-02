:title: ASCII picture for this blog
:date: 2022-12-23 00:22
:tags: www
:category: tech
:slug: assci-picture
:authors: Frank Martin
:summary: How I created the ascii picture using Python for this space.

ASCII picture
=============


When I started designing my blog I wanted create a look and feel of a
code editor. So instead of a regular picture I wanted to have a ascii
version of myself.

At first I used an online tool to generate the picture. While it was
good enough to decide that that was indeed a good idea, I felt I did
not have anough control over the results. So I decided to write my own.

.. figure:: {filename}/images/me.jpg
   :alt: original picture
   :width: 400px
   :align: center

   Original picture that I want to convert to an ASCII version.

Algorithm
---------
I remembered an algorithm which I have seen during a computer vision
course. Which computed the average intensity of a section in the
picture and then matched it to a character with the same intentsity.

I used the Python package Pillow (which is an python implementation of
PIL) for most of the image processing tools.

Preprocessing the Image
-----------------------
The box on my webpage is 220x220 pixels. So I cropped the image to a
square so that it mathes the shape.

.. code-block:: python

   from PIL import Image
   im = Image.open("input.jpg")
   # I found this a nice cutout.
   # (left, upper, right, lower)
   im.crop((500, 100, 1500, 1100))

We want a (single) intesity value per image segment. In a color image
we have three values per pixel: red, green and blue. A first step would
be to convert the image to a grayscale image. This can be easily
achieved by computing average of the three color channels per pixel.

.. code-block:: python

   # convert to grayscale
   im = im.convert("L")

Then, I normalized the grayscale image to use the full range 0-255 to
maximize the contrast between segments.

.. code-block:: python

   from PIL import ImageOps
   # normalize the image
   im = ImageOps.autocontrast(im)


Segmenting Picture
------------------
In order to compute the intensity per segment we need to split the
image into segments. I decided to use a grid to use 110 segments in x
and y direction. So every segment is 2x2 pixels in the final resulting
assci-picture.

.. code-block:: python

   n_segments = 110
   (width, height) = im.size
   # compute the width (and height since we have a square image) of a
   # segment
   dw = width // n_segments

To visualize the segments I created a new image and drew the segments:

.. container:: toggle

   .. container:: header

         **Show code**

   .. code-block:: python

      # make a copy of the image, as we do not want to have the
      # segmentation gizmo in the final image
      im_ = im.copy()

      d = ImageDraw.Draw(im_)
      for i in range(1, n_segments):
         d.line((0, i*dw, img_h, i*dw), fill=255)
         d.line((i*dw, 0, i*dw, img_h), fill=255)

      display(im_processed2)

.. figure:: {filename}/images/segmented-image.png
   :alt: Segmented picture
   :width: 400px
   :align: center

   The original image with the segmentation lines.



Computing Letter Intensities
----------------------------
Before we can match the segments to letters we need to compute the
intensity per letter. This intensity is dependant on the font that is
used. I used the `Ubunto Mono font <https://fonts.google.com/specimen/Ubuntu+Mono>`_,
which is the same font as this page uses.

- font size
- monospace

.. code-block:: python

   charactersList=list(string.ascii_letters + string.digits ) \
      + [' ', '!', '?', '.', ',', ':', ';', '(', ')', '[', ']',
         '{', '}', '/' , '|', '-', '_', '=', '+', '*', '&', '^',
         '%', '$', '#', '@', '~', '`']

   # load the mono-spaced font
   fnt = ImageFont.truetype("fonts/UbuntuMono-Regular.ttf", size=font_size)


Match letters to segments
-------------------------

.. code-block:: python

      import math

      import numpy as np
      from PIL import Image, ImageDraw, ImageOps, ImageFont
      from typing import Union, List


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