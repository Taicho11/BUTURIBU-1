import os,sys
import shutil
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Conv2D,Dense,MaxPooling2D
from tensorflow.data import Dataset
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import plot_model
import cv2
from keras.models import load_model
################################################################################################################################################################################################################################
def makefolder(folder_name,rm=False):
    if rm:
        shutil.rmtree(folder_name,ignore_errors=True)
        os.makedirs(folder_name)
    else:
        try:os.makedirs(folder_name)
        except FileExistsError:pass

def makegenerater(inputfolder,inputsize, batch):
    train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=90,
    zoom_range=[1.0,4.0],
    validation_split=0.2
    )
    train_generator = train_datagen.flow_from_directory(inputfolder,target_size=inputsize,batch_size=batch,shuffle=True,class_mode='categorical',subset='training')
    valid_generator = train_datagen.flow_from_directory(inputfolder,target_size=inputsize,batch_size=batch,shuffle=True,class_mode='categorical',subset='validation')

    train_ds = Dataset.from_generator(lambda: train_generator,output_types=(tf.float32, tf.float32),output_shapes=([None, *train_generator.image_shape],[None, train_generator.num_classes]))
    valid_ds = Dataset.from_generator(lambda: valid_generator,output_types=(tf.float32, tf.float32),output_shapes=([None, *valid_generator.image_shape],[None, valid_generator.num_classes]))

    train_ds = train_ds.repeat()
    valid_ds = valid_ds.repeat()

    classinfo={v:k for k,v in train_generator.class_indices.items()}
    return train_ds,train_generator.n,valid_ds,valid_generator.n,classinfo

def graph(history,graphfile):
    def graphplot(tatememori,yokomemori,index,xdata_ephocs,trainydata,validydata,ylim,ylabel):
        plt.subplot(tatememori,yokomemori,index)
        plt.plot(xdata_ephocs,trainydata,label='training',linestyle='--')
        plt.plot(xdata_ephocs,validydata,label='validation')
        plt.xlim(1,len(xdata_ephocs))
        plt.ylim(*ylim)
        plt.xlabel('ephocs')
        plt.ylabel(ylabel)
        plt.grid()
        plt.legend(ncol=2,bbox_to_anchor=(0,1),loc='lower left')
        
    plt.figure(figsize=(10,10))
    xdata_ephocs=range(1,1+len(history['loss']))

    graphplot(2,1,1,xdata_ephocs,history['loss'],history['val_loss'],(0,5),'loss')
    plt.savefig(graphfile)
    plt.close('all')

 ####################################################################################################################################################################################################################################   
def estimateimage(image_path,dsize=(50,50)):
    input_data=cv2.imread(image_path)
    input_data=cv2.resize(input_data,dsize=dsize)
    input_data=input_data.reshape(1,*dsize,3)
    input_data=input_data.astype('float32')/255

    return input_data

def tflite_from_keras(input_path,output_path):
    model= load_model(input_path)

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    open(output_path,'wb').write(tflite_model)
##############################################################################################################################################

def add_conv_pool(x,filternumber,filtersize,pool,kasseika='relu'):
    x=Conv2D(filternumber,filtersize,padding='same',use_bias=False,activation=kasseika)(x)
    #x=Conv2D(filternumber,filtersize,padding='same',use_bias=False,activation=kasseika)(x)
    x=MaxPooling2D((pool))(x)
    return x

def add_dense(x,denseunit,kasseika='relu'):
    x=Dense(denseunit,activation=kasseika)(x)
    return x


def modelinfo(infofile,model,batch,reuse,ephocs):
    with open(infofile,'w') as f:
        model.summary(print_fn=lambda x: f.write(x+'\n'))
        smallinfo=[f'batch={batch}',f'reuse={reuse}',f'ephocs={ephocs}']
        f.writelines(smallinfo)