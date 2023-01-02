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
maximize the contrast between segments.2

.. code-block:: python

   from PIL import ImageOps
   # normalize the image
   im = ImageOps.autocontrast(im)

.. container:: scrollx

   .. list-table::
      :widths: 25 25 25 25
      :header-rows: 1
      :align: center

      * - Original
        - Cropped
        - Grayscale
        - Normalized
      * - .. figure:: {filename}/images/me.jpg
            :alt: original picture
            :width: 180px
            :align: center

            The original loaded image

        - .. figure:: {filename}/images/cropped.png
            :alt: cropped picture
            :width: 180px
            :align: center

            The square cropped image

        - .. figure:: {filename}/images/grayscale.png
            :alt: grayscale picture
            :width: 180px
            :align: center

            The grayscale image

        - .. figure:: {filename}/images/normalized.png
            :alt: normalized picture
            :width: 180px
            :align: center

            The normalized image


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

         **Visualization code**

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


To actually segment the picture I used:

.. code-block:: python

   im_part = im.copy()

   segments = []
   for i in range(n_segments):
      for j in range(n_segments):
         segments.append(
               im_part.crop((j*dw,i*dw,(j+1)*dw,(i+1)*dw))
         )

.. container:: toggle

   .. container:: header

         **Draw images segments**

   .. code-block:: python

      def display_many(images: List[Image.Image],
                 dim: tuple=(1, 1)) -> Image.Image:

         assert math.prod(dim) == len(images), 'Thats not a grid'
         n, m = dim
         img_w, _ = images[0].size

         new_image = Image.new('L', ((n)*img_w+n+1, (m)*img_w+m+1), 255)

         for i in range(1,n+1):
            for j in range(1,m+1):
                  idx = (i-1)*m + (j-1)
                  new_image.paste(images[idx], ((j-1)*img_w+(j), (i-1)*img_w+(i)))

         return new_image

      display_many(segments, (n_segments, n_segments))

   .. figure:: {filename}/images/segmented-image2.png
      :alt: Segmented picture
      :width: 400px
      :align: center

      The segmented pictures displayed in a grid.



Computing Letter Intensities
----------------------------
Before we can match the segments to letters we need to compute the
intensity per letter. This intensity is dependant on the font that is
used. I used the `Ubunto Mono font <https://fonts.google.com/specimen/Ubuntu+Mono>`_,
which is the same font as this page uses. This code only works for
mono-spaced fonts. If the font is not mono-spaced the algorithm will
be much more complicated, as the final ASCII image is not a grid.

The font size is not important when computing the intensities, as they
are relative to each other.

I used a selection of letters, digits and symbols. Symbols like ``"``,
``'`` and ``/`` are not included, as they have a meaning within HTML.

.. container:: toggle

   .. container:: header

         **function to compute intensity of single letter**

   .. code-block:: python

      def compute_letter_intensity(letter: str) -> Union[float, Image.Image]:
         img_dims2 = (font_size//2, font_size)
         img = Image.new('L', img_dims2, color='black')
         d = ImageDraw.Draw(img)
         d.text((0,0), letter, font=fnt, fill=255, align='center')

         data = img.getdata()

         n_of_pixels = math.prod(img_dims2)
         avg_intensity = sum(data)/n_of_pixels
         return avg_intensity

.. code-block:: python

   # define the characters to use
   charactersList = list(string.ascii_letters + string.digits ) \
      + [' ', '!', '?', '.', ',', ':', ';', '(', ')', '[', ']',
         '{', '}', '/' , '|', '-', '_', '=', '+', '*', '&', '^',
         '%', '$', '#', '@', '~', '`']

   # load the mono-spaced font
   fnt = ImageFont.truetype("fonts/UbuntuMono-Regular.ttf",
                            size=font_size)

   # compute the intensity of each letter
   intensities = {}
   for char in charactersList:
      intensities[char] = compute_letter_intensity(char)

   # normalize values between 0 - 1
   low = min(intensities.values())
   high = max(intensities.values()) - low
   for k, v in intensities.items():
      intensities[k] = (v - low) / high


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