from ensurepip import version
import qrcode
import image
qr = qrcode.QRCode(version=10, box_size=10, border=3 )
data = input("\n Enter the data to create qr code : ")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("qr.png")
print("\n your QR CODE has been generated successfully \n in this folder with the name of qr.png \n")
