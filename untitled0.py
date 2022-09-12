# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:11:59 2021

@author: Asus
"""

import untitled1 as nn
import numpy as np

with np.load('mnist.npz') as data:

    training_images = data['training_images']
    training_labels = data['training_labels']
    print(training_images.shape)

layer_sizes = (784,5,10)


net = nn.NeuralNetwork(layer_sizes)

net.print_accuracy(training_images,training_labels)