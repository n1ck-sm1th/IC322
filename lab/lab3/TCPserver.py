#Nicholas Smith
#Lab03 IC322
#AI utilized for STEP 4 as prescribed in the instruction. 
#Specifically gave instruction on what Mimetypes was and how to
#adequately read a file in binary mode. 

from socket import *
import mimetypes
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
    
    #Filename is parsed from the GET request. Method = [0] file = [1]
    filename = request.split()[1]
    
    #Mimetypes figures out what type of file we are using.
    content_type, _ = mimetypes.guess_type(filename)

    #Defaults to binary stream if type cannot be determined. 
    if content_type is None:
        content_type = 'application/octet-stream'  

    # Open the file in binary mode
    with open(filename[1:], 'rb') as f:
        responseBody = f.read()

    # Construct the response
    responseStatus = "HTTP/1.1 200 OK\r\n"
    
    #Change the content type depending on result of Mimetypes function.
    responseHeader = f"Content-Type: {content_type}\r\nContent-Length: {len(responseBody)}\r\n\r\n"
    response = responseStatus.encode() + responseHeader.encode() + responseBody     
    connectionSocket.send(response)
    connectionSocket.close()
