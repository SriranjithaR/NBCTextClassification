# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 00:47:43 2017

@author: Sriranjitha
"""
import numpy as np
import pandas as pd 
import string

def splitData(filename,percentage):


    fileLocation = filename
    df = pd.read_csv(fileLocation, sep='\t', dtype='str')
#    print df.shape
    
    msk = np.random.rand(len(df)) < (float(percentage)/100.0)
    train = df[msk]
    test = df[~msk]
    
    # Training data
    x_train = train.as_matrix()    
    rid_train = x_train[:,0]
    y_train = x_train[:,1]
    x_train = x_train[:,2]
    
    # Test data
    x_test = test.as_matrix()   
    rid_test = x_test[:,0]
    y_test = x_test[:,1]
    x_test = x_test[:,2]

    return rid_train,x_train,y_train,rid_test,x_test,y_test
    
def preprocess(reviewText):
    for i in range(len(reviewText)):       
        reviewText[i] = str(reviewText[i]).lower()
        reviewText[i] = reviewText[i].translate(None,string.punctuation)
        reviewText[i] = reviewText[i].split()
        
    return reviewText