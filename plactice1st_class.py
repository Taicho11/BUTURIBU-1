import sys,os
sys.path.append(os.pardir)
from collections import OrderedDict
from common.layers import *
class plactice1st:
    def __init__(self,weights):
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution(weights['W1'], weights['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Pool1'] = Pooling(pool_h=2, pool_w=2, stride=2)
        self.layers['Affine1'] = Affine(weights['W2'], weights['b2'])
        self.layers['Relu2'] = Relu()
        self.layers['Affine2'] = Affine(weights['W3'], weights['b3'])
    
    def predict(self,x):
        for layer in self.layers.values():
            x = layer.forward(x)
        return x