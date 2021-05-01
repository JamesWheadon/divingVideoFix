from PIL import Image
import numpy as np

im = Image.open('TurtleImage.jpg')
width, height = im.size
pixels = width * height
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

greenMean = np.mean(green)
blueSTD = np.std(blue)
blueMean = np.mean(blue)
greenSTD = np.std(green)
mu, sigma = 127, 30
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)

greenTransformed = []
for g in green:
    diff = ((g - greenMean) / greenSTD)
    newValue = round(mu + diff*sigma)
    if newValue < 0:
        newValue = 0
    if newValue > 255:
        newValue = 255
    greenTransformed.append(newValue)

blueTransformed = []
for b in blue:
    diff = ((b - blueMean) / blueSTD)
    newValue = round(mu + diff*sigma)
    if newValue < 0:
        newValue = 0
    if newValue > 255:
        newValue = 255
    blueTransformed.append(newValue)

for x in range(width):
    for y in range(height):
        origPixelMap[x, y] = (red[x * height + y], greenTransformed[x * height + y], blueTransformed[x * height + y])
im.save('transformedTurtle.jpg')