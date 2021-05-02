import cv2
from PIL import Image
import os

def extractFrames(video, folder, fileNameTemplate):
    cap = cv2.VideoCapture(video)
    i=0
    framesMissing = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(folder + fileNameTemplate + str(i) + '.jpg', frame)
            i += 1
        else:
            framesMissing += 1
            if framesMissing > 10:
                break
    cap.release()
    cv2.destroyAllWindows()

def writeFrames(frameFolder, videoName, frameRate):
    frames = sorted(os.listdir(frameFolder), key=len)
    im = Image.open(frames[0])
    width, height = im.size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(videoName, fourcc, frameRate, (width, height))
 
    for frame in frames:
        im = cv2.imread(frameFolder + frame)
        out.write(im)
    out.release()