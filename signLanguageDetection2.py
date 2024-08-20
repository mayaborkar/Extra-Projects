import os

WORKSPACE_PATH = '/Users/mayaborkar/Desktop/Tensorflow/workspace'
SCRIPTS_PATH = WORKSPACE_PATH + '/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

labels = [{'name':'Hello', 'id':1}, 
          {'name':'Yes', 'id':2},
          {'name':'No', 'id':3},
          {'name':'Thank You', 'id':4},
          {'name':'I Love You', 'id':5}]


with open((ANNOTATION_PATH + '\label_map.pbtxt'), 'a') as f:
    for label in labels:
        
        f.write("item { \n")
        f.write("\tname:\'{}\'\n".format(label['name']))
        f.write("\tid:{}\n".format(label['id']))
        f.write('}\n')

