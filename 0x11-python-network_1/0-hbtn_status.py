#!/usr/bin/python3
from urllib import request
''' fetch https://intranet.hbtn.io/status '''


with request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}\
'.format(html.__class__, html, html.decode()))
