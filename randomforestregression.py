# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:53:09 2018

@author: v-beshi
"""

import predict_btc_future
from sklearn import preprocessing
from sklearn.decomposition import IncrementalPCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

data=predict_btc_future.get_agg_data()

data['bids_wall']=data['bfx_bids_wall']/100
data['asks_wall']=data['bfx_asks_wall']/100
data['total_bids']=data['bfx_total_bids']/100
data['total_asks']=data['bfx_total_asks']/100
data['buy_volumn']=data['bfx_buy_volumn']/50
data['sell_volumn']=data['bfx_sell_volumn']/50
trade_data=data.drop(['bfx_bids_wall','bfx_asks_wall','bfx_total_bids','bfx_total_asks','bfx_buy_volumn','bfx_sell_volumn'],axis=1)
features=trade_data.drop(['next_price5','next_price10','next_price15'],axis=1)
y1=trade_data['next_price5']
y2=trade_data['next_price10']
y3=trade_data['next_price15']
PCA=IncrementalPCA(n_components=5)
PCA.fit(features)
PCA_feature=PCA.transform(features)
X_train,X_test,y1_train,y1_test=train_test_split(PCA_feature,y1,test_size=0.33)
rfr=RandomForestRegressor()