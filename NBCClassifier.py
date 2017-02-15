# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:57:34 2017

@author: Sriranjitha
"""
import numpy as np

def featureVector(words,x_train,y_train):
    n = len(y_train);
    p = len(words);
    c = p;

    # Creating feature vector
    
    fv = [[0 for y in range(p+1)] for x in range(n)]
           
    fv0 = [[0 for y in range(p+1)] ]
    fv1 = [[0 for y in range(p+1)] ]
    
    for i in range(n):
        print i
        for j in range(p):
            if(words[j] in x_train[i]):
                fv[i][j] = 1;
            else:
                fv[i][j]= 0;
        fv[i][c] = y_train[i]
        if(fv[i][c] == '1'):
            fv[i][c] = 1;
            fv1 = np.vstack([fv1,fv[i]]);
        else:
            fv[i][c] = 0;
            fv0 = np.vstack([fv0,fv[i]]);
             
    fv0 = np.delete(fv0, (0), axis=0)
    fv1 = np.delete(fv1, (0), axis=0)
        
#    print fv
#    print "Not done"
#    print len(fv),len(fv[0])
#    print len(fv0),len(fv0[0])
#    print len(fv1),len(fv1[0])
#  
    
    return fv,fv0,fv1
    
def calcProb(fv,fv0,fv1):

    p = len(fv0[0])
    
    fv0sum = np.sum(fv0,axis=0)
    fv1sum = np.sum(fv1,axis=0)
#    
    print len(fv0sum)
    print len(fv1sum)
#    print fv0sum[c]
#    print fv1sum[c]
#    
    
    # Calculating probabilities   
    
    Nk = [0 for x in range(2)]
    Nkw = [[0 for y in range(p+1)] for x in range(2)]
    
    Pkw = [[0 for y in range(p+1)] for x in range(2)]
    Pk = [0 for x in range(2)]
            
    N = len(fv)
    Nk[0] = len(fv0)
    Nk[1] = len(fv1)
    
    Nkw[0] = fv0sum;
    Nkw[1] = fv1sum;
    
    print Nk[0]
    print Nk[1]
    
    print Nkw[0]
    print Nkw[1]
    
    Nkwfloat0 = (np.array(Nkw[0])).astype(float)
    Nkwfloat1 = (np.array(Nkw[1])).astype(float)
    
    # Performing Laplace correction
    
    Nkwfloat0 = np.add(Nkwfloat0,1.0)
    Nkwfloat1 = np.add(Nkwfloat1,1.0)  
    
    Pkw[0] = np.divide(Nkwfloat0,float(Nk[0])+2.0)
    Pkw[1] = np.divide(Nkwfloat1,float(Nk[1])+2.0)
    
    print Nkwfloat0
    print Nk[0]+2.0
    print Pkw[0]
    print type(Pkw[0])
    print type(Nkw[0])
    
    Pk[0] = Nk[0]/float(N)
    Pk[1] = Nk[1]/float(N)
    
    print type(Pk[0])
#    print Pk[0][1]
    
    print "Done"
    return Nk,Nkw,Pkw,Pk
        
def testNbc(Nk,Nkw,Pkw,Pk,trainfv, trainfv0, trainfv1, testfv, testfv0, testfv1):
    
#    print "hi"
#    nt = len(testfv); # no. of test samples
#    pred = [0 for x in range(s)]
#            
#    p = len(testfv[0]) # no. of words
#    
    testfvTranspose = testfv.transpose()
    
    predTable = np.matmul(Pkw,testfvTranspose)
    print predTable.shape
    
#    for s in range(nt):
#        a = 1
#        for t in range(p):
#            a *= 
#    
    
    
    
    