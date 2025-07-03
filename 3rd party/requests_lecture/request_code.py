import requests

# response = requests.get("https://www.stackoverflow.com")
#
# for key, value in response.headers.items():
#     print(f"{key}: {value}")

# query_params = {
#     'q': 'python http requests',
#     'num': 5
#     }
# response = requests.get(
#     "https://www.google.com",
#     params=query_params
# )
#
# #print(response.status_code, response.reason)
# #print(response.headers['content-type'])
# print(response.headers['content-encoding'])
API_KEY = "d1if1f9r01qhsrhf68s0d1if1f9r01qhsrhf68sg"
base_url = 'https://finnhub.io/api/v1'
url = f'{base_url}/quote'
params = {
    'token': API_KEY,
    'symbol': 'AAPL'
}

response = requests.get(url, params)
print(response.json())