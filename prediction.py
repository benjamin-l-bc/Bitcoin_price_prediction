# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:06:58 2018

@author: v-beshi
"""
import pickle
from sklearn.decomposition import IncrementalPCA
from sklearn.neural_network import MLPClassifier
nn5=pickle.loads(s_next5)
nn10=pickle.loads(s_next5)
n15=pickle.loads(s_next5)
pca=pickle.loads(dataPCA)

def predict(x):
    PCA_ed_feature=pca(x)
    next_5=nn5.predict(PCA_ed_feature)
    next_10=nn10.predict(PCA_ed_feature)
    next_15=nn15.predict(PCA_ed_feature)