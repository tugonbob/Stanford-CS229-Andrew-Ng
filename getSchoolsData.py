from gc import collect
from textwrap import indent
import requests
import json
import time
import csv

url = "https://gs-api.greatschools.org/schools"
headers = {
	"x-api-key": "Ojyww9Xi206CmuUOBCni184ksYiq3dfj3ytMcxbJ"
}

# parse CollectedData.tsv
collectedData = []
with open("_backupDb.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        collectedData.append(line)

# get all unique zipcodes
zips = []
for i, house in enumerate(collectedData):
    if i == 0:
        continue

    zip = house[22]

    try:
        zips.index(zip)
        continue
    except:
        zips.append(zip)

dict = {}
for zip in zips:
    # call great schools api
    querystring = {'zip': zip, 'school_type': 'public'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    toJson = json.loads(response.text)
    print(toJson)
    dict[zip] = toJson['schools']



# write dict to file
with open("houstonSchools.json", "w") as outfile:
    outfile.write(dict)


