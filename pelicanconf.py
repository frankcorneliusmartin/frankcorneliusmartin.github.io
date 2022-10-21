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

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Theme

THEME =  Path('.') / 'pelican-atom'

DESCRIPTION = "hello world"

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

ASCII_PICTURE = \
"""
0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK00KKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKXXKKKXK0000KKKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKK0OOOOOOkOKKKOOKXKKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKK00Okxdolccccll::lxOkkKK0OkkO00KKXXKKXXXXXXXXXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKK00OOkdl:;,..........',,;;:lolclodxxxO0KKKXXKXXXXXXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXXXXXXXKKKKK00OOkdl:;'......................,,:ldkxdxO0KKXXKKKXKXXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXXKKKKKK000Oxdol;'..............................,:c:okxxk0KKKKKKKXXXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXXXXXK0000OOkdoc;,.....................................',:ooox00000KKKKXXXXXXXXXXXXXXXX
0XXXXXXXXXXXXXKKKKOkxolc:;'...........................................,;,cddxkkO00KXKKKXXXXXXXXXXXXX
0XXXXXXXXXXXXXKKKOxol:;;'................................................;olldxkOO0KKKKXXXXXXXXXXXXX
0XXXXXXXXXXKKKKK0Oxxkdl;'............................'''',,,,'''.........,:::ldOOO0KKXXXXXXXXXXXXXXX
0XKKXXXXXXKKK000kdxxl:,'......................'',::ccllloodddoolc;,........,;cddxk00KKKKXXXXXXXXXXXX
0XKKXXXKKKKKKK0kddoll;...................',;::cldxxkkOOOOO0OOOkxdol:,.......':cldxkkOKKKXXXXXXXXXXXX
0XKKKXXKKKKKKKOxdllo;..................';cloddxxkO0000KKKKK0000Okxxl:;'......;::oxxxxOKXXXXXXXXXXXXX
0KKKKKKKKKKKKKKklod:.................,;:oxkO00OOO00000KKKK0K000Okkxdol:,.......;dkOOkk0KXXXXXXXXXXXX
0KKKKKKKKKKKKK0kol;............',,;::lok0KKKKKKK00KKKKKKK0000000Okkxdol:'......;dxOK0kk0KKXXXXXXXXXX
OKKKKKKKKKKKKK0Oo:;...........;odxxkxk0KKXKKKKKK0OO0KKKKK0000000Okkxdolc,......':ldk0Ox0XKKKXXXXXXXX
OKKKKKKKKKKKKKKOo;'..........':dkkOO0KKKXXXXKKKKKKKKKK00KKK0000OOkkxddoc,......',cloO0k0XKKKXXXXXXXX
0KKKKKKKKKKKK0Okd:..........;cldkOOO0KKKXXXXKKK000KKKKKKKXKKKK0Okxxxddol;'.....';lxOO0O0KKKKXXXXXXXX
0KKKKKKKKKKKK00Oo,.........'cddxkOOO0KKKKXXXXXKKKKXXXXXXXXXKKK0Okkxxddooc'......,cdkO00KKKKKKKXXXXXX
OKKKKKKKKKKKKKKOl'.........:odxkkOOO0KKKKKKKKKKXKXXXKKKKK00Okkkxxxddooool,.......cdxOKKKKKKKKKXXXXXX
OKKKKKKKKKKKKK00x;........,ldddlc:ccllloooodxkOOO00OOkkxdoc:;,,,,,;;,,;cl;.......;dO0KKKKKKKKXXXXXXX
OKKKKKKKKKKKKK00Oc........,::c:,,;;,,''''''',:coxxxxxdoc;;,'..'',;;:;,,,;,........lO0KKKKKKKKKKKKXXX
OKKKKKKKKKKKKK00k:...........';;;;;;;;,''''...'',;:::;,'''..''',,,,;,,,;,.........;ok00KKKKKKKKKKXXX
OKKKKKKKKKKKKK00x;........'.':;,'.',,'..':;,,;:;...''..,:;'','...';,''';:;'........,oO0KKKKKKKKKKKKX
OKKKKKKKKKKKKK00x;........:,;ooc;,;cc;,;cooccldc'lkOkl';lc;:ll:;;:c:;;:cll,....'....,cxO000KKKKKKKKX
OKKKKKKKKKKKKKK0Oc.......'l:;dxdocclllllllllloo:l0KK0kc,clcccccccccccclodl,.,,.',',,'':dkO0KKKKKKKKK
OKKKKKKKKKKKKKKK0kl,.....,ll;okkxooddddoodxxxxccOK00Okd:;oxxxdddddddoodxdc,,;::'..'cdxk00KKKKKKKKKKK
OKKKKKKKKKKKKKKKK00xc;,'.'coollooodxkkkkkkxdo::xO0K00kxdc;coxxxxxxxxdoolcccc;:lc'.;dO0KKKKKKKKKKKKKX
OKKKKKKKKKKKKKKKKK0kol:;;;:odxxddooooooooolc;cdkO0000Oxddlc:ccllloooooooodolc;co::d0KKKKKKKKKKKKKKXX
OKKKKKKKKKKKKKKKKK0Oxdoclc:ldxxxkkkOOOOOOkkxxxxkO0KK0OkxdddxkkkkkkkkxxxddoollcldodOKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKOkdodl:codxxxkO00KKKK0OkxdoldOOOkxlccoodkOO000OkxxddooooooodxO0KKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKK0kxxdoooddxxkkO00KK00Okxl;;clllcc;,,cldxO000OOkxddoooodxddk0KKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKOkxolodddxxkkO00000OOkdoloolcclollloxkO00OOkxxdddoodxxkOKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKK00kloddxxxkkkO000OOkkxxdxxddddxdddxxkkOOOkxxdddddox0KKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKK0kdddxxxkkkkOOkxxxxxkkxkkkkkkxxxxddddxkxxdddddddOKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKKK0xoddxxxxxxxxdlllloooollloollllllcccodddddddddk0KKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKK0Odlooddxxxxxdolcc::clooolcllcc:;;;:cloooooddox0KKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKK00Odooooodddxxxxdollloxxxxxxxdolccldddoooooood0KKKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKK00xloollloooodxxxdolc::::;;::::clloddoolllllokKKKKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKK00koodolccllllodddddoollccccclllooooollllllodOKKKKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKKKKK00kddddlccccllodxxkkkkkxxxxxxxdxddoollclloddk0KKKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKKKKK00K0Odoxxddolccccoodxkxxxxxxxxdddxxxdolccclodddx0KKKKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKKKK000Odl:''lxxxddollc::cclooooooollllloolccccllooodl;;d0KKKKKKKKKKKKKKKKKKKKKKKKK
OKKKKKKKKKKKKKKKKKK000xl,.....cxxxxxdoolc:;;,,,,,,,,,,,,;;;;;:clloooool,..cOK0KKKKKKKKKKKKKKKKKKKKKK
OK0KKKKKKKKKKK000000xc........lxxxxxxddollc:;,''......'',;::clloooooooo,...cOK00000KKKKKKKKKKKKKKKKK
O000KKKKKKK0000000Oo'........,oxxxxxxxxddooolcc:;;,,,;;:clllloooooooooo;....l00000000000KKKKKKKKKKKK
O0000KKKK00000000kc..........:dxxxxxxxxxxddddddddooooooooooooooooooddoo:....'ck000000000KK0KKKKKKKKK
O000000000000Oxoc;'.........,odxxkkkkxxxxxxxxkkkkkkkkkxxdoooooooooodoooc'.....,:loxO00000000KKKKKKK0
k0000000000kl;..............cddxxkkkkkxxdddxxkOOOOOOOOkxdooooodddddooooc,..........;lx00000000000000
"""

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True