from pyqrcode import *
from png import *
url = pyqrcode.create('https://www.instagram.com/lnleric/', error='L', version=4)
url.svg('ig-url.svg', scale=5)
url.png('ig-url.png', scale=5, module_color=(127,17,244), background=(255,255,255))
