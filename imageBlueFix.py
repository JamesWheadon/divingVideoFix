from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

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
"""uniqueRed, countsRed = np.unique(red, return_counts=True)
uniqueGreen, countsGreen = np.unique(green, return_counts=True)
uniqueBlue, countsBlue = np.unique(blue, return_counts=True)"""
redMean = np.mean(red)
redSTD = np.std(red)
greenMean = np.mean(green)
blueSTD = np.std(blue)
blueMean = np.mean(blue)
greenSTD = np.std(green)
print(redMean, redSTD)
print(greenMean, greenSTD)
print(blueMean, blueSTD)
mu, sigma = 127, 30
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)
"""plt.plot(uniqueRed, countsRed / pixels, color='red')
plt.plot(uniqueGreen, countsGreen / pixels, color='green')
plt.plot(uniqueBlue, countsBlue / pixels, color='blue')
plt.plot(x, y, color='black')
plt.show()"""
"""redTransformed = []
for r in red:
    diff = ((r - redMean) / redSTD)
    newValue = round(mu + diff*sigma)
    if newValue < 0:
        newValue = 0
    if newValue > 255:
        newValue = 255
    redTransformed.append(newValue)
uniqueRedTransformed, countsRedTransformed = np.unique(redTransformed, return_counts=True)"""
greenTransformed = []
for g in green:
    diff = ((g - greenMean) / greenSTD)
    newValue = round(mu + diff*sigma)
    if newValue < 0:
        newValue = 0
    if newValue > 255:
        newValue = 255
    greenTransformed.append(newValue)
uniqueGreenTransformed, countsGreenTransformed = np.unique(greenTransformed, return_counts=True)
blueTransformed = []
for b in blue:
    diff = ((b - blueMean) / blueSTD)
    newValue = round(mu + diff*sigma)
    if newValue < 0:
        newValue = 0
    if newValue > 255:
        newValue = 255
    blueTransformed.append(newValue)
uniqueBlueTransformed, countsBlueTransformed = np.unique(blueTransformed, return_counts=True)
"""plt.plot(uniqueRedTransformed, countsRedTransformed, color='red')
plt.plot(uniqueGreenTransformed, countsGreenTransformed, color='green')
plt.plot(uniqueBlueTransformed, countsBlueTransformed, color='blue')
plt.plot(x, y, color='black')
plt.show()"""

for x in range(width):
    for y in range(height):
        origPixelMap[x, y] = (red[x * height + y], greenTransformed[x * height + y], blueTransformed[x * height + y])
im.save('transformedTurtle.jpg')