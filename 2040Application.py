import json, requests, datetime

TOKEN = '9e048c151db34066955043ef2cad3799'
dict= {'token': TOKEN , 'github' : 'https://github.com/faisalgedi/Faisal2040FellowApp'}
r0 = requests.post("http://challenge.code2040.org/api/register", json = dict)



dict = {'token': TOKEN}
inputString = requests.post("http://challenge.code2040.org/api/reverse", dict)
reversedString = inputString.text[::-1]
send = {'token' : TOKEN, 'string': reversedString}
inputString = requests.post("http://challenge.code2040.org/api/reverse/validate",send)



r1 = requests.post("http://challenge.code2040.org/api/haystack", data={'token': TOKEN})
json = r1.json()
needle = json['needle']
haystack = json['haystack'] 
index = haystack.index(needle)
r1 = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token': TOKEN, 'needle': index})



r2 = requests.post("http://challenge.code2040.org/api/prefix", data={'token': TOKEN})
newArray = []
json = r2.json()
prefix = json['prefix']
array = json['array']
for item in array:
    
  if not item.startswith(prefix):
      
    newArray.append(item)
    
r2 = requests.post("http://challenge.code2040.org/api/prefix/validate", json={'token': TOKEN, 'array': newArray})




r3 = requests.post("http://challenge.code2040.org/api/dating", data={'token': TOKEN})
json = r3.json()
datestamp = json['datestamp']
interval = json['interval']
datestamp1 = datetime.datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
datestamp3 = datestamp1 + datetime.timedelta(seconds=int(interval))
datestamp4 = datestamp3.strftime("%Y-%m-%dT%H:%M:%SZ")
r3 = requests.post("http://challenge.code2040.org/api/dating/validate", data={'token': TOKEN, 'datestamp': datestamp4})
