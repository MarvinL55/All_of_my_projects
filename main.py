import pyqrcode
from pyqrcode import QRCode

s = "https://www.instagram.com/they_envy_marvin/"

url = pyqrcode.create(s)

url.svg("myig.svg", scale=8)
