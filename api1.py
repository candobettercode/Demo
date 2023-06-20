import requests

response = requests.get('https://randomfox.ca/floof')
print(response.status_code) #print status code whether site is acessible
print(response.text)
print(response.json)
fox = response.json()
print(fox['image'])