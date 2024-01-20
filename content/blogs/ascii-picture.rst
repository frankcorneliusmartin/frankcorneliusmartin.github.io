
ASCII picture
=============

:title: ASCII picture for this blog
:date: 2022-12-23 00:22
:tags: www, python, ascii, image processing
:category: tech
:slug: ascii-picture
:authors: Frank Martin
:summary: How I created the ascii picture using Python for this space.


When I started designing my blog I wanted create a look and feel of a
code editor. So instead of a regular picture I wanted to have a ascii
version.

At first I used an online tool to generate the picture. While it was
good enough to decide that I liked it, I felt it did not gave me enough
control over the result. So I decided to write my own in Python.

.. figure:: {static}/images/me.jpg
   :alt: original picture
   :width: 400px
   :align: center

   Original picture that I want to convert to an ASCII version.

Algorithm
---------
I remembered an algorithm which I have seen during a computer vision
course. Which computed the average intensity of a segment in the
picture and then matched it to a character with the same intensity.

I used the Python package Pillow (which is an python implementation of
PIL) for most of the image processing tasks.

Preprocessing the Image
-----------------------
The identity box on my website is 220x220 pixels. The first step would
be to crop the image to a square.

.. code-block:: python

   from PIL import Image
   im = Image.open("input.jpg")
   # I found this a nice cutout.
   # (left, upper, right, lower)
   im.crop((500, 100, 1500, 1100))

We want a (single) intensity value per image segment. In a color image
we have three values per pixel: red, green and blue. A first step would
be to convert the image to a gray scale image. There are many ways to
do this, but I decided to use the average intensity of the three color
channels.

.. code-block:: python

   # convert to grayscale
   im = im.convert("L")

Then, I normalized the gray scale image to use the full range 0-255 to
maximize the contrast between segments.

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
      * - .. figure:: {static}/images/me.jpg
            :alt: original picture
            :width: 180px
            :align: center

            The original loaded image

        - .. figure:: {static}/images/cropped.png
            :alt: cropped picture
            :width: 180px
            :align: center

            The square cropped image

        - .. figure:: {static}/images/grayscale.png
            :alt: gray scale picture
            :width: 180px
            :align: center

            The gray scale image

        - .. figure:: {static}/images/normalized.png
            :alt: normalized picture
            :width: 180px
            :align: center

            The normalized image


Segmenting the Picture
----------------------
Before we can compute the intensity per segment we need to split the
image into segments. I decided to use a grid to use 110 segments in ``x``
and ``y`` direction. So every segment is 2x2 pixels in the final
resulting ASCII-picture.

.. code-block:: python

   n_segments = 110
   (width, height) = im.size
   # compute the width (and height since we have a square image) of a
   # segment
   dw = width // n_segments

The cropped image with the grid looks like this:

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

.. figure:: {static}/images/segmented-image.png
   :alt: Segmented picture
   :width: 400px
   :align: center

   The original image with the segmentation grid.


I used the ``crop`` function of the ``Image`` class to split the image
into segments:

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
Before we can match the each segment to a character we need to compute the
intensity for each character. This intensity is dependant on the font that is
used. I used the `Ubunto Mono font <https://fonts.google.com/specimen/Ubuntu+Mono>`_,
which is the same font as this website. This code only works for
mono-spaced fonts. If the font is not mono-spaced the algorithm will
be much more complicated, as the final ASCII image is not a grid in that case.

The font size is not important when computing the intensities for each character, as
we are computing the average pixel intensity of the character box.

.. container:: toggle

   .. container:: header

         **compute_letter_intensity(letter: str)**

   .. code-block:: python

      def compute_letter_intensity(letter: str) -> float:
         img_dims2 = (font_size//2, font_size)
         img = Image.new('L', img_dims2, color='black')
         d = ImageDraw.Draw(img)
         d.text((0,0), letter, font=fnt, fill=255, align='center')

         data = img.getdata()

         n_of_pixels = math.prod(img_dims2)
         avg_intensity = sum(data)/n_of_pixels
         return avg_intensity

The function ``compute_letter_intensity`` returns the average pixel
intensity of a character. In other words, it sums the pixel values and divides
them by the number of pixels that are in the character box.

We want to match every segment in our preprocessed image to a character.
So we need to compute the letter intensity for all characters we want to
use in out final ASCII image.

I used a selection of letters, digits and symbols. Symbols like ``"``,
``'`` and ``/`` are not included, as they have a meaning within HTML. Another option
would be to escape these characters, but I decided to leave them out.

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
For each segment we match the letter with the most similar intensity:

.. code-block:: python

   chars = []
   for objective in segment_average:
      chosen_char = '*'
      distance = 1
      for char, intensity in intensities.items():
          di = abs(objective - intensity)
          if di < distance:
              chosen_char = char
              distance = di
      chars.append(chosen_char)

   # merge chars into strings of length n_segments
   result_string = ''.join(chars)
   n = n_segments
   lines = [result_string[i:i+n] for i in range(0, len(result_string), n)]

Making our final result:

.. raw:: html

   <div class="identity align-center">
   <pre class="picture gray">
   rrrrr++r++++++*****==============??????????????????||||?||||||||||||||||||||||||||||||||||||||||||||||||||||||
   rrrrr+++++++++*********==========??????????????????|?|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
   rrrrrrr++++++++*****===========????????????????????????|||||||||||||||||||||||||||||||||||||||||||||||||||||||
   rrrrrr++++++++**+***=*=====?====??????????????????==*??|||||||||||||||||||||||||||||||||||||||||||||||||||||||
   rrrrr+++++++++**+*==========??=????????????????+++=*+rr=||||||||||||||||||||||||||||||||||||||||||||||||||||||
   rrrrrr++++++++*****=========????????????=*+++^:!:::::!!!r?|????|||||||||||||||||||||||||||||||||||||||||||||||
   rrrr++++++++++***=*========????????????==+r;:,,..,~~~~:!!!r^^*?|||||||||||||||||||||||||||||||||||||||||||||||
   rrr+r++++*++++***=*=======?=???????????=r!,....,.,_,~,,~_!!:::*|||||||||||||||||ii||||||||i|||||||||||||||||||
   r+r++++++*+********=====?===??????????=!,.-````----...,~~~::~,!=?||||||||||i||i||i||||||i||||||i||||||||||||||
   r+++++++++**+**=*=*======????????????+!.``````````-..,,::_:::,:+=*||||||ii|||||||iiii||iii||||i|||||||||||||||
   r++++++++*****=*=*=======??????????*^:.`````````-......,,~:!!!:~!:=??|||iiiiiii|i|iiiii|i|iii|iiii||i|||||i|||
   r+++r++++*+***=*=========?????????=!.`````````````-.,,,,~:!::^!:::r?|?||iiiiiiii||iiiiiiiiiiiiiiiiii|i|i||||||
   ++++++++******==========?????????*~-``````````````-..,,:::~,~!r^:,,!++^=iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii|||
   ++++++++******======????=???????+,````````````````-.,...,,::~,:::!,._:::|||iiiiiiiiiiiiiiiiiiiiiiiii|iiii|i|||
   r++++++******=======?=?=???????r,```````-````--....,.,,~,.,::_:!!,:~._,,r|||iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
   +++++++***=*=*========???????=+,````````````---`-.,,,,,,,:~~,,,,:*_~:,::_||||iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
   ++++*+****==*=======????????*+:-``````````....```-.,,~:::_::::::,_^:,:,~:!?i|iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii|
   +++++*****==*=====?????????==^.``````````..-`````-.,~!+=??|||i??*!,!~,,.,,+i|iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
   ++++*****=*=======????????=?*,`````````-.,``````..,:!=|/7i/Tzzxxz(r~:,-.,.:riiiiiLiiiiLiiLiiiiiiiiiiiiiiiiiiii
   +++******========??????????=~```````` `...````...,~!*|ivliiTxlxsfjn?~:..,._?|iiiiiiiiiLiLLLLiiiiiiL/Liiiiiiiii
   +****=*=======?=??????????=,```  ``` `.--,``-..,,,:;=i/77/|)tYIjySwS|:_..,::=|iiLiL/LLLL//LLLLLLiL//LiiLLiiiii
   ++****=*===?=?????????????:```   ``  -.-.~-..,,,,:!+|)7lx)/zJ{y5emhhSl!,...,!?iii///L/L///L/L/LLLL//LLL/LLiLii
   ******======?????????????r-``       `..-~...,,:::!^?i(c(viTJ{j54khhkmaJ:,..,,!*|ii/)/)L//L////////////L/i/iLii
   *******=======??????????*.``        `-`.,..,~_:!:^=|)v)/vxtfjoSeEAAEEEmc,...,.:+iiL))/)/)L///L//)///)//////iLL
   ****=*======?????????|?=!``         `-`...,,~::!^+?|c7vTzzIj3ZmhUU6UUU64*.--.,,!|///())(////)///)()))/)/)/////
   *****========??????????r:`         ````..,,,::!^+=|iv7v1Juy4mEAAqKKKpKKE5_---...r|/ccccc)())c()))c)))))())))//
   *=*=======??????????|??+,`         ```-..,,~::!r?|i)vTzIuySmEU69KKdbdddKA|.-.....+icccc))c((vcc)cvvcc/ccc(/(/(
   ***======??????????||??r-``        ```..,,,~:!!r?|iLTxFuj5VkE66qKKdODOOdUj:.-..-.~?vcv7c(cvv7vvv7vvvc)(cccc)/(
   =*======?????????|||||?~`         ```-..,,,~:!!r=|/lxtfjy5whhE6qKdODMMROdm?,`..-.,:)vvvvv77777TTv77vvvvvvccccc
   *=======?????????|||||=.         ```-..,,,,~:!;r*|ilzt[y5SeemXAqdHRRWgWRHEl:.-..-~,!7777777TTTTTT7TTTvv7vcvvvv
   =======????????|?|||||!`        ``-..,,,,,,~!!!^*|/lxJ[jyyyy5kUKdRMMg08MDh1^,-..-.:~vTlvl77TlllTT7TTTvTT7vv77v
   ======?????????||||||?:`        `..,,,,,,,,~!!^^+|cxx1n[{ssj5hUdDRM0NN00MAJ?^..,.-,!LlllTllllllllTlTlTT77TTTTT
   ====????????|||||||||!,        `-.,,,,,,,,,~:!r+*|cxxzIsxt{5kUdDDMgN&&&NgKs|r,-,...!|TlllxxlxxxlxlllllTllTTlTT
   =====????????|||||||?,`   ``  ``..,,,,,,,,,,:;+=?7xzxzx11C5mUdDMRM0&&&&&ND5=r!-....++Tlxllxxxxxxxllllxxlllllll
   ===?????????|?||||||*:````    ``.,,,,,,,,,,~:^+?izJYtzl1I5kUKOg000&&&&&&&86i:!.-...r+7xzxxxxxxxxlxxxxxxlllllll
   =?=????????|||||||||+;``` `   ``.,,,,,,,,,,,:^+=c1{{[11tok6dHRN#####NN0&NNOt:~,....;?Lxxxzzxxzxxxxxxxxxxxlxllx
   =???????????||||||||r!`-` `   ``.,,,,,,,,,,,:^r=)1jjysJ{wUdOH0&###&0g0ggNN8k:.,...,!|cxxzzzzxzzzzxxxxxzxxlxxxl
   ???????????|||||||||=!`-``    ``.,,,,,,,,,,,:^r=i1jS5js[mEKddMMM8RRdAhK80&gd^.,.,.,!|7xzzzzzzzzzzxxxxxxxxzxxxx
   ?????????|||||||||||?!`-```   `-.,,,,....,,,:!r?i1[Z5y{s2kkZmEj7i|i11x15dN0D=-.-...!ixzzzzzzzzzzzzzxzxzzzzzzxx
   ????????|||||||||||||;.```    `...,,..-----.~!^r|)t5jyytj5ySyjirr;r;r|itnURD=``..,,;Tzzzz11zzzzzzzzzzxzxzzzzxz
   ?????????||||||||||||=~````   `....-````````-.,:r?LnC[ys[Syntx?:!ri[S4jzLiKR|-`,.~,?lzzz1111zz11zzzzzzzzzzzzzz
   ???????|||||||||||||||^-```   `....`````---`---,~;=|xCSSyjj5[r?tY11yKDMOdkzG1`-,.:!?xzz1111111111zzzzzzzzzzzzz
   ??????|?|||||||||||||||,```   `...-``..~:_~,,,,.-,:!r1mmjmh{rYi^^=cnjPKOOdh{1`.:.!:|xzzz11111111111zzzzzzzzzzz
   ???????|||||||||||||iii!```   `..---.....,:_,..,.-...~:::+Sr1+~:!!!*it5mU9Gm*,^:,;,izz111111111t11z1zzzzzzzzzz
   ????????||||||||||||iii!```   `..-....--.,,::,-...``.r[1AK!|r~!!_,,!+*^|JjSm*~+r,:,?x111t11111t111zzzzzzzzzzzz
   ????????||||||||||||iii;```   `-.....---````.,.-..,,,?kkmD|Y!r^!:,.I=mc?kdRW{:!^,,.+z11111t11111111z1zzzzzzzzz
   ??????|||||||||||||||iir```   ``.,,..--.-``.,.`-...,,=ZKkH7ux|:!:!_^YE4IER&Nj=|:,.-!zz1111t11z1111111zzz1xzzzz
   ??????|||||||||||||iiii*````  `.,,,..`-.-.```.`-..-.,?odKXTuv^!+?=?IEmEAdMNNyJ*!,-`:x111t11t11111111zzzz1zzzzz
   ????||?||||||||||||iiii?.```  `..,,,.--...--..`-..`-~?jOW5v!|^!^*|{e6AdORW&Njk;,.``,x11111111t111111z1zzzzz1zz
   ?????|||||||||||||iiiii|~``` ``..~,,.........-`--.`.:?SONEj^J|rr?z[kU6ORM0NNjd!,-``,/z1111tt1t1111111z1zzzzzzz
   ?????|?|||||||||||iiiiii!``````,.,,,,.......-``--.`.~?5Kg05TXj1vcJjemqR0ggNph%^.``-.i11111tt111t11111111zzzzz1
   ????|||||||||||||||iiiii?.`````,,,,,.......-------`.,=2qRNR{Y6SySmEp6R&NNgNjgR=,`-,,v111t111t1111111z1111zzzzz
   ??????|?||||||||||||iiii|~````-,,.,,.,.....----..`..,r5KD0NAlP9EEA6K6DNgggAP0%L..,!!zzz11t111111tt11z1zz111z11
   ??????|?||||||||||i|iiiii;````-,,.,,,,,..........-..,^yKHRNgjiAKqUq9kdRMMEyN0Dx-,;**z1111111t11111t1z1zz1zzzzz
   ?????|?||||||||||||iiiiii?.````,,,.,,,,,........-...,^[UdR8&Hti5qAhE4qOdnk&NNRl,+{itz11t111t1t1t1111111zzzzzzz
   ??????||||||||||||i|iiiii|,-```,,,,.,,,........`...,,;FEKORg0KCi|)xxv1s28&&&N%z=1kj5z1t1tt11tt1ttt11111z11zzzz
   ?????|?||||||||||iiiiiiiii~.```,,,,,........---....,,^zEKHHR08HEwS4X6b%M0NNN0D4ElSdPt111tttt1ttt1t111111z1zzzz
   ????|?|||||||||||iiiiiiiii_.```,,,,,,,....--.......,,rzEdOHHR%bKKKKddDM0N&#&NOdHvGgKt11ttttt1ttttttt1111zz1zzz
   ????|?||||||||||i|iiiiiiii,.``..,,,,,,,,,..........,~=zkMOROHdqUKKddHM0##&&&NDDK)K0d11ttttt1ttttttt1t1111111zz
   ???|?||||||||||i||iiiiiiii,.`-,.,,,,,,,,.,,........,~?tmdddRH$hXEUdHRg&##&N&0DMG9gMdtttttttttttt1tttt1111z11zz
   ??|??||||||||||||iiiiiiiii~,.`,,,,,,,,,,,,,.....-...,?sZA^*$O6hkXUbDMNN##&&Ng%WKRNMUttttttttttttttttt111t111zz
   ??|??||||||||||||iiiiiiiiL:.,..,,,,,,,,,,,,.....-.- `!13t.,3OhEUAUdDMNN##&&NgDD#B#getttttJttttJtttttt1z1t1111z
   ??||||||||||||||iiiiiiiiii^,,,.,,,,,,,,,,,,.....-.-``,?3El?5pmAdbKd%RgN&&NNNRRg#B&MCtttttJtJtttttttttt1ttt111z
   ??|||||||||||||iiiiiiiiLLi|,,,,,,,,,,,,,,,,......--`..;xliJm4mqDRDO%RM0NNNN0MDNB#NXJttttJttJJJtJttttttttttt11z
   ?|?|?||||||||i||iiiiiiLiLLi!,,,,,,,,,,,,,........-`-,:!::!|iJ36ORMRRRgNNNNNNWORNgEJttttttJttttJJJttttt11ttt1zz
   ???|?|||||||||||iiiiiiiiL/L|_,,,,,,,,,,,,.......-``-.,...:+?i146dRMMW00N000N8DyyntJttttttJJtJJttJttttttt11tt1z
   ???|||||||||||iiiiiiiiiiLL/)|:,,,,,,,,,.,......-```--.,-.~^!!i1nkUdM880N0N&NgDsJJJJttttJtJJJJJJJJJttttttttt111
   ?||||||||||||||iiiiiiiiiLL////|r~,,,,,,,,....-``````-,.-.!^r^||TFjmKRg0NNNNNgHJJJJttJJJttJJJYJtJJttttt1tttt111
   |??|||||||||||iiiiiiiiiiLiLL)/L|r,,,,,,,...-```````.,:_~!/xi*r=l)7jXKgN&NNNg8dJttJJtJJttJtJJJJJtJJJJttttttt111
   |?|||||||||||||iiiiiiiiiLL/)/)))/!,,,,,,,.-``````-..,:^i7tnj[sxtl||z2d0&&NN0M6JtJJtJJJJtJJJJJJJttJJJttttttt111
   ||||||||||||iiiiiiiiLiLLLL/)/))/)+,,,,,,,.`````-......_=?(JuIJj5ji||yd0NN008MkJttttJJtttJJJJJJJJJJJJttttttt11t
   ?|??|||||||||iiiiiiiiiLiL////)()ci,,,,,,,.-``------...~**iJyjFnIi:^|Z%gNN00WRoJttJJJJJtJJtJJJJJJJtJJJtttttt111
   |||||||||||iiiiiiiiiiLL/L///))))(c:,,,,,,..-``````--.,!:!^is3jjSey^76%000NgMOFttJJJJttJJJJJJtJJJJJJtttttttt111
   ||||||||||||iiiiiiiiiLL///(/))(/ccr,,,,,,,..-..---..~;?=?LI4k4wEDD5J6OW000M%htttJtJYttJJJJJtJJJJJJJJJttttttt11
   ?|||||||||||iiiiiiiiiLiLLL/)))vvcci,,,,,,,........-.,!+*?Ts55ZEdDRKEpdRWWgRbjJJJtJtJtJtJJJJJJJtJttJttttttttt11
   |||||||||||||iiiiiiiiLLL////c(cvcvv!,,,,,,,..........:!r*izjZX9bD%OKKHDRMDOEJttttJJJJJJJJJJJJJJJttJtJtttttt111
   ?|||||||||||iiiiiiiiiL////))())ccv7|,,,,,,,......-`-.,,,:!*|x{6ODDOHddO%RHKEJJJttJJJJJJJJJJJJJJJJJJJttJtttt11t
   ?|||||||||||iiiiiiiiLiLL///)()cc(cvc~,,,,,,.......-```-.,.:?nEqOODR%OHOD%KK6YttJJJJJJJJJYJJtJJJJJJJJtttt1tt1t1
   ||||||||||||iiiiiiiiLLL///)))(cc(cvv!,,,,,,...,,,...--`-.:=jApdD%DRRDOH%dKD9JJtJJJJJJJJJJYYJJJJtJJJtJtJttttt1t
   ||||||||||||iiiiiiiLLL/////))cccccvv!,,,,,,...,,......,~^|IEKdHO%RMMR%OHpORKsJtJJJJJJJJJJJtJJJJJJJJttJttt111t1
   ||||||||||iiiiiiiiiiLL///)))cvvcvvvvr,,,,,,,.,,......,!*|x2UKH%DRMMRROdqHRMKJJJJtJJJJYtJJJJJtJJJJJJJJJJttttttt
   ||||||||||i|iiiiiiiiLL///)()vccccvvT=,,,,,,,,,,,....,~;+?ty54UdMM8ROOd9KRMWdYJttJtJJJYYJJJYJJYJJJJJJJJtJtt1ttt
   |||||||||||iiiiiiiii/L//)//cccvcvvvv?,,,,,,,,,.,..-..~:!+?tn5SqKOHKdqU9%WggOYttJJJJJJJJYJYJJYYJJJtJJJJJtJtt11t
   |||||||||i|iiiiiiiii/////)/))(ccvvv7|,,,,,,,......`-.,,_;+i1JykE6PXUhAHM800DYJJYYJJJJYYJsJJJJYJJJYJJJtJttttttt
   |||||||||i|iiiiiiiiiL///)())c)ccvcvvi,,,,,,,..----``.,.,:!+=?z353J2kEK%g0N0DstJYJYJJJJJYYsJJJJJtJJJJJttJJtJtt1
   |||||||||i||iiiiiiL/L/)//)c(c(cvvvvv/,,,,,,,,.---````.,,,:!*?|)1i=lhqbRW00gDIJJYJYJYJJJYYYJYYJYJJJJJJJJJJJtt1t
   ||||||||||ii|iiiiiLiL////))cvvcvcvvTc,,,,,,,,,..--```-...,:;;*rr^i4UKOW0NNg%nJJJJYJJJJYJJYJJsJJJJJJJYJJJJttttt
   |||||||||||iiiiiiiiiLL///((c)vvvvv77v,,,,,,,,,,..--`---.-.~:::!rce6KOR8gNN0RfYYJJJJJJJJJJYJJYJtJJJtJJJJJJtJt1t
   |||||||||i|iiiiiiiLi////)))))vcvcTv7v~,,,,,,,,,.,..-......,,!+?J4E$dRWg00NgRjYYsYJYYJJJJJYYYYJJJJJJJJJtttJJt11
   |||||||||iiiiiiiLiLiL/)))(c)c(c77v7TT:,,,,,,,,,,,,,,,,,,,_:^|YjVEUKDMWg00NgR3JJsYsYJJJYJJYYJJJJJJJJYJJtJJttttt
   |||||||||i|iiiiiLiLL/L)))cv(ccv77Tv77:,,,,,,,,,,,,,,,,~:!^=ctn5hUdORWWgg000MmYsYYYsJJYYJJJJJJYJJYJJJJJJJJttttt
   |||||||||iiiiiiiiiLLL////(c)ccv7TvTlT:,,,,,,,,,,,,,,,,~:!r|ljZEqdDRMRgg0M8gMEYYJJYJYYYJJYJJJJJJJJJYYJJJJtJtttt
   |||||||||i|iiiiiiLiL////)c(cvcvv777TT:,,,,,,,,,,,,,,,~:!r?T{ShKORRMWM0000N08KssYYsYYYJJJsJJJJJJJJJYYJJJtJJtttt
   |||||||||iiiiiiiLiiiL//)ccccvccvTcTT7:,,,,,,,,,,,,,,,:!*)s3k6d%MWMW8gg00NN0gOssYYssYYJYYYYJJJJJJYJYYYJJtJttttt
   |||||||||iiiiiiiiLLL//L))ccvvvvv7vTTl_,,,,,,,,,,,,,,_!*vC2G$dDM8gggMRggg0NNNMjsYssJYYYYsYJJJYJJJJJYYYJtJJJtttt
   |||||||||iiiiiiiiiiLL//))(cvcvvcvv77T_,,,,,,,,,,,,,,:^|tykUdDRMg00gWMWW0NN&NWA[lltJYsYJJYJJYJYJJJJJJtJJtJttttJ
   ||||||||||iiiiiiiiL/////)c)cvvcc7v)?;,,,,,,,,,,,,,,~!*)CSPKORgg000gMRM8gNNN&gdEj!!itYYJYJJJJJYYJtJJJJJJJJJtttJ
   ||||||||||iiiiiiiiLL//////)(ccv/?!.` .,,,,,,,,,,,,,~!?lfVEdRg0g0g08MRRgg0N&&0OpUXi,!lttYYJJJJJJJJJJJJJtJJttttt
   ||||||||iiiiiiiiiii///////((ci!.-`  -,,,,,,,,,,,,,,:^?vjmAdRWgg00gMRRRW80N&&NRdp6EY.izxxtJJJJJtJJJJJYJJttttttt
   |||||||||iiiiiiLiLLLLL/)/)/i;.--`  -,,,,,,,,,,,,,,,,!?TuV6HRRMM88MR%%RMWgN&NNMHdK9E!i11T?^)1JJJJJtJJJYJJtttttt
   |||||||||i|iiiiiiiiLi/L/LL^.``````-.,,,,,,,,,,,,,,,,:=LYSUODDRRRRR%ODRM8g00NNgOHKKA^i1txi:|7x1tttJJJJJJttttttt
   ||||||||||iiiiiiiLiiL///i:-```````-.,,,,,,,,,,,,,,,,,^|zZKHHO%DRDDOODRMggg0NNgDHdKkrcztzc^LlllxtJJJJJJJttttttt
   ||||||||||||iiiiiiiiiL/?,-````````-.,,,,,,,,,,,,,,,,,:+cSKdddOO%DOHOORMW8800N0RObdt|zzt1i?vz1zxlzttJtJtttttt1t
   ||||||||||||iiiiiiiLii!.```````````..,,,,,,,,,,,,,,,,,^iVKdKdO%%DHddHDRMgM8g0gROdK|vzz11?izz1zxxlTzttJtttJt1tt
   |||||||||||||iiiiiii=,`````````````..,,,,,,,,,,,,,,,,,:?y9KdHDRDOdddODbRMMWMgMRHOIilxxzz=l1ttzzxTvTx1ttttttttt
   |||||||||||i|iiiii|:.```````````````..,,,,,,,,,,,,,,,,_rsk6KdODDHdKdHddORMMMMRRH5ivlxlzL|zttt11zzxxl7lztttt1tt
   ||||||||||||i||ii^.-````````````````-.,,,,,,,,,,,,,,,,~^zSh9KHOOdKKKddHODRRRRRRe|cllTcx=l1t1t11zxxllllTx111111
   |||||||||||||||+,-```````````````````-..,,,,,,,,,,,,,,:rxyk6KdHHKKKKKdddOOODD%m|/TTTTT||zYJt11zxxllxzxllvTzz11
   ?||||||||||||?:-``````````````````````-..,,,,,,,,,,,,,:rlymEqdddKKKpKKKddOOOOy|i/()vl7=?^Ytt1zxxxxxlllTlll7vlz
   ??||||||||||;.-````````````````````````-..,,,,,,,,,,,~!+ljwE9ddKKKKKKpppKdH6z|||iicv7?i:~1t1zzxzxxllxllllll7cv
   </pre>
   </div>

   Funny enough, I did not use this image in the final version of this website. But I
    still like it, so I decided to include it here.