import sys, os
sys.path.append(os.pardir)  
import numpy as np
import matplotlib.pyplot as plt
from ch07.simple_convnet import SimpleConvNet
import glob
from tqdm import tqdm
from 実験 import data_prosess
from collections import OrderedDict
import pickle

network = SimpleConvNet()
while True:   
    dt_now = datetime.datetime.now()
    file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(f'./pictures/{file_name}.jpg', frame)
    cap.release()


with open ('weights2022-06-04 08:14:37.187527.pickle','rb') as f:
    weights = pickle.load(f)
    print(weights)