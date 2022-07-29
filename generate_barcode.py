import barcode  # python-barcode module
import png  # pypng module
from barcode import ISBN13
from barcode.writer import ImageWriter


# data for barcode provider
# code = barcode.get_barcode_class('code128')
code = barcode.get_barcode_class('ean13')

# data before barcode
# data = 'youtube.com'
data = '1001234567890'

# Generate Barcode
bar = code(data, writer=ImageWriter(format='PNG'))

# save in svg named 'mybarcode.svg'
bar.save('mybarcode1')

# save in png named 'myqrcode.png'
# bar.png('mybarcode.png', scale=6)

# Generate Barcode and save in png named 'isbnbarcode.svg'
# with open('isbnbarcode.png', 'wb') as f:
#     ISBN13('978123456789', writer=ImageWriter).write(f)
