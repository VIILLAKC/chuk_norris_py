import requests


api = 'http://localhost:4000/chucknorris'

data = requests.get(api)
con = 0
for item in data.json():
    con +=1
    print(item)


print(con)