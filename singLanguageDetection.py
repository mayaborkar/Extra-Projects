import os
import time
import uuid
import cv2

IMAGES_PATH = '/Users/mayaborkar/Desktop/CollectedImages/'

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    os.mkdir('/Users/mayaborkar/Desktop/CollectedImages/' + label) 
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs): 
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()