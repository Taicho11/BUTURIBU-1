import os
import shutil
import cv2
from collections import OrderedDict
import glob
class imageedit:
    def __init__(self,outputparentfoldr,inputparentfolder,anglestep):
        self.outputparentfolder=outputparentfoldr
        self.inputparentfolder=inputparentfolder
        self.anglestep=anglestep
        
    def makefolder(self,foldernumber=33):
        shutil.rmtree(self.outputparentfolder,ignore_errors=True)
        os.makedirs(self.outputparentfolder)
        for i in range(foldernumber):
            foldername=os.path.join(self.outputparentfolder,f'{i*self.anglestep}')
            os.makedirs(foldername)

    def imread(self):
        imagepath=os.path.join(self.inputparentfolder,'*','*')
        imagepaths=glob.glob(imagepath)
        imagepaths.sort()
        
        images={}

        for angle,i in enumerate(imagepaths):
            trueangle=angle*self.anglestep
            images[str(trueangle)]=cv2.imread(i)
        
        return images
    
    def edit(self,images):
        image=images[1]
        fixedimage=images[200:420,:,:]
        fixedimage=cv2.rotate(fixedimage,cv2.ROTATE_180)
        return fixedimage
    
    def imwrite(self):
        images=self.imread()
        for folder,image in images.items():
            fixedimage=self.edit(image)
            folder=str(folder)
            outputfolder=os.path.join(self.outputparentfolder,folder,'fixed.jpg')
            cv2.imwrite(outputfolder,fixedimage)
            
kurasu=imageedit(outputparentfoldr='/home/pi/Desktop/ImageEdit/fixedimages',inputparentfolder='/home/pi/Desktop/ImageEdit/TeacherPictures',anglestep=12)
kurasu.imwrite()
#kurasu.makefolder()