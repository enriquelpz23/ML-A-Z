#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:33:36 2020

@author: enriquelopez
"""

# Importar bibliotecas y dataset

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.impute import SimpleImputer as Imputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split

#%% 
dataset = pd.read_csv("Data.csv")

# Divider variables ind y dep

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 3]

#%%

# Sustituir NaN por la media de la columna axis = 0

imputer = Imputer(missing_values = np.nan, strategy = "mean") 
imputer = imputer.fit(X.iloc[:, 1:3])

X.iloc[:, 1:3] = imputer.transform(X.iloc[:, 1:3])

#%%

# Cambiar categoricas por numericas

countries = {
    "France": 1,
    "Spain": 2, 
    "Germany": 3
    }

## dataset.replace({"Country": countries}) 

X["Country"] = X["Country"].map(countries)

#%%

# Crear variables dummy

onehotencoder = make_column_transformer((OneHotEncoder(), [0]), remainder = "passthrough")
X = onehotencoder.fit_transform(X)

#%% 

# Categoricas a numericas en variable objetivo

purchased = {
    "No": 0, 
    "Yes": 1
    }

y = y.map(purchased)

#%%

# Split en train y test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



#%%

# Escalar variables 

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)









