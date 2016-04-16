# -*- coding: utf-8 -*-
'''
Created on 2016年4月16日

@author: fly
'''
import socket  
address = ('127.0.0.1', 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()  
s.bind(address)  
s.listen(5)  
  
ss, addr = s.accept()  
print ('got connected from',addr  )
  
ss.send('byebye'.encode())
i = 0  
while i < 20:
    ra = ss.recv(512)  
    print (ra)
    ss.send('fuck'.encode())
    i +=1
    
ss.close()  
s.close() 