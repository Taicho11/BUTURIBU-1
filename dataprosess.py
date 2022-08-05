import cv2
import numpy as np
import glob
from collections import OrderedDict
import math
import random
import pickle
import datetime

def data_prosess(picture_paths,folder_number,picture_number):                #写真のファイルパス、フォルダの個数、写真の枚数を引数にとる
    picture_array = np.array([cv2.imread(paths) for paths in picture_paths]) #指定したファイルパスの写真のRGBを読み込む
    
    x = picture_array.transpose(0,3,1,2)                                     #ゼロつくが提供している関数に１行前で読み込んだRGBをそのまま入れるとエラーになるので調整して、ｘに代入する
    
    dictio= OrderedDict()                                                    #一枚一枚の写真に正解ラベルを貼り付けて、ｔに代入する。oneーhotではなく、'1'の写真には'1'のラベルを貼る　例）フォルダが４つ、１つのフォルダに３枚の写真がある場合[0,0,0,1,1,1,2,2,3,3,3,4,4,4]
    for i in range(folder_number):                                           
         dictio[f'{i}']=np.full((3,),i)                       
    t = np.array([dictio[f'{i}'] for i in range(folder_number)])
    t = np.ravel(t)
        
    index_list = list(range(picture_number))                                 #xとtをそれぞれシャッフルする
    random.shuffle(index_list)                                               #numpy[index]って書くとindexの通りにnumpyの要素がシャッフルされるので、ランダムな数の配列を作ってx[index]t[index]ってやる
    x = x[index_list,:,:,:]
    t = t[index_list]
        
    x_train,x_test = np.split(x,[round(picture_number*0.8)])                 #xの８割を訓練データ、２割をテストデータにする
    t_train,t_test = np.split(t,[round(picture_number*0.8)])                 #$xの８割を訓練データ、２割をテストデータにする

    return x_train,x_test,t_train,t_test

    