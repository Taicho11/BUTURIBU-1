import sys, os
sys.path.append(os.pardir)  
import numpy as np
import cv2
from plactice1st_class import plactice1st
import glob
from dataprosess import data_prosess
from collections import OrderedDict
import pickle
import datetime
import RPi.GPIO as GPIO

with open ('weights2022-06-04 08:14:37.187527.pickle','rb') as f: #openの第一引数に重みが記録されているファイルのパスを入力する
    weights = pickle.load(f) #変数'weights’に重みが代入される
    

    """
    分析したい写真を撮影する
    dt_now = datetime.datetime.now()
    file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    """
#     conv - relu - pool - affine - relu - affine - softmax
pic = '/home/pi/Desktop/deep-learning-from-scratch-master/教材収集/0.taichou/2022年06月13日18時39分27秒.jpg'
x = cv2.imread(pic)
x = x.reshape(1,480,640,3).transpose(0,3,1,2)#ただの写真をAIのためのデータに整形する

cla = plactice1st(weights)#使うAI（のクラス）を指定する
y = cla.predict(x)#ここで行われている処理はこのファイルの５行目でimportされているファイルを参照（それもgithub内にあります）
print(y)

