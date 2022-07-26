import requests

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123",}

r=requests.get(url_get,params=payload)
print(r.url)
print("request body:",r.request.body)
print(r.status_code)
print("Response as text:" ,r.text)
print(r.headers['Content-Type'])
print("json",r.json())
print(r.json()['args'])

#POST Requests

#Like a get requests, a post us used to send data to a server

url_post='http://httpbin.org/post'
#We use post function and payload is passed to data
r_post=requests.post(url_post,data=payload)

print("POST request URL: ",r_post.url)
print("GET request URL: ",r.url)

#Body
print("POST request body:",r_post.request.body)
print("GET request body: ",r.request.body)


print(r_post.json()['form'])



