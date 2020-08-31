#!/usr/bin/python3
import requests
''' fetch https://intranet.hbtn.io/status '''


html = requests.get('https://intranet.hbtn.io/status')
print('Body response:\n\t- type: {}\n\t- content: {}\
'.format(html.text.__class__, html.text))
