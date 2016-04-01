# -*- coding: utf-8 -*-
'''
Created on Mar 15, 2016

@author: fky


k-近邻算法

'''

from numpy import array
import operator

from numpy.lib.shape_base import tile
def  createDataSet():
    group = array([[1.0,1.1],
                   [1.0,1.0],
                   [0,0],
                   [0,0.1]])
    
    labels = ['A','A','B','B']
    
    return group, labels



def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) -dataSet    #   算距离
    print(diffMat)
    sqDiffMat = diffMat**2      
    sqDistances = sqDiffMat.sum(axis=1)             #
    distances = sqDistances**0.5                    #
    print(sqDistances)
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):                              # 距离最小的k个点 
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)   # 排序
    print(sortedClassCount)
    return sortedClassCount[0][0]



if __name__=='__main__':
    group, labels = createDataSet()
    print(classify([1,1], group, labels, 3))
