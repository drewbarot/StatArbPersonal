import requests

url = "https://besttime.app/api/v1/keys/pri_a8f59facce5f4f6a90e0096b6265de5d"

response = requests.request("GET", url)

print(response.json())



import requests
import datetime
import json
import pandas as pd
dictionaryData = {}
tempList = []
tempList2 = []

# List with multiple venues in tuples
venue_list = [
    ("Best Buy","5133 Richmond Ave, Houston"),
    ("Walmart Supercenter","8651 NW 13th Terrace, Doral"),
    ("Lululemon","592 5th Ave, New York"),
    ("Crocs","152 W 34th St, New York"),
    ("Target","1302 S La Brea Ave Ste A, Los Angeles"),
    ("Kohls","1265 Coolidge Hwy, Troy"),
    ("Gamestop","9598 Destiny USA Dr, Syracuse"),
    ("Dicks","10311 Destiny USA Dr, Syracuse"),
    ("Lowes","1659 Niagara Falls Blvd, Amherst"),
    ("HomeDepot","3201 E Central Texas Expy, Killeen"),
    ("BBBY","3165 Wonderland Rd S Unit 1")
    
]

for venue in venue_list:
    
    url = "https://besttime.app/api/v1/forecasts"
    params = {
        'api_key_private': 'pri_a8f59facce5f4f6a90e0096b6265de5d',
        'venue_name': venue[0],
        'venue_address': venue[1]
    }

    response = requests.request("POST", url, params=params)
    data = response.json()
    
    for i in range(0,7):
        dictionaryData[str(i)] = data['analysis'][i]['day_raw']
        
    
    
    url = "https://besttime.app/api/v1/forecasts/live"
    response2 = requests.request("POST", url, params=params)

    day = datetime.datetime.today().weekday()
    data2 = response2.json()
    actual = data2['analysis']['venue_live_busyness']
    hourStart = data2['analysis']['hour_start']
    predicted = dictionaryData[str(day)][hourStart-6]
    tempList.append(actual)
    tempList2.append(predicted)
    
    

output = pd.read_pickle("dfBestTime.pkl")

df = pd.DataFrame([tempList], columns=list('ABCDEFGHIJK'))

newDataframe = output.append(df)
newDataframe.to_pickle("dfBestTime.pkl")