# -*- coding: utf-8 -*-
'''
Created on Mar 29, 2016

@author: fky
'''

class PropertyTest():
    
    def __init__(self):
        self._name=None
        self._onlygetter = None
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,m_name):
        self._name = m_name
    
    @property
    def onlygetter(self):
        return self._onlygetter
        
if __name__=='__main__':
    p = PropertyTest()
    p.name = 'sdf'
    
    print(p.name)
    print(p.onlygetter)
    
    try:
        p.onlygetter = 'ds'
    except Exception as e:
        print(e)