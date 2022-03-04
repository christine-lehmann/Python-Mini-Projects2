import qrcode
import image

qr = qrcode.QRCode(
    version = 15, # 15 means the version of the qr code is high (bigger number = complicated picture)
    box_size= 10, # size of the box where qr code will be displayed
    border = 5    # it is the white part of image -- border in all 4 sides with white color
)

data = "https://github.com/christine-lehmann"
        # as I give a pathway to my github profile you can change it 
        # if you don't want to redirect in any link you can still write a text inside the quote

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")