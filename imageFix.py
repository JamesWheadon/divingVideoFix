from PIL import Image
import matplotlib.pyplot as plt
im = Image.open('TurtleImage.jpg')
width, height = im.size
origPixelMap = im.load()
red = []
green = []
blue = []
for x in range(width):
    for y in range(height):
        pixelColour = origPixelMap[x, y]
        red.append(pixelColour[0])
        green.append(pixelColour[1])
        blue.append(pixelColour[2])
plt.plot(red)
plt.show()
plt.plot(green)
plt.show()
plt.plot(blue)
plt.show()