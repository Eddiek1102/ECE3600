from socket import * 
import sys 

##### http://********/HelloWorld.html 
##### 

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a server socket 
#Fill in start 
serverPort = 6770
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1) 
#Fill in end 

while True: 
    #Establish the connection 
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept() 
    
    try: 
        message = connectionSocket.recv(1024).decode() 
        filename = message.split()[1] 
        f = open(filename[1:])
        outputdata = f.read() 
        
        #Fill in start 
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end 
        
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    
    except IOError: 
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        #Fill in end 
        
        #Close client socket 
        #Fill in start 
        connectionSocket.close() 
        #Fill in end 
        
    serverSocket.close() 
    sys.exit() 
    

