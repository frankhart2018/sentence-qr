# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
import time


def qrify(s):
    # Generate QR code 
    url = pyqrcode.create(s) 

    # Generate filename using current timestamp
    filename = f"static/images/{time.time()}.png"

    # Create and save the png file naming "myqr.png" 
    url.png(filename, scale = 6) 

    return filename