# to use virtual environments in vscode, add the file to python projects!
import qrcode

# list of common img subfixes
image_files = ('.png', '.jpg')

data = input('Enter the  text or URL: ').strip() # remove any whitespaces around the input
filename = input('Enter the filename: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='green', back_color='white')

if filename[-4:] not in image_files:
    filename = f'{filename}.png' # add .png to the filename

image.save(filename)

print(f'QR code saved as {filename}')