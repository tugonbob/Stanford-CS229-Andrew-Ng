import requests
import json
import time
import csv




url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"


headers = {
	"X-RapidAPI-Key": "a71aba6589msh37bdbd47a65f874p1ca48ejsn20b6f6d93b6e",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}


dict = []
for offset in range(0, 10000, 50):
    time.sleep(0.13)
    querystring = {"city":"Houston","state":"TX","limit":"50","offset": f"{offset}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(offset, response)
    toJson = json.loads(response.text)

    for listing in toJson:
        dict.append(listing)


with open("CollectedData.tsv", "w") as output_file:
    dw = csv.DictWriter(output_file, sorted(dict[0].keys()), delimiter='\t', lineterminator='\n')
    dw.writeheader()
    dw.writerows(dict)


