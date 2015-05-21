import requests

url = "https://api.ammado.com/v1/categories"
apiKey = "92DB55DF-7027-4383-A050-3C51E04C1873"

payload = {'apiKey' : apiKey}

r = requests.get(url, params=payload)

data = r.json()

for item in data['categories']:

	print item
	
