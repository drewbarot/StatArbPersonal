

import praw
import pandas as pd
import datetime
from datetime import datetime, timedelta

reddit = praw.Reddit(client_id='huieylFVwbDC52PQszZveQ',client_secret='_eeGDXeSjDUDQnhQj7zeyEyazBJutA',user_agent='mustangCap',username='brennanrl',password='$Bunnysex69')


subreddit = reddit.subreddit('crocs')
for submission in subreddit.top(limit=1):
    print(submission.title, submission.id, submission.created_utc)

def submissionsWithin24hours(subreddit):
    subreddit = reddit.subreddit(subreddit)
    
    submissionsLast24 = 0
    scores = 0
    comms_number = 0
    for submission in subreddit.new(limit=100): 
        utcPostTime = submission.created_utc
        submissionDate = datetime.utcfromtimestamp(utcPostTime)
        submissionDateTuple = submissionDate.timetuple()

        currentTime = datetime.utcnow()

        #How long ago it was posted.
        submissionDelta = currentTime - submissionDate

        title = submission.title
        link = 'www.reddit.com' + submission.permalink
        submissionDelta = str(submissionDelta)
        
        if 'day' not in submissionDelta:
            submissionsLast24 +=1
            scores += submission.score
            comms_number += submission.num_comments
            
    avg_score = scores/submissionsLast24
    avg_comms = comms_number / submissionsLast24
    return_list = [submissionsLast24,avg_score,avg_comms]
            
    
    return return_list
theDictionary = ['BestBuy', 'walmart', 'lululemon', 'crocs', 'Target', 'homegym', 'GameStop', 'homegym', 'Lowes', 'HomeDepot', 'BedBathandBeyond']
finalDict = {}
for i in theDictionary:
    output = submissionsWithin24hours(i)
    finalDict[i] = output

    

busy = []


for i in range(0, len(finalDict)):
    busy.append(round(finalDict[theDictionary[i]][0],3))
    
output = pd.read_pickle("dfReddit.pkl")

df = pd.DataFrame([busy], columns=list('ABCDEFGHIJK'))

newDataframe = output.append(df)
newDataframe.to_pickle("dfReddit.pkl")
