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
            newBlueValue = round(mu + greenDiff*sigma)
            if newBlueValue < 0:
                newBlueValue = 0
            if newBlueValue > 255:
                newBlueValue = 255
            origPixelMap[x, y] = [pixelColour[0], newGreenValue, newBlueValue]

    im.save(saveFileName)
