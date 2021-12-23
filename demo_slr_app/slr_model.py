# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:51:25 2021

@author: ssridhar
"""

import os
import pickle

import pandas as pd
from sklearn import linear_model
from .constants import MODEL_PICKLE_FILE_NAME

print(os.getcwd())

lm = linear_model.LinearRegression()

X = pd.DataFrame({'x':[1,2,3,4,5]})

y = pd.Series([2,3,5,8,11])

lm.fit(X,y)

lm.coef_, lm.intercept_

lm.predict(X)

if not os.path.exists(MODEL_PICKLE_FILE_NAME):
    # save the model to disk
    pickle.dump(
        lm,
        open(MODEL_PICKLE_FILE_NAME, 'wb')
    )
