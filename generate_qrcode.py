import pyqrcode
import png  # pypng module
from pyqrcode import QRCode

# data in qrcode
data = 'www.python.org'

# Generate QRCode
qr = QRCode(data)

# save in png named 'myqrcode.png'
qr.png('myqrcode.png', scale=6)

