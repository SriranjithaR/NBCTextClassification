# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 00:46:09 2017

@author: Sriranjitha
"""
from preprocess import splitData
from preprocess import preprocess
import numpy as np
import operator
from NBCClassifier import featureVector
from NBCClassifier import calcProb
from NBCClassifier import testNbc

#def max(a,b):
#    if (a>b):
#        return a
#    return b
    
# Getting data split using splitData function  
rid_train,x_train,y_train,rid_test,x_test,y_test = splitData('Data\yelp_data.csv',3);

# Pre-processing data
x_train = preprocess(x_train)
x_test = preprocess(x_test)

print y_train
# Creating dictionary from x_train
dlist = {}
words = {}

for i in range(len(x_train)):
    for word in x_train[i]:
        if(not words.has_key(word)):
            words[word] = 1;
            dlist[word] = i;
            
        else:
            if(dlist[word] != i):
                dlist[word] = i;
                words[word] += 1;
              
wordList = words.keys();
print len(wordList)
print len(words)



words = sorted(words.items(), key = operator.itemgetter(1), reverse = True)

trainfv, trainfv0, trainfv1  = featureVector(wordList, x_train, y_train)

Nk, Nkw, Pkw, Pk = calcProb(trainfv, trainfv0, trainfv1)

testfv, testfv0, testfv1 = featureVector(wordList, x_test, y_test)

zeroOneLoss = testNbc(Nk,Nkw,Pkw,Pk,trainfv, trainfv0, trainfv1, testfv, testfv0, testfv1   )

#d = words
#print len(d)
#for _ in range(100):
#    d.pop()
#
#print len(d)
#for i in range(100,600):
#    print d[i]
#    if (i==len(d)):
#        break;
#        
## Output top ten highest freq words
#for i in range(10):
#    print "WORD"+str(i+1)+" "+d[i][0]
#    if (i==len(d)):
#        break;
#print "ZERO-ONE-LOSS "
     
#print words
#o = len(words)

#for _ in range(100):
#    del words[max(words, key=words.get)]
      
#print repr(max)
#d = {}
#d = words
#for _ in range(100):
#    key_to_delete = max(words, key = dict(words).get(dict(words).keys()))
#    del words[key_to_delete]               
##               
#
#print o
#print len(words)
#              
#       
#print words
#    amax(d, key=lambda k: d[k])
