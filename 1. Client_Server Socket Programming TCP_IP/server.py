# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:03:47 2021
@author: AshwinBalaji
"""
print("\nSERVER : SOCKET PROGRAMMING")
print("\n")
import socket
import sys

'''
1. SOCKET()
2. BIND()
3. LISTEN()
4. ACCEPT()
5. CONNECT()
6. READ() <------> WRITE()
7. CLOSE()

'''

try:
    
    '''
    socket() two parameters
    
    Type of network (IPV4/IPV6) default: IPV4
    AF_INET, PF_INET, PF_UNIX, PF_X25 etc. and INET(refers IPV4)
    
    Type of protocol (TCP/UDP) default:TCP
    SOCK_STREAM (connection_oriented)  SOCK_DGRAM (connection-less)
    '''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server Socket Initiated .....")
    
    '''
    bind() take single parameter having (client_address, port_number)
    Since, same machine is client as well as server, so localhost
    Port number 2^16-1 = 65535 
    1. 0-1024 well-known/reserved ports
    2. x > 1024 ephemeral ports
    '''
    host = '127.0.0.1'
    port = 19876
    server_socket.bind((host, port))
    
    '''
    listen(#clients)
    '''
    #print("test")
    server_socket.listen(3)
    print('\nWaiting for a conversation with the clients ......\n')
    
    '''
    accept() returns two parameters client_socket and client_address
    '''
    while True:
        #Accepting client socket and port
        client_socket, client_port = server_socket.accept()
        
        #Receiving buffer info written by the client at the server side
        #Buffer size is mentioned
        get_input = client_socket.recv(4096).decode()
        
        #print("Connected with", client_port)
        
        #Reading client's request at the server side
        print("CLIENT : ", get_input)
        
        #Server writing reponse in the buffer
        puts_input = input("SERVER : ")
        
        #Server sendin the buffer info to the client
        client_socket.send(bytes(puts_input, "utf-8"))
        
        client_socket.close()
except:
    sys.exit("Initiation failed .....")
    
    
    
    

