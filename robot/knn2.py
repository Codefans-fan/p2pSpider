# -*- coding: utf-8 -*-
'''
Created on Mar 15, 2016

@author: fky
'''
from numpy import zeros
from nt import listdir
from knn import classify

def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect
    
    
def handwriteingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify(vectorUnderTest,trainingMat,hwLabels,3)
        
        print("the classifier came back with: %d, the real answer is : %d" % (classifierResult,classNumStr))
        if classifierResult != classNumStr:
            errorCount += 1.0
    
    print("The total number of errors is: %d." % errorCount)
    print("The total error rate is: %f." % (errorCount/float(mTest)))
        




if __name__=='__main__':
    handwriteingClassTest()