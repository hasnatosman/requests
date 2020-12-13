import requests
img_url = 'http://goo.gl/PsibBu'
r = requests.get(img_url)
with open('image.png', 'wb') as f:
    f.write(r.content)