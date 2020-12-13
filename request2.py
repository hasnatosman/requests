import requests
url = 'http://dimikcomputing.com'
response = requests.get(url)
with open('dikim.html', 'w') as f:
    f.write(response.text)