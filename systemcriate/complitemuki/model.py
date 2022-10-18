from keras.layers import Flatten,Input,Dropout
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import ReduceLROnPlateau
import util
import pickle

class model:
    def __init__(self,inputfolder,outfolder,estimatefile,infofile,graphfile,historyfile,classfile,
                inputsize,channel,filternumbers,filtersize,pool,denseunits,
                lr,min_lr,keep_lr,batch,reuse,epochs):
        self.inputfolder=inputfolder
        self.outfolder=outfolder
        self.estimatefile=estimatefile
        self.infofile=infofile
        self.graphfile=graphfile
        self.historyfile=historyfile
        self.classfile=classfile

        self.inputsize=inputsize
        self.channel=channel
        self.filternumbers=filternumbers
        self.filtersize=filtersize
        self.pool=pool
        self.denseunits=denseunits
        
        self.lr=lr
        self.min_lr=min_lr
        self.keep_lr=keep_lr
        self.batch=batch
        self.reuse=reuse
        self.epochs=epochs
    
    def define(self):
        input_x =Input(shape=(*self.inputsize,self.channel))
        x=input_x
        
        for f in self.filternumbers:
            x=util.add_conv_pool(x,f,self.filtersize,self.pool)
        
        x=Flatten()(x)
        x=Dropout(0.4)(x)

        for u in self.denseunits[:-1]: 
            x=util.add_dense(x,u)
        
        x=util.add_dense(x,self.denseunits[-1])
        
        model=Model(input_x,x)
        
        model.compile(optimizer=Adam(lr=self.lr),loss='mse',metrics=['mae'])
        
        return model
    
    def fit(self):
        train_ds,train_n,valid_ds,valid_n,classinfo=util.makegenerater(self.inputfolder,self.inputsize,self.batch)

        model=self.define()

        reduce_lr=ReduceLROnPlateau(patience=self.keep_lr,min_lr=self.min_lr,verbose=0)
        callbacks=[reduce_lr,]

        history=model.fit(train_ds,steps_per_epoch=int(train_n*self.reuse/self.batch),epochs=self.epochs,callbacks=callbacks,
                         validation_data=valid_ds,validation_steps=int(valid_n*self.reuse/self.batch))
        
        return model,history.history,classinfo
    
    def control(self):
        model,history,classinfo=self.fit()
        
        util.makefolder(self.outfolder,rm=True)
        model.save(self.estimatefile)
        
        util.modelinfo(self.infofile,model,self.batch,self.reuse,self.epochs)
        
        util.graph(history,self.historyfile)

        with open(self.classfile,'wb') as f:
            pickle.dump(classinfo,f)