import qrcode
from PIL import Image
import os

data = input("Enter text to generate QR: ")

# Create the QR code
qr = qrcode.QRCode(version=2, box_size=10, border=3)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")

# Get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Save the QR code in the same directory as the script
file_path = os.path.join(script_dir, "qr_code.png")
image.save(file_path)

# Open and display the QR code
img = Image.open(file_path)
img.show()
