# -*- coding: utf-8 -*-
'''
Created on 2016年3月27日

@author: fly
'''

# example 1
def log(func):
    def wraper():
        print('Info:starting {}'.format(func.__name__))
        func()
        print('Info:finishing {}'.format(func.__name__))
    return wraper

@log
def run():
    print('Runing run...')

#end example 1

#example 2
from time import sleep, time

def timer(cls):
    def wraper():
        s = time()
        obj = cls()
        e = time()
        print('Cost {:.3f}s to init.'.format(e-s))
        return obj
    return wraper


@timer
class Obj():
    def __init__(self):
        print("hello")
        sleep(3)
        print('obj')
if __name__=='__main__':
    run()
    Obj()