# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:05:11 2021
@author: AshwinBalaji
"""
print("\nCLIENT : SOCKET PROGRAMMING")
print("\n")

import socket
import sys

try:
    #Client socket creation
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("Requesting Server ..... ")

    #Connecting with the server HOST ID and it's PORT NUMBER
    client_socket.connect(('127.0.0.1', 19876))
    
    #Client is writing in the buffer as a request to the server
    get_input  = input('CLIENT : ')
    
    #Sending buffer info to the server
    client_socket.send(bytes(get_input,'utf-8'))
    '''
    using decode() will not print 'b' at the starting of the statement 
    '''
    #Response from the server will be printed at the client side
    print("SERVER : ", client_socket.recv(4096).decode())
    
except:
    sys.exit("Connection failed ....")
    



