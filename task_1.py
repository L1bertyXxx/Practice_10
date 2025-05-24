from PIL import Image

img = Image.open("otk.jpg")
width, height = img.size
cropped = img.crop((20, height - 100, width - 10, height))
cropped.save("otk_new.jpg")