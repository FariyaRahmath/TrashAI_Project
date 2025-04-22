# camera.py

import cv2
import PIL.Image
from PIL import Image
import time

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
        self.tt=0
        
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        cv2.imwrite("getimg.jpg", image)
        '''i=0
        while i<=5:
            print(i)
            i+=1
            time.sleep(2)'''
            
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Read the frame
        #_, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw the rectangle around each face
        j = 1
        
        for (x, y, w, h) in faces:
            mm=cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #cv2.imwrite("obj.jpg", mm)
            #image = cv2.imread("obj.jpg")
            #cropped = image[y:y+h, x:x+w]
            #gg="f"+str(j)+".jpg"
            #cv2.imwrite("upload/"+gg, cropped)
            #mm2 = PIL.Image.open('upload/'+gg)
            #rz = mm2.resize((100,100), PIL.Image.ANTIALIAS)
            #rz.save('upload/'+gg)
            j += 1

        '''self.tt+=1
        
        if self.tt==20:
            print(self.tt)
            self.tt=0'''

            


            
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
