# -*- coding: utf-8 -*-
'''
Created on 2016年4月16日

@author: fly
'''

import threading
import time
import socket  

def sendToServer(client):
    time.sleep(4)
    client.send('hello world.'.encode())
    

address = ('127.0.0.1', 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(address)  

i = 0
while i < 20:
    t = threading.Thread(target=sendToServer, args=(s,))
    t.start()
    data = s.recv(512)  
    time.sleep(5)
    print ('the data received is',data ) 
    i += 1
s.send('hihi'.encode())  
  
s.close()  