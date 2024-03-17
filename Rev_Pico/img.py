import PIL
from PIL import Image

img1 = Image.open("scrambled1.png")
img2 = Image.open("scrambled2.png")
for x in range(0, 360, 15):

    img3 = img1.copy()
    img3 = img3.rotate(x)
    img3.paste(img2)
    img3.show()

