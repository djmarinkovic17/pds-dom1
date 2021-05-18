import requests
import json

url = "https://getpantry.cloud/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/igorovbasket"

payload = json.dumps({
	"id": "9867",
	"ime": "Petar",
	"prezime": "Simoninovic",
	"smer": "poljoprivreda",
	"predmeti": [
		"poljoprivreda",
		"medicina",
		"srpski",
		"filozofija",
		"ors"
	],
	"prosek": 9.87,
	"kontakt": {
		"adresa": "Gradskih predsednika 6",
		"mesto": "Narnia",
		"telefon": "060 123 1232"
	}
})
headers = {
	'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
