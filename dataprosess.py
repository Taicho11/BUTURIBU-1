import cv2
import numpy as np
import glob
from collections import OrderedDict
import math
import random
def data_prosess(folder_number,picture_number):
    #写真をｘに変換する
    picture_paths = glob.glob('/home/pi/Desktop/新規/教材収集/*.taichou/*')
    picture_paths.sort()
    picture_array = np.array([cv2.imread(paths) for paths in picture_paths])
    x = picture_array.transpose(0,3,1,2)
    
    #fpicture_number枚の写真が入ったfolder_number個のフォルダ
    dictio= OrderedDict()
    
    for i in range(folder_number):
        dictio[f'{i}']=np.full((3,),i)
    t = np.array([dictio[f'{i}'] for i in range(folder_number)])
    t = np.ravel(t)
    
    index_list = list(range(picture_number))
    random.shuffle(index_list)
    x = x[index_list,:,:,:]
    t = t[index_list]
    
    x_train,x_test = np.split(x,[round(picture_number*0.8)])
    t_train,t_test = np.split(t,[round(picture_number*0.8)])
    return x_train,x_test,t_train,t_test

if __name__ == '__main__':
    '''
    x_train,x_test,t_train,t_test = data_prosess(10,30)
    
    print(t_test)
    print(x_test)
    '''
    
    
    t = np.array([0,0,1,0,0])
    y = np.array([0,0,0.9,0,0])
    e = -np.sum(t*np.log(y+1e-7))    
    print(e)
    
    #t:0~5
    t = np.array([3,4])
    y = np.array([[0,0,0.9,0.1,0],[0,0,0,0.9,0.1]])
    
    print(f'{t}\n{y}')
    e = -np.sum(np.log(y[np.arange(2),t]+1e-7))/2
    print(e)