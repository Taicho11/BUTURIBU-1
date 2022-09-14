import os
import shutil
import cv2
from collections import OrderedDict
import glob

def makefolder(foldernumber=31,parentfolder='/home/pi/Desktop/fixedimages'):
    shutil.rmtree(parentfolder,ignore_errors=True)
    os.makedirs(parentfolder)
    for i in range(foldernumber):
        shutil.rmtree(parentfolder+'/*',ignore_errors=True)
        foldername=os.path.join(parentfolder,f'{i*12}')
        os.makedirs(foldername)

def imread(folderpath='/home/pi/Desktop/画像編集/TeacherPictures'):
    imagepath=os.path.join(folderpath,'*','*')
    imagepaths=glob.glob(imagepath)
    imagepaths.sort()
    
    dictio=OrderedDict()

    angle=0
    for i in imagepaths:
        angle+=1
        trueangle=angle*12
        dictio[str(trueangle)]=cv2.imread(i)

def experi(inputpath='/home/pi/Desktop/画像編集/TeacherPictures/8.taichou/2022年08月23日13時54分14秒.jpg',ystart,yend,xstart,xend,outputpath='/home/pi/Desktop/画像編集/fixedimages/0/fixed5.jpg'):
    image = cv2.imread(inputpath)
    fixedimage=image[ystart:yend,xstart:xend,:]
    fixedimage=cv2.rotate(fixedimage,cv2.ROTATE_180)
    cv2.imwrite(outputpath,fixedimage)
