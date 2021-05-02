from PIL import Image
import numpy as np

def blueGreenFix(fileName, saveFileName, greenData, blueData):
    
    im = Image.open(fileName)
    width, height = im.size
    origPixelMap = im.load()
    greenMean = greenData[0]
    greenSTD = greenData[1]
    blueMean = blueData[0]
    blueSTD = blueData[1]
    mu, sigma = 127, 30

    for x in range(width):
        for y in range(height):
            pixelColour = origPixelMap[x, y]
            green = pixelColour[1]
            greenDiff = ((green - greenMean) / greenSTD)
            newGreenValue = round(mu + greenDiff*sigma)
            if newGreenValue < 0:
                newGreenValue = 0
            if newGreenValue > 255:
                newGreenValue = 255
            blue = pixelColour[2]
            blueDiff = ((blue - blueMean) / blueSTD)
            newBlueValue = round(mu + blueDiff*sigma)
            if newBlueValue < 0:
                newBlueValue = 0
            if newBlueValue > 255:
                newBlueValue = 255
            origPixelMap[x, y] = (pixelColour[0], newGreenValue, newBlueValue)

    im.save(saveFileName)

def numpyFix(fileName, saveFileName, greenData, blueData):
    
    im = Image.open(fileName)
    width, height = im.size
    origPixelMap = im.load()
    greenMean = greenData[0]
    greenSTD = greenData[1]
    blueMean = blueData[0]
    blueSTD = blueData[1]
    mu, sigma = 127, 30
    
    pixels = np.array(im)
    pixels_green = (mu + sigma*((pixels - greenMean) / greenSTD))
    pixels_fix = np.clip((pixels_green).astype(int), 0, 255)
    npImage = Image.fromarray(np.uint8(pixels_fix))

    npImage.save(saveFileName)

"""im = Image.open('TurtleImage.jpg')
width, height = im.size
origPixelMap = im.load()
print(origPixelMap[0, 0])
green = []
blue = []

for x in range(width):
    for y in range(height):
        pixelColour = origPixelMap[x, y]
        green.append(pixelColour[1])
        blue.append(pixelColour[2])

greenData = (np.mean(green), np.std(green))
blueData = (np.mean(blue), np.std(blue))
greenMean = greenData[0]
greenSTD = greenData[1]
blueMean = blueData[0]
blueSTD = blueData[1]
mu, sigma = 127, 30
print(blueData, greenData)

pixels = np.array(im)
print(pixels.shape)

pixels_green = (mu + sigma*((pixels - greenMean) / greenSTD))
pixels_blue = (mu + sigma*((pixels - blueMean) / blueSTD))
pixels_fix = np.clip((pixels_green).astype(int), 0, 255)
print(pixels_fix)
npImage = Image.fromarray(np.uint8(pixels_fix)).show()"""