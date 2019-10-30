import requests

url_1 = "http://httpbin.org/"
url_2 = "http://httpbin.org/status/200"
url_3 = "http://httpbin.org/delay/1"
url_4 = "http://httpbin.org/anything/200"
url_5 = "http://httpbin.org/redirect-to"

get_1 = requests.request("GET", url_1+"get")
get_2 = requests.request("GET", url_2)
get_3 = requests.request("GET", url_3)
get_4 = requests.request("GET", url_4)
get_5 = requests.request("GET", url_5)

post_1 = requests.request("POST", url_1+"post")
post_2 = requests.request("POST", url_2)
post_3 = requests.request("POST", url_3)
post_4 = requests.request("POST", url_4)
post_5 = requests.request("POST", url_5)

put_1 = requests.request("PUT", url_1+"put")
put_2 = requests.request("PUT", url_2)
put_3 = requests.request("PUT", url_3)
put_4 = requests.request("PUT", url_4)
put_5 = requests.request("PUT", url_5)

delete_1 = requests.request("DELETE", url_1+"delete")
delete_2 = requests.request("DELETE", url_2)
delete_3 = requests.request("DELETE", url_3)
delete_4 = requests.request("DELETE", url_4)
delete_5 = requests.request("DELETE", url_5)

print(get_1.status_code)
print(get_2.status_code)
print(get_3.status_code)
print(get_4.status_code)
print(get_5.status_code)

print()

print(post_1.status_code)
print(post_2.status_code)
print(post_3.status_code)
print(post_4.status_code)
print(post_5.status_code)

print()

print(put_1.status_code)
print(put_2.status_code)
print(put_3.status_code)
print(put_4.status_code)
print(put_5.status_code)

print()

print(delete_1.status_code)
print(delete_2.status_code)
print(delete_3.status_code)
print(delete_4.status_code)
print(delete_5.status_code)