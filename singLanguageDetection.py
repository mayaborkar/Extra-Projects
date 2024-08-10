import os
import time
import uuid
import cv2

IMAGES_PATH = 'Tensorflow/workspace/images/collectedImages'

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    