import requests
url = 'http://subeen.com/allposts/'
response = requests.get(url)
print(response.ok)
print(response.status_code)
