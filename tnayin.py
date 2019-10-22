import requests

g = requests.request("GET", "https://httpbin.org/base64/23")
print(g.content)
g1 = requests.request("GET","https://httpbin.org/bytes/2")
print(g1.content)
g2 = requests.request("GET","https://httpbin.org/delay/name")
print(g2.content)
g3 = requests.request("GET","https://httpbin.org/drip")
print(g3.content)
g4 = requests.request("GET","https://httpbin.org/stream/7")
print(g4.content)

v = {}
v["name"] = ["surname"]
p = requests.request("POST","https://httpbin.org/delay",data=v)
print(p.content)
p1 = requests.request("POST","https://httpbin.org/anything",data=v)
print(p1.content)
p2 = requests.request("POST","https://httpbin.org/delay/name",data=v)
print(p2.content)
p3 = requests.request("POST","https://httpbin.org/drip",data=v)
print(p3.content)
p4 = requests.request("POST","https://httpbin.org/stream/7",data=v)
print(p4.content)



d = requests.request("DELETE","https://httpbin.org/delay")
print(d.content)
d1 = requests.request("DELETE","https://httpbin.org/anything")
print(d1.content)
d2 = requests.request("DELETE","https://httpbin.org/delay/name")
print(d2.content)
d3 = requests.request("DELETE","https://httpbin.org/drip")
print(d3.content)
d4 = requests.request("DELETE","https://httpbin.org/stream/7")
print(d4.content)


a = {}
a["name"] = ["surname"]
k = requests.request("PUT","https://httpbin.org/delay",data=a)
print(k.content)
k1 = requests.request("PUT","https://httpbin.org/anything",data=a)
print(k1.content)
k2 = requests.request("PUT","https://httpbin.org/delay/name",data=a)
print(k2.content)
k3 = requests.request("PUT","https://httpbin.org/drip",data=a)
print(k3.content)
k4 = requests.request("PUT","https://httpbin.org/stream/7",data=a)
print(k4.content)
