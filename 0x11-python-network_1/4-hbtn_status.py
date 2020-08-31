#!/usr/bin/python3
import requests
''' fetch https://intranet.hbtn.io/status '''


r = requests.get('https://intranet.hbtn.io/status')
print('Body response:\n\t- type: {}\n\t- content: {}\
'.format(r.text.__class__, r.text))
