# -*- coding: utf-8 -*-
"""Farmi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oRwlb2PQ_80HA7LAPsZ62T2zP-3_C40G
"""

#!wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1nmblNJwE2fzu0vmRmQOuWqOdR7Sg9hFG' -O Crop_recommendation.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
import pickle

data=pd.read_csv('G:/Project Done by ME/Crop prediction/First_flask/First_flask/Crop_recommendation.csv')

data.head()

data.columns

data.isnull().sum()

plt.pie(data.humidity.value_counts().to_list()[:10], labels=data.label.value_counts().index[:10], radius=1.8, autopct="%0.2f%%")
plt.show()

values = data.label.value_counts().to_list()[:10]
labels = data.label.value_counts().index[:10]
plt.figure(figsize=(15,5))
sns.barplot(x=values, y=labels)
plt.show()

sns.pairplot(data, hue='label')

X=data.drop('label', axis=1)
Y=data['label']

G = pd.unique(Y)

labelencoder = LabelEncoder()
y = labelencoder.fit_transform(Y)

dictionary = dict(zip(labelencoder.transform(labelencoder.classes_),labelencoder.classes_))
print(dictionary)

#encoded_data, mapping_index = pd.Series(y).factorize()

#print(encoded_data)
#print(mapping_index)

#dictionary = dict(zip(mapping_index, G))
#print(dictionary)

#dictionary2 = dict(zip(encoded_data, Y))
#print(dictionary2)

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2)

ler=LinearRegression()
ler.fit(X_train,y_train)

y_pred = ler.predict(X_test)

MSE=mean_squared_error(y_test, y_pred)  
print("RMSE Linear regression : ", sqrt(MSE))

pickle.dump(ler, open('farmi.pkl','wb'))

pickle.dump(labelencoder, open('labelencoder.pkl','wb'))

#dumping Encoded DATA after decoding
pickle.dump(dictionary,open('dict.pkl','wb'))
