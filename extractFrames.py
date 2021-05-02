import cv2
import os

def extractFrames(video):
    cap = cv2.VideoCapture(video)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite('./turtleFrames/turtleFrame'+str(i)+'.jpg',frame)
        i+=1
    cap.release()
    cv2.destroyAllWindows()

def writeFrames(frameFolder, videoName):
    frames = sorted(os.listdir(frameFolder), key=len)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(videoName, fourcc, 48, (2704, 1520))
 
    for frame in frames:
        im = cv2.imread(frameFolder + frame)
        out.write(im)
    out.release()