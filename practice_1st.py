import sys, os
sys.path.append(os.pardir)  
import numpy as np
import cv2
from plactice1st_class import plactice1st
import glob
from tqdm import tqdm
from dataprosess import data_prosess
from collections import OrderedDict
import pickle
import datetime

with open ('weights2022-06-04 08:14:37.187527.pickle','rb') as f:
    weights = pickle.load(f)
    

    """
    dt_now = datetime.datetime.now()
    file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
     x = data_prosess(0,1)
    """
#     conv - relu - pool - affine - relu - affine - softmax
pic = '/home/pi/Desktop/deep-learning-from-scratch-master/教材収集/0.taichou/2022年06月13日18時39分27秒.jpg'
x = cv2.imread(pic)
x = x.reshape(1,480,640,3).transpose(0,3,1,2)

cla = plactice1st(weights)
y = cla.predict(x)
c = np.max(y)
exp_y = np.exp(y-c)
sum_exp_y = np.sum(exp_y)
y = exp_y/sum_exp_y
print(y)
answer = np.argmax(y)
print(answer)
