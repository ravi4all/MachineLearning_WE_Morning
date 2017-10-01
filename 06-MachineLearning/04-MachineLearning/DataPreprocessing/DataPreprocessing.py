# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:15:31 2017

@author: asus
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv('data/Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

labelEncoder_x = LabelEncoder()
X[:, 0] = labelEncoder_x.fit_transform(X[:, 0])

from sklearn.preprocessing import OneHotEncoder

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)