import requests

url_1 = "http://httpbin.org/headers"
url_2 = "http://httpbin.org/ip"
url_3 = "http://httpbin.org/html"
url_4 = "http://httpbin.org/json"
url_5 = "http://httpbin.org/xml"

get_1 = requests.request("GET", url_1)
get_2 = requests.request("GET", url_2)
get_3 = requests.request("GET", url_3)
get_4 = requests.request("GET", url_4)
get_5 = requests.request("GET", url_5)

print(get_1.status_code)
print(get_1.content)
print(get_2.status_code)
print(get_2.content)
print(get_3.status_code)
print(get_3.content)
print(get_4.status_code)
print(get_4.content)
print(get_5.status_code)
print(get_5.content)