import os
from PIL import Image
import numpy as np
from imageBlueFix import blueGreenFix, numpyFix
from extractFrames import extractFrames, writeFrames

def fixVideo(videoFile, fixedName=False):

    subject = videoFile.split('.')[0]
    originalFrames = './' + subject + 'frames/'
    fixedFrames = './fixed' + subject + 'frames/'

    os.mkdir(originalFrames)
    os.mkdir(fixedFrames)

    extractFrames(videoFile, originalFrames, subject)

    files = sorted(os.listdir(originalFrames), key=len)

    im = Image.open(originalFrames + files[0])
    width, height = im.size
    pixels = np.array(im)
    green = pixels[:, :, 1]
    blue = pixels[:, :, 2]

    greenData = (np.mean(green), np.std(green))
    blueData = (np.mean(blue), np.std(blue))

    for frame in files:
        numpyFix(originalFrames + frame, fixedFrames + frame, greenData, blueData)
        print(frame)
    
    if !fixedName:
        fixedName = 'fixed' + subject + '.MP4'

    writeFrames(fixedFrames, fixedName)