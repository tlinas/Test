import requests

r = requests.get('https://www.python.org/static/img/python-logo@2x.png')
print(r.content)
with open('logo.png', 'wb') as f:
    f.write(r.content)
    print("nothing")