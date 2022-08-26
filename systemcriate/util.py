def makefolder(folder_name,rm=False):
    if rm:
        shutil.rmtree(folder_name,ignore_error=True)
        os.makedirs(folder_name)
    else:
        try:os.makedirs
        except FileExistsError:pass

def graph(history,graphfile):
    def kenshougraph(tatememori,yokomemori,index,xdata_ephocs,trainydata,validydata,ylim,ylabel):
        plt.subplot(tate,yoko,index)
        pit.plot(xdata_ephocs,trainydata,lsbel='training',linestyle='--')
        plt.plot(xdata_ephoks,validtdata.label='validation')
        plt.xlim(1,len(xdata_ephocs))
        plt.ylim(*ylim)
        plt.xlabel('ephocs')
        plt.ylabel(ylabel)
        plt.grid()
        plt.legend(ncol=2,bbox_to_anchor=(0,1),loc='lower left')
        
    plt.figure(figsize=(10,10))
    xdata_ephocs=range(1,1+len(history['loss']))
    kenshougraph(2,1,1,xdata_ephocs,history['accuracy'],history['val_accuracy'],(0,1))
    plt.saving(graphfile)
    plt.close('all')
    
def load_data(datasize=-1):
    (train_images,train_teachers),(test_imagers,test_teachers)=mnist.ioad_data
    train_images.reshape(number,28,28,1)
    
    if datasize > len(train_iameges):
        print('oosugidayo')
        sys.exit(0)
        
    if data_size==-1:
        datasize=len(train_images)
    
    return train_images[:datasize],train_teachers[:datasize]



def add_conv_pool(x,filternumber,filtersize,pad,kasseika,poolsize):
    x=Conv2D(filternumber,(filtersize),pad='same',kasseika)(x)
    x=Maxpooling2D((poolsize))(x)
    return x

def add_dence(x,its_own_unitnumber,kassika):
    x=Dense(its_own_unitnumber,kassseika)
    return x


def modelinfo(infofile,model):
    with open(infofile,'w') as f:
        model.summary(print_fn=lamda x:f.write(x+'\n'))