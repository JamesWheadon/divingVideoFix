import os
from PIL import Image
import numpy as np
from imageBlueFix import blueGreenFix, numpyFix
from extractFrames import extractFrames, writeFrames

files = sorted(os.listdir('./turtleFrames'), key=len)
files = files[100:1500]
print(files[0], files[-1])
print('hello')
frameFolder = './turtleFrames/'
fixedFrameFolder = './numpyTurtleFrames/'

im = Image.open(frameFolder + files[0])
width, height = im.size
origPixelMap = im.load()
green = []
blue = []

for x in range(width):
    for y in range(height):
        pixelColour = origPixelMap[x, y]
        green.append(pixelColour[1])
        blue.append(pixelColour[2])

greenData = (np.mean(green), np.std(green))
blueData = (np.mean(blue), np.std(blue))

for frame in files:
    numpyFix(frameFolder + frame, fixedFrameFolder + "numpy" + frame, greenData, blueData)
    print(frame)

writeFrames('./numpyTurtleFrames/', 'numpyTurtle.MP4')