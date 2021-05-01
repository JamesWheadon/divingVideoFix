from PIL import ImageEnhance, Image

im = Image.open('transformedTurtle.jpg')

enhancer = ImageEnhance.Contrast(im)
enhancer.enhance(1.5)

enhancer = ImageEnhance.Sharpness(im)
enhancer.enhance(2).show()
