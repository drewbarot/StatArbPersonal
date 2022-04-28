
#imports
import sys
get_ipython().system('{sys.executable} --version')
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import json



#method to add to blank dictionaries
def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value
        
        
        
#dict with company names and url for alexa search ranking        
website_dict = {'best_buy': 'https://www.alexa.com/siteinfo/bestbuy.com',
    'walmart': 'https://www.alexa.com/siteinfo/walmart.com',
    'lululemon': 'https://www.alexa.com/siteinfo/lululemon.com',
    'crocs': 'https://www.alexa.com/siteinfo/crocs.com',
    'target': 'https://www.alexa.com/siteinfo/target.com',
    'kohls': 'https://www.alexa.com/siteinfo/kohls.com',
    'gamestop': 'https://www.alexa.com/siteinfo/gamestop.com',
    'dicks_sporting_goods': 'https://www.alexa.com/siteinfo/dickssportinggoods.com',
    'lowes': 'https://www.alexa.com/siteinfo/lowes.com',
    'home_depot': 'https://www.alexa.com/siteinfo/homedepot.com',
    'bed bath and beyond': 'https://www.alexa.com/siteinfo/bedbathandbeyond.com'}


website_keys = list(website_dict)
website_dict_final = {}

#loop that goes through each website and compiles values in website_dict
for i in range(0, len(website_keys)):
    name = website_keys[i]
    URL = website_dict[website_keys[i]]
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="rankData")
    niceResults = results.prettify()        
    finalDict = niceResults[58:-12]
    
    converted = json.loads(finalDict)
    
    
    
    #current search
    keys = list(converted)
    currentTraffic = converted[keys[len(keys)-1]]
    append_value(website_dict_final, name, currentTraffic)
    

    
    
    
    #is current above the moving average?
    avg = 0
    for i in range(0, len(keys)-1):
        avg += int(converted[keys[i]])
    averageTraffic = round(avg / len(keys),1)
    percentAboveAverage = round(float(currentTraffic) / averageTraffic,2)
    append_value(website_dict_final, name, percentAboveAverage)
    
    
    #weeks increasing 
    n = 7
    weeksIncreasing = {}
    totalList = [keys[i:i+n] for i in range(0, len(keys), n)]
    length = len(totalList)
    for i in range(0, length-1):
        avg1 = 0
        avgFinal = 0
        for p in range(0, len(totalList[i])):
            avg1 += int(converted[totalList[i][p]])
    
        avgFinal = round(avg1 / len(totalList[i]), 3)
        append_value(weeksIncreasing, str(i+1), avgFinal)

    

    weeks = 1
    for i in range(len(weeksIncreasing), 0, -1):
    
        n_key = list(weeksIncreasing)[i-1]
        n_val = list(weeksIncreasing.values())[i-1]
        n1_val = list(weeksIncreasing.values())[i-2]
    
        if(i==1):
        
            break
        elif(n_val < n1_val):
            weeks += 1
        
        else: 
        
            break
    append_value(website_dict_final, name, weeks)
        


busy = []

for i in range(0, len(website_keys)):
    busy.append(round(float(website_dict_final[website_keys[i]][0]),3))
    
output = pd.read_pickle("dfSimilarWeb.pkl")

df = pd.DataFrame([busy], columns=list('ABCDEFGHIJK'))

newDataframe = output.append(df)
newDataframe.to_pickle("dfSimilarWeb.pkl")




