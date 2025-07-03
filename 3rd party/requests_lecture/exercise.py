import requests

# url = 'https://en.wikipedia.org/wiki/John_von_Neumann'
#
# response = requests.get(url)
# print(response.status_code)
# start =response.text.find('<title>')+len('<title>')
# end = response.text.find('</title>')
# print(response.text[start:end])

# url = 'https://httpbin.org/json'
#
# response = requests.get(url)
# print(response.headers['content-type'])
# x = response.json()
# print(type(x))

url = 'https://httpbin.org/anything'
params = {
    'a': 1,
    'b': 2
}

data = {
    'x': 500,
    'y': 200,
    'z': ['a', 'b', 'c']
}
response = requests.post(url, data, params=params)
#print(response.status_code, response.text)
x = response.json()
print(x)