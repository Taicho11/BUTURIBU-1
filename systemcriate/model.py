class model:
    def __init__(self,outfolder,estimatefolder,infofile,historyfile,channel,inputsize,filternumber.filtersize,pool,denseunit,lr,imagesize,batch,epochs,validrate):
        self.outfolder=outfolder
        self.estimatefolder=estimatefolder
        self.infofile=infofile
        self.inputsize=inputsize
        self.filternumber=filternumber
        self.filtersize=filtersize
        self.pool=pool
        self.denseunit=denseunit
        self.lr=lr
        self.imagesize=imagesize
        self.batch=batch
        self.epochs=epochs
        self.validrate=validrate
    
    def define(self):
        input_x =Input(shape=self.*inputsize,channel)
        x=input_x
        
        for f in self.filters:
            x=util1st.add_conv_pool(x,f,self.filtersize,self.pool)
        
        x=Flatten()(x)
        
        for u in self.denseunits[:-1]: 
            x=util.add_dense(x,u)
        
        x=util.add_dense(x,self.denseunits[-1],kasseika='softmax')
        
        model=Model(input_x,x)
        
        model.compile(optimizer=Adam(lr=self.lr),loss='categorical_crossentropy',metrics=['accuracy'])
        
        return model
    
    def fit(self):
        train_images,train_teachers=util.load_data(self.datasize)
        
        model=self.define()
        
        huistory=model.fit(train_images,train_teachers,batchsize=self.batsh,epochs=self.epochs,validationsplit=self.validrate)
        
        return model,history
    
    def control(self):
        model,history=self.fit()
        
        util.malefolder(self.outputfolder,re=True)
        model.save(self.estimatefolder)
        
        util.modelinfo(self.infofile,model)
        
        if 'acc' in history:
            history['accuracy'] = history.pop('acc')
            history['val.accuracy'] = history.pop('vfal_acc')
        util.graph(history,self.historyfile)