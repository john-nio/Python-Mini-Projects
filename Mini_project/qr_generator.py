import sys
import qrcode

data = input("Enter the text or URL: ").strip()
if not data:
    print("Error: No data provided. Exiting.")
    sys.exit(1)

filename = input("Enter the filename: ").strip()
if not filename.lower().endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")
