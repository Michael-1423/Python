# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:13:30 2021

@author: Asus
"""

import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        #print(weight_shapes)
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in weight_shapes]
        #print(self.weights)
        self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]
        #print(self.biases)

    def predict(self, a):
        for w,b in zip(self.weights,self.biases):
            print("previous" ,np.argmax(a))
            a = self.activation(np.matmul(w,a) + b)
            print("later" , np.argmax(a) , a )
            a1 = self.activation(np.matmul(w,a))


        return a1

    def print_accuracy(self, images,labels):
        l = []
        predictions = self.predict(images)
        l = [(np.argmax(a),np.argmax(b))  for a,b in zip(predictions , labels)]
        with open(r"E:\newd\nn\da" , 'w+' ,encoding="utf8") as f:
            for items in l:
                p = str(items[0])+str(items[1])

                f.write(p)
                f.write('\n')
                #for i in items:
                    #f.write('%s\n' % items[0])
        f.close()

        num_correct = sum([np.argmax(a) == np.argmax(b) for a,b in zip(predictions , labels)])
        print('{0}/{1} accuracy : {2}% '.format(num_correct , len(images) , (num_correct/len(images))*100))


    @staticmethod
    def activation(x):
        return 1/(1+max(0,x))