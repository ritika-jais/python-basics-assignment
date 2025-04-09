import qrcode

# Data to encode
data = "https://example.com"

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save it
img.save("my_qr.png")

print("QR code generated and saved as my_qr.png")
