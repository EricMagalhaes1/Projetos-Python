from pyqrcode import *
from png import *
url = pyqrcode.create('https://www.instagram.com/lnleric/', error='L', version=4)
url.svg('ig-url.svg', scale=5)

