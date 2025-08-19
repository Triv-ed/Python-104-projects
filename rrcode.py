import qrcode 
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=12,
                 border=4
                 )
data=input("Please Enter Data")
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="brown", back_color="white")  
name=input("Enter the name ")
img.save(f"{name}.png")
