# -*- coding: utf-8 -*-
'''
Created on Mar 10, 2016

@author: fky
'''
import sys
import zklib
import time
import zkconst

zk = zklib.ZKLib("172.69.8.4", 4370)
ret = zk.connect()
print ("connection:", ret)