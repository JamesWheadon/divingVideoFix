from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
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
uniqueRed, countsRed = np.unique(red, return_counts=True)
uniqueGreen, countsGreen = np.unique(green, return_counts=True)
uniqueBlue, countsBlue = np.unique(blue, return_counts=True)
plt.plot(uniqueRed, countsRed, color='red')
plt.plot(uniqueGreen, countsGreen, color='green')
plt.plot(uniqueBlue, countsBlue, color='blue')
plt.show()