from datetime import date
from pathlib import Path


SITENAME = 'Frank Martin'
SITEURL = 'http://localhost:8000'

AUTHOR = 'Frank Martin'
HEADLINE = 'Biomedical Engineer &amp; Software Engineer'
DESCRIPTION = "My personal playground"

PATH = 'content'
TIMEZONE = 'Europe/Amsterdam'
YEAR = date.today().year

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# metadata for social platforms
TWITTER = {
    'handle': 'fcmartin'
}

# the key of this dict are the font-awesome classname
SOCIALS = {
    'github': 'https://github.com/frankcorneliusmartin',
    'linkedin': 'https://www.linkedin.com/in/frankcorneliusmartin',
    'facebook': None,
    'pinterest': None
}


DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Theme

THEME =  Path('.') / 'pelican-atom'

DESCRIPTION = "hello world"
TAGS_URL = 'tags.html'
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

ASCII_PICTURE = \
r"""
rrrrr+++++++++*****==========?==??????????????????|?||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
rrrrr+++++++++********===========??????????????????|?|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
rrrrrrr++++++++*****===========???????????????????????|||?||||||||||||||||||||||||||||||||||||||||||||||||||||
rrrrrr++++++++********=====?====??????????????????===?||||||||||||||||||||||||||||||||||||||||||||||||||||||||
rrrrr+++++++++****==*=======??=????????????????+r*=+rr+?||||||||||||||||||||||||||||||||||||||||||||||||||||||
rrrrrr++++++++******=======?????????????**++r!:::::::!!!*||???||||||||||||||||||||||||||||||||||||||||||||||||
rrr+++++++++++*****=======?????????????=*r^:,...,,~_~~!!!!^;r?||||||||||||||||||||||||||||||||||||||||||||||||
rrr+r++++*++*+***=*=======?????????????+!~..-..,,~,,,,~~:!!::!||||||||||||||||||i|||||||||||||||||||||||||||||
r+r++++++*+********====??=?=??????????+~.-`````--`-..,,~~~::,~+?||||||||||i||i||i||||||i||||||i|||||||||||||||
r+++++++++*++**=*=*=====????????????=r~-`````````-...,~:::::~,;*r?|||||ii|i||||||iii||iii||||i||||||||||||||||
r++++++++*+*****=========?????????=+!,``````````......,,,::!!::::r???||iii|iiii|||iiii|i|iii|iiii||i|||||i||||
r++++++++*+***=*=========?????????r~-````````````--,,~,,~:!:!;:::!=???||iiiiiii|iiiiiiiiiiiii|iiiii|i|||||||||
++++++++******==========?????????;.```````````````...,~:::~,_!r!,,_rr!^|iiiiiiiiiiiiiiiiiiiiiiiiiiiii|iiii||||
+++++++*******======???=????????!.```````````````-.,,...,~::~:::::,,::,+||iiiiiiiiiiiiiiiiiiiiiiiii|iiii||||||
r+++++*******=======?=????????=!.```````-```---...,,.,,~,.,:_~!;:,:,,,,!|i|iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
+++++++***===*======?=??????==^.```````````-.--`-.,,~,,,,__~,,,:r!,:~~:_=|||iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
++++*+****==*===?===???????=*^,``````````....-``-.,,~:!!:!!!!!::,:;,,_,~!*i|iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
+++++***+**=======????????=?*:``````````..-``````.,,:r?|||||)i||+__!,,,..!||iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
++++*****=*======?????????==;-`````````...`````...~!+|iT(ivzzxzt1i!,:...,:!|iiiiiiiiiLLLLiiLiiiiiiLiiiiiiiiiii
+++******========??????????^-``````` `.-.-```...,,:r?i(l)i/llxJjj51!~~-,.,=|iiiiiiLiiLiLLL/iiiiiiL/Liiiiiiiiii
+**+**=====?==?=??????????r.``   ``  `.-..`-..,,,:!r|LcTTi/zsCjy5mknr:,..~,^|iiiiL/LL/L//iL/LLLiLL/LiiLLiiiiii
++***==*=====????????????=,``    `` `...:....,~,:!^?ivTxviTJFy54mhPmj|_...,_+|iiL////L///L/L/LL/L/L/LL/LLiLiii
****=*======?????????????:``        `.`,,-.,,~:::^*|)))c)ctnj5VkhAXkmy?,...,_;?iLL)))L//L//)L//////)/L/L/LLLii
*******======???????????;```       ``-`,..,,~:!!!+|i7v((l1njy3eXA6EEAhy:..-.,,^iii))/)))L///L//)///)//////LLLL
****========?????????|?+~``        ```-...,,::!;r=|/vTvztJj24mE6$U$$9UhY,---.,,=/L/c)(()))/))/)(c())/)))//////
****========???????????^,`         ```-..,,~::!r=?icv7zJnjZkEUA$KKdKKK9hr.--...:?L(vcc()c))cc)))c(()))cc)))/)/
*=*=======??????????|?=+.``        ```...,,::!;+|iicTxsnySwXU6UK$dHHdddU[,--..-.!|cccv()(ccvcc)cvvcv)cc(()(/))
***====?=??????????||?=!```       ```-..,,,_:!^*?iLvxY{jySmhE6UKKdORDDOKm+,`....,r(ccvvcvvv7v7vv7vvcc(cvcc))cc
**======????????||?|||*-         ````...,,,:!!^+?|ll1sjy5VkkhAUKdOOMWM%b6z:.-..-~,?vv7v777T7TTTT7TT7cvvvcvcccc
========?????????|||||;`         ``-..,,,,,:!!^r?|cxtCj35S4VmEqKH%MWg8MD6n;,-..-.:,)TT7T77TlTlTT7TTT777vvvvvvc
======?????????||||||?:`        `-.,,,,,,,,:!;!^?iTlzs[yj[[ye6Kd%MMg0ggR9n?!....-~:LllTTTTlllllTTTTT77T77v777v
=====??????????||||||^~        `-.,,,,,,,,,:!^^r?ilxzJ[F1s{ykUdDRM0NNN0gdfir,.,.-.:|lllllllllxllTlllT77TTTTTTv
====????????|||||||||:`    `  ``..,,,,,,,,,:!^++|Lzxx1JtzC3mUKD%R8N&&&&NDo|+!-....!=TlxllxxxxxlxllllllllTTlllT
===?=???????|?||||||+,`` ``   ``.,,,,,,,,,,_!^=?iz1zzzxts3m6d%WMM0&&&&&NMAL^^.-...^rvlxxxxxxxxxxllxxxxllllTlll
==?????????||?||||||^: ```    `-.,,,,,,,,,,:!r*|7tIstxzs2k6KHg0N&##&&&&&0dJ!:,`...!*/xzxxxxxxxxxxxxxxxllxlllll
===?????????||||||||^:``` `  ``-.,,,,,,,,,,_!r+|lsjjsttjm6KHO0#B##&NN00NNW4!,~....!?ilxxxzxxzzxxxxxxxxxxlxxlll
=??????????||||||||?r:`-```  ``-.,,,,,,,,,,~!r+|vI32jYs5EKOHM&###&gRRWgNN0d=.,....:|)xxzzzzzzzzzxxxxzxxxxxxxll
???????????|||||||||=:````   ``-.,,,,,,,,,,~!^+|7Iye3[I5k6pUHdK9AEAmjSK8&0DT-.....:|vxzzzzzzzzzzzxxxxzxzzxzxxx
?????????|||||||||||?:````   ``..,,,......,~:^r?LJySjysC5mS5mn|*+r?iL/xSHgRJ-`....:Lxzzz1zzzzzzzzzzzzzzzzzzxzx
????????|||||||||||||!.```    `.....--`````.,:!ri/uj[ynJy2yyFi+;:;^r|??)3dRs-`,.,,^7zzzz11z1z1zzzzzzxzxzzzzzzz
????????|||||||||||||?~```    `....`````````-.,:^?cJCy2u5ynCYr^?x{mdRRdm/xOS-`,.~,*lzzz1111zz111zzzzzzzzzzzzzz
???????|||||||||||i|||r-```   `...````.,,,....-.~!r?lywSj5m{r1x|i)1SKORDdPJk``,,::|xzzz111111111z11zzzzzzzzzzz
??????|?|||||||||||||||,```   -...`-..,~~~~,..,.-,,:*tsljEyrJ*:!r|Tj3hqHHAEY-.:,!,|xzz1111111111111zzzzzzzzzzx
???????|||||||||||||iii~```   `..-....--,~::,-...-``._!^?x:x^~:::~:;*)t3e53*~v!,:~=xz111111t11111z1zzzzzzzzzzz
????|???|||||||||||iiii~```   `......-----.,!,-.....![knR4!?:!;:_.r;Y=;1VEdC!:*,,.^z1111111111111zz1zzzzzzzzzz
???????||||||||||||||ii:```  ```..,.----```-.---..:.!u9yOUi=?^!:!.r?Gk(oHgNZ=^r~,.!z1t111t111z111111zzzzzzzzzz
??????|||||||||||||iiii!```  ``.,,,.-`..-``,..`.....!tAKUA|3?!^r!:^smm56R&NS1|!,.-:zz1111t11z1111111zzz1zzzzzz
?????||?|||||||||||iiii^```  `-.,,,.--..--``.-`...`.!1EMmk!t=!;*|zykEAKORNNym?!,``,l111t11t11111111z1zzzzzzzzz
???????|||||||||||iiiii=-``` `-.,,,..........-`-.-`,!160d2!;?!;*iI4UpKOR8&&yO+,.``./111z1111tt111111zzzzzzzzzz
?????|||||||||||||iiiii|,``` `.,,,,.........-``-.--,;JUW0at[Cc?=/sShEHR80NNjR|,.``.|zz111t11111111t1z11zzzzzzz
?????|?|||||||||||iiiiii!`````.,.~,,.......--`---`.,!thON8jvEju[jehhq8N080KGMT,-`..|1111t1tt11111111111zzzzz1z
????|?||||||||||||||iiii+.````.,,,,,......------.`.,:1EHWNdt46kmkAqKdNN000{0Rs,-.:~Tzz1t111t111t111zz1z111zzzz
?????|?|||||||||||||iiii|~````.,,,,,,,.....---..--.,:lAd%NNSc9K6U6K6UM888yKNRy..:r!xz111111tt11111111zz1zzz11z
?????|||||||||||||iii|iii!````.,,.,,,,,.........-..,:chdOM&RJiAKUUUhEOMOn9NNMS.~x=|x11t1111t11111tzz11z1zzzzzz
??????||||||||||||i|iiiii=-```.,,,.,,,,........`...,:/mKd%gNU1|zekXSEmnjg&&&Mo:?ezyz1t1t1t1t11t1111111z11zzzzz
?????||||||||||||i|iiiiii|..``-,,,,...,......--....,:|a9dOR00d3Ii|cxJm%0NN&NR4yvjEm11111ttttttttt111111z1zzzzz
?????||||||||||||iiiiiiiii,.```,,,,,,..------......,:|SKdHdMWDKpqUKdH%MgN&&NRKO1yMKt11ttttt1ttttt111111zzzzzzz
????|?|||||||||||iiiiiiii|,.`--,,,,,,,,,,..........,!ijObODHOdqKKKddRMN&#&#NRdWxZ0DJ1tttttttttt1tttt111111zzzz
??????||||||||||i|iiiiiii|,.`..,,,,,,,,,,.........,,;(jOHDROKAEA9KdOMN##&N&NROdjdNOttttttttttttttttt1111z1z1zz
?????||||||||||||iiiiiiii|,.`.,,,,,,,,,,,,.........,^x[UAJ6DKEkkAdORgN##&NN0RRpqNMHttttttttttttttttt11t11z1zzz
??|??||||||||||||iiiiiiiLi,,.-.,,,,,,,,,,,,....-..``:cjm!`LdphEEEdORgN##&&&0RO08#9UJttttJttttJtttttt1111111zzz
??|??|||||||||||iiiiiiiiii:.,..,,,,,,,,,,,,.......` `+zmY:|$6XKdqKDR8N&&&NNWRR#B#gSttttttttttttttttt111t111zzz
??||||||||||||||iiiiiiiiLi^,,,,,,,,,,,,,,,,.....--``-~c5YzZEeEd%ObORM0N&NNNMR8B#&%sJttttttJJJtJJtttttttttt1zzz
|????|||||||||iiiiiiiiiiiL|,,,,,,,,,,,,,,........``.,!r^!*zI5AORMRDRW0NNNN0gDM##MyttttttJtttttJtttttttttt111zz
?|?|?||||||||i||iiiiiiiiL/ir,,,,,,,,,,,,,.......-``.,,,.~^?izS9OMMRMg0NN0NNg%hhkntttttJtJJtJJttttttttt111tt1zz
????||||||||||iiiiiiiiiiL/LL!,,,,,,,,,,,,......-```..,.-,!^^?YjXKDW880NN0NN0RyJtJJttttttJtJJJJJJtttttttttt1111
?|?||||||||||||iiiiiiiiiL////?!:,,,,,,,,,....-`````-.,.`,!r^?|cI2kKR80NNN&Ng%jJJttJtJtttJJJJJtJJJttttttttt1111
|??||||||||||||iiiiiiiiiLLL/)/i=:,,,,,,,...-```````.,~.,!||rr+llz[hqWN&NNN0gRnttJttJJtttJJJJJJttJJttt1tttt1111
|?|||||||||||iiiiiiiiiiLLL////)L|,,,,,,,..-``````-.._!rizCjJvi7i|/t5dgN&&N0WOstttJJJJJtJJJJJJJtJJJJtttttt11111
||||||||||||iiiiiiiiLiiiLL///)))/:,,,,,,.-`````-.....,r|/zC[njyyz|?IkWNN0NgWKJttJtJJtttJJJJJJJJJJJJttttt1111t1
?||?|||||||||iiiiiiiiiLi/L/)/))/)^,,,,,,.-```-.---....^=?1jjICuF+r?JKMNN008MEJJtJJJJJtJJJJJJJJJJttJJtttttt1111
|||||||||||||iiiiiiiiiL/i////)))(|,,,,,,,.--`````--..,:!^?1jjCj[1!=SOWN000M%5JtJJJJtJJJJJJJJJJJJJJJttttttt1111
|||||||||||iiiiiiiiiiL/L/L(/))()cc:,,,,,,..--.----.,:r?=?TjkmwmK%k/kdM000gRdstJtJJJttJJJJJtJJJJJJJJJttttttt111
||||||||||||iiiiiiiiiLi/L/)/)(cvcvr,,,,,,,.......-.,!r==)zym5mKORbkAd%WggMOmJJJtJtJtJtJJJJJJJtJJtJttttttttt111
||||||||||||iiiiiiiiiLLLL//)(ccvvvi,,,,,,,..........,!r+?lJ3m$KODDKKdDRMRDKIJJttJJJJJJJJJJJJJJJttJtJttttttt111
?|||||||||||iiiiiiiiiLL//)))))cccvv;,,,,,,,......--.,,_:;=Ltnkd%DDHddHDRHdKYJJttJJYJJJJJYJJJJJJJJJJttJtttt1111
?|||||||||||iiiiiiiiLiL///)(()cc(vc?,,,,,,.......-``--..,_^iSEHDOR%OHHDRdKdstJJJJJJJJJJJJJtJJJJJJJJtJttttt1t1t
||||||||||||iiiiiiiiLLL///)))cvc)vvi,,,,,,,..,,,...-```.,!|VUKODDRRDObDOqHHsJtJJJJJJJJJJJYJJJJJJJJJJtJttttt1t1
||||||||||||iiiiiiiLLL///)/cccccccv/,,,,,,,...,.......,~^l5UKdOD%RMR%OOKdR%CJJJJJJJJJJJJJJJJJJJJJJtJJtttt1tt1t
||||||||||i|iiiiiiiiLL///)))ccccvvvv:,,,,,,..,,.....,:;=|ImddDO%MMMRDOdKRM%CJtJtJJJJJJJJJJJttJJJJJttJJtttt1t11
||||||||||iiiiiiiiiiLL///)()vccccvvv!,,,,,,,,,,,....,:+*vje4AdMM8WDDOKUDMWRnJttJtJJJYJJYJYYJYJJJJJJJJJJtt1tt1t
||||||||||||iiiiiiiLLi////)ccvvcvvvv!,,,,,,,,,,,....,:!r?v[yZEbO%dddq6dMggM[tttJJJYYJJYYYJJYYYJJJJJJJJttttttt1
|||||||||i|iiiiiiiii///////))ccvvvvT^,,,,,,......--.,,~!^|tJjmEUAE6AEK%M00MjtJJJJJJJYJJsJJJJYJJJJJJJtJtttttttt
|||||||||i|iiiiiiiiiL//L)()cc(ccvvvvr,,,,,,,..---``.,.,~:^??cjmyjymh$HWgN0MjtJYJJJYJJJYYsJJJYJtJJJJJJtJJtJtt11
|||||||||i|iiiiiiLL/L/)//)((c)vvvvvv+,,,,,,,..--````-,,,_:r??cJl?i56dDM0N0RytJYYYYJJJJYssJYYJYJJJJJJJJtJJttttt
||||||||||i|iiiiiiLLL////))vvccvcvv7=,,,,,,,,..---```....:!!r=+^=jEKHRg0NgM2JJJJYJJYJJJJYYJsJJJJJJJYJJJJtttttt
||||||||||iiiiiiiiiii////((((vvvvvT7?,,,,,,,,,,..-``---.-,!_::!?jh9d%WgNN0M5YJJYJJJJJYJJYJJJJtJJJtJJJJJJtJt1tt
|||||||||||iiiiiiiLLLL//)))()vcvv77T|,,,,,,,,,,,...-.....,,:;*LjP6KOMgg000MZYYsYJJYJJJJJYYYYJJJJJJJJJtttJJt11t
|||||||||iiiiiiiLiLiL)))()c)ccvT777T|,,,,,,,,,,,,,,,.,,,,:!+l[5kAqHRMg0000MmJJsYYYJJJYJJYYYJJJJJJJYJJtJJtttttt
|||||||||i|iiiiiLiLLLL))(cv(ccv777vvi,,,,,,,,,,,,,,,,~~:!r|lsjmAKHRMW800008AYsYsYYYJJYJJJJJJYJJJJJJJJJJJtttttt
|||||||||iiiiiiiiiLLL///))c)ccvT77Tli,,,,,,,,,,,,,,,,,:!^=iYykUKORMR8g0WWgMdYYJJYYJYsJJJJJJJJJJJJJYJJJJttttttt
|||||||||iiiiiiiiLL/////)c(cccv7T77li,,,,,,,,,,,,,,,,~:!+|tjm6d%RMMMg00gN08DIYYYsYYYJJJsJJJJJJJJYYYJJJtJJttttt
|||||||||iiiiiiiLiiL//))(cccvvcv7cT7i,,,,,,,,.,,,,,,~:^|z{ZhqOMMMWgWg00NN0gR[sYJsssYJYYYYJJJJJJYJYYYJJtJtttttt
|||||||||iiiiiiiiLL////))ccvvvv7vvTTi,,,,,,,,,,,,,,,:^|1jeAKOR8ggg8RMgg0NNN84ssssYYYYYsYJJJYJJJJJYYYJtJJJttttt
|||||||||iiiiiiiiiiLLL/))ccccvvvvvvT|,,,,,,,,,,,,,,_!=x{ZEKORMW0gg8MMMg0N&N0KyzT1JYsYJJYJJYJYJJJJJJtJJtJttttJt
||||||||||iiiiiiiiL/////)()vc7cc7vi+!,,,,,,,,,,,,,,:^|1ym6bDMgg0008RMWg0NNNNOASr!|zYYJYJJJJJYYJtJJJJJJJJJtttJt
|||||||||iiiiiiiiiLL/////)/cccvi*~```,,,,,,,,,,,,,,:+iJ2kqOM0g0g0gWRRWg00&&0RKUht~:vttJYJJJJJJJJJJJJJtJJJttttt
||||||||iiiiiiiiiiL/////))()c?:.`  `.,,,,,,,,,,,,,,!*iYShKDM8g000MRRRM80N&&&WdKUAS,|zxx1JJJJJtJJJJJYJJtttttttt
|||||||||iiiiiiLiLLLLL/)/)/|:---` `.,,,,,,,,,,,,,,,:+it3kK%RRM8gMRRDRMMgN&&NWOdKq6r|11l|;L1JJJJJtJJJYJJttttttt
|||||||||i|iiiiiiiLLL///Li!-``````-.,,,,,,,,,,,,,,,~r|xjhdOORRRRR%DO%R8800NNgDOdK$?|1tzL:|7x1tttJJJJJJttttttt1
||||||||||iiiiiiiiiiL///|,````````..,,,,,,,,,,,,,,,,:?)[6HHHDDRDDOODRRggggNN0ROdd$+/z1zcrilllxtJJJJJJJtttttttt
||||||||||||iiiiiiiiLLLr.`````````-.,,,,,,,,,,,,,,,,,;|C6dddHOD%OHOODMM8800N0ROHd5?xz1t(*vz1zxlzttJtJtttttt1Jt
||||||||||||iiiiiiiii|:-``````````-..,,,,,,,,,,,,,,,,:=JqdKdHDRDOddHORMgWWg00MObdc/zz1t?|zz1zxxlTzttJttttt1tt1
|||||||||||||iiiiiiir.`````````````..,,,,,,,,,,,,,,,,~rzEpKdO%DOdddHDH%MMMMgMRHOS|lxzz1=T1ttzzxTvTx1tttttttttt
|||||||||||i|iiiii=~-``````````````-.,,,,,,,,,,,,,,,,,!iSE$dODDOdKddHKO%RMMMMROkivTxlxv?xtt11zzzxxlTlz1ttt1ttt
|||||||||||||||i|:-`````````````````..,,,,,,,,,,,,,,,,:|jkAKdOOHdKKKdHODRRRRRRh|)lllcl=Ttttt11zxxllllTl1111t11
|||||||||||||||!.-```````````````````..,,,,,,,,,,,,,,,!|{eE9KHHdKKKKdddHOOOD%h|/vTvlTi?lYJt11zxxllxzxllv7xz111
?||||||||||||+,-``````````````````````-..,,,,,,,,,,,,_!|CVGUdddKKKpKKKKdHOOH5|iiv)vlT=?!Jtt1zxxxxxlllTlll7vlzz
??|||||||||?:--````````````````````````-..,,,,,,,,,,,:^|s5X6KKKKKKpKpqqKKdU1|||iL/v7?i:,lt1zxxxxxllxllllll7cvl
??|||||||?!.```````````````````````````---...,,,,,,,,:^|tymE6UUU$9$UU6666y|?||||iiL|i!,_+1xlxzzxllxlxllllTlTvc
"""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True