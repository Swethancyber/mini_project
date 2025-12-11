import qrcode as qr

url = input("Enter the url hear : ")

img = qr.make(url)
img.save("img.png")
print("qrcode generated succfully ")