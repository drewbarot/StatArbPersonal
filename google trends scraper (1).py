
#imports
import sys
import time
get_ipython().system('{sys.executable} --version')
import pandas as pd
import numpy as np

from pytrends.request import TrendReq

#set trendreq
pytrends = TrendReq(hl='en-US', tz=360)

stock_dict ={
    'best_buy': ['best buy', 'best buy near me', 'best buy sale'],
    'walmart': ['walmart', 'walmart near me', 'walmart grocery'],
    'lululemon': ['lululemon', 'lululemon near me', 'lululemon sale'],
    'crocs': ['crocs', 'crocs near me', 'crocs sale'],
    'target': ['target', 'target near me'],
    'kohls': ['kohls', 'kohls near me'],
    'gamestop': ['gamestop', 'gamestop near me'],
    'dicks_sporting_goods': ['dicks sporting goods', 'dicks sporting goods near me'],
    'lowes': ['lowes', 'lowes near me'],
    'home_depot': ['home depot', 'home depot near me'],
    'bed bath and beyond': ['bed bath and beyond', 'bed bath and beyond near me']
}


kw_list = [stock_dict['walmart'][0]]
hi = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

stock_keys = list(stock_dict)

# start by creating a payload for each
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
        

#blank dict to store values
stock_info ={
}




#bulk of project, this loops through each company and the search terms, and compiles them in a dict
for m in range(0,len(stock_dict)):
    list_index = stock_keys[m]
    dictionary_index = stock_dict[list_index]
    for i in range(0,len(dictionary_index)):
        
        #search volume for today
        kw_list = [dictionary_index[i]]
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='US', gprop='')
        popularity_dataframe = np.array(pytrends.interest_over_time())
        
        popularityNow = popularity_dataframe[len(popularity_dataframe)-1, 0]
        
        listNumbers = []
        for i in range(len(popularity_dataframe)-180, len(popularity_dataframe)-1):
            listNumbers.append(popularity_dataframe[i,0])
       
        append_value(stock_info, dictionary_index[0], popularityNow)
        
        

        #search volume compared to last year
        popularityLastYear = popularity_dataframe[len(popularity_dataframe)-365, 0]
        comparison = round(popularityNow/popularityLastYear,3)
        append_value(stock_info, dictionary_index[0], comparison)

    
        #is the current search above moving average
        total = 0
        for i in range(1,31):
            total += popularity_dataframe[len(popularity_dataframe)-i, 0]
            
        average = total/30
        aboveAverage = round(popularityNow/average,3)
        append_value(stock_info, dictionary_index[0], aboveAverage)
        

        weeksIncreasing = {}
        n = 7
        totalList = [listNumbers[i:i+n] for i in range(0, len(listNumbers), n)]
        
        length = len(totalList)
        for i in range(0, length-1):
            avg1 = 0
            avgFinal = 0
            for p in range(0, len(totalList[i])):
                
                avg1 += int(totalList[i][p])
    
            
            avgFinal = round(avg1 / len(totalList[i]), 3)
            append_value(weeksIncreasing, str(i+1), avgFinal)

        

        weeks = 1
        for i in range(len(weeksIncreasing), 0, -1):
    
            n_key = list(weeksIncreasing)[i-1]
            n_val = list(weeksIncreasing.values())[i-1]
            n1_val = list(weeksIncreasing.values())[i-2]
    
            if(i==1):
        
                break
            elif(n_val > n1_val):
                weeks += 1
        
            else: 
        
                break

        append_value(stock_info, dictionary_index[0], weeks)

final_stock_dict = {}
stockKey = list(stock_info)
n=4

for p in range(0, len(stock_keys)):
    length = len(stock_info[stockKey[p]])
    
    total = length / n
    for i in range(0,4):
        avg = 0
        if(total == 2):
            avg = (stock_info[stockKey[p]][i] + stock_info[stockKey[p]][i+4])/total
        if(total == 3):
            avg = (stock_info[stockKey[p]][i] + stock_info[stockKey[p]][i+4] + stock_info[stockKey[p]][i+8])/total
        if(total == 4):
            avg = (stock_info[stockKey[p]][i] + stock_info[stockKey[p]][i+4] + stock_info[stockKey[p]][i+8] + stock_info[stockKey[p]][i+12])/total    
        if(total == 5):
            avg = (stock_info[stockKey[p]][i] + stock_info[stockKey[p]][i+4] + stock_info[stockKey[p]][i+8] + stock_info[stockKey[p]][i+12] + stock_info[stockKey[p]][i+16])/total
        append_value(final_stock_dict, stockKey[p], avg)
        
busy = []

for i in range(0, len(stockKey)):
    busy.append(round(final_stock_dict[stockKey[i]][0],3))

output = pd.read_pickle("dfGoogleTrends.pkl")

df = pd.DataFrame([busy], columns=list('ABCDEFGHIJK'))

newDataframe = output.append(df)
newDataframe.to_pickle("dfGoogleTrends.pkl")