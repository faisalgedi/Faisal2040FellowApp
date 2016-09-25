import json, requests, datetime

TOKEN = '9e048c151db34066955043ef2cad3799'
dict= {'token': TOKEN , 'github' : 'https://github.com/faisalgedi/Faisal2040FellowApp'}
r = requests.post("http://challenge.code2040.org/api/register", json = dict)

print r
