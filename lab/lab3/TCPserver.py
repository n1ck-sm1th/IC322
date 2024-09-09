#Nicholas Smith
#Lab03 IC322

from socket import *
serverPort = 12000

#Create TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#Associate port number w/ socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    #This is the information from the request
    request = connectionSocket.recv(1024).decode()
    #Print the request to the server. Part 2 step 1.
    #Filename is parsed from the GET request. Method = [0] file = [1]
    filename = request.split()[1]
    #File object is opened using the open() for reading
    f = open(filename[1:]) 
    #Read from the file object
    responseStatus = "HTTP/1.1 200 OK\r\n"
    responseHeader = "\r\n"
    responseBody = " "
    #Read from the file.
    for line in f:
        responseBody += line
    response = responseStatus+responseHeader+responseBody
    #Error testing print line.
    #print(response)
    connectionSocket.send(response.encode())
    connectionSocket.close()
