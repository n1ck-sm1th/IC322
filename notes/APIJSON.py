#Data structures can be represented in JSON. 
#JSON - Javascript Object Notation, much more efficient than XML and easier for humans to read.

#JSON example
import json

data = {
    "calculateArea": {
        "origin": { "x": 10, "y": 20 },
        "corners": [ { "x": 100, "y": 200 }, { "x": 150, "y": 250 } ]
    }
}

# `dumps`, or "dump string" converts a Python object to JSON.
json_string = json.dumps(data) 
print(json_string) #Prints information in JSON format.

# `loads`, or "load string" converts a JSON string to a Python object.
data = json.loads(json_string)
print(data)

#How JSON data can be sent in the HTTP body.
POST /calculateArea HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 92

{"calculateArea":{"origin":{"x":10,"y":20},"corners":[{"x":100,"y":200},{"x":150,"y":250}]}}

'''Curl allows us to make HTTP requests.
By default it makes GET requests but we can add url parameters. '''

#POST requests allow us to create new resources, most APIs require a POST request.
#POST request example
curl -X POST https://jsonplaceholder.typicode.com/posts \ #Specifies HTTP method to use.
     -H "Content-Type: application/json" \ #Sets content type header to application/json.
     -d '{"title":"foo", "body":"bar", "userId":1}' #Provides JSON data to send in the request body. 

#To include additional headers, we use API keys. 
curl --header "api-key: 2ab34-f29913" https://api.example.com/endpoint


#Python Requests
#Helps to make HTTP requests in Python. 

#Methods
get() #Method to make GET request.
json() #Handles response from GET request and decodes JSON. 

#Example get() & json() method usage, with parameters for the URL.  
import requests
response = requests.get("https://jsonplaceholder.typicode.com/comments", params={'postId': 1})
print(response.json())

#Passing data in the body of a POST or PUT request.
json= Argument encodes data as JSON
data= Argument uses "url form encoding" as its default.

#Example of using json= 
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post(url, json=payload)
print(response.json())
