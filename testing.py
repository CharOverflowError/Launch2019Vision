from PIL import Image

img = Image.open("dick_butt_by_beyx.png")
img.save("./dick_butt_compressed.jpeg", "JPEG", quality=1)

print(img)