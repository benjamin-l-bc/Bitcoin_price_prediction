# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:06:58 2018

@author: v-beshi
"""
import NNC
from sklearn.decomposition import IncrementalPCA
from sklearn.neural_network import MLPClassifier
import predict_btc_future
import pandas as pd
from sklearn.externals import joblib

pca=joblib.load('pca.m')
next5=joblib.load('next5.m')
next10=joblib.load('next10.m')
next15=joblib.load('next15.m')

feature=predict_btc_future.get_agg_data('_2').drop(['next_price5','next_price10','next_price15'],axis=1)

#def predict(x):
PCA_ed_feature=pca.transform(feature)
next_5=next5.predict(PCA_ed_feature)
next_10=next10.predict(PCA_ed_feature)
next_15=next15.predict(PCA_ed_feature)
result=pd.DataFrame({'next_5':next_5,'next_10':next_10,'next_15':next_15})