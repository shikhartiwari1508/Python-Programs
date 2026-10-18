import qrcode

url = "https://www.google.com"
qr = qrcode.make(url)
qr.save("my_qr.png")
print("✅ QR Code generated and saved as 'my_qr.png'!")