import os
from model import model
import datetime

dt_now=datetime.datetime.now()

INPUTFOLDER='mainenv/program/ro-ba-/向き/Fixedimages'
OUTPUTFOLDER=f'{dt_now}'
ESTIMATEFILE = os.path.join(OUTPUTFOLDER, 'estimator.h5')
INFOFILE= os.path.join(OUTPUTFOLDER, 'model_info.txt')
GRAPHFILE= os.path.join(OUTPUTFOLDER, 'model_graph.pdf')
HISTORYFILE= os.path.join(OUTPUTFOLDER, 'history.pdf')
CLASSFILE =os.path.join(OUTPUTFOLDER,'class.pkl')

INPUTSIZE = (50,50)
CHANNEL=3
FILTERNUMBERS= (1,)
FILTERSIZE = (3,3)
POOL=(2,2)
DENSEUNITS =[4]

LR= 1e-3
MIN_LR=1e-7
KEEP_LR=5
BATCH= 16
REUSE=5
EPOCHS=5

DENSEUNITS.append(1)

MODEL= model(inputfolder= INPUTFOLDER,outfolder=OUTPUTFOLDER,estimatefile=ESTIMATEFILE,infofile=INFOFILE,graphfile=GRAPHFILE,historyfile=HISTORYFILE,classfile=CLASSFILE,
            inputsize=INPUTSIZE,channel=CHANNEL,filternumbers=FILTERNUMBERS,filtersize=FILTERSIZE,pool=POOL,denseunits=DENSEUNITS,
            lr=LR,min_lr=MIN_LR,keep_lr=KEEP_LR,batch=BATCH,reuse=REUSE,epochs=EPOCHS)

MODEL.control()