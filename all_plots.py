# imports 
import pandas as pd 
import matplotlib.pyplot as plt

# Company Names
names = {'A':'Best Buy','B':'Walmart','C':'Lululemon','D':'Crocs','E':'Target','F':'Kohl’s','G':'GameStop','H':'Dicks Sporting','I':'Lowe’s','J':'Home Depot','K':'Bed Bath and Beyond'}

def best_time_plot():
    # Read In NEW PKL
    df = pd.read_pickle('dfBestTime.pkl')

    # Transfer PKL DataFrame to a plot ready DataFrame

    newIndex = []
    # SMA is Currently the Col mean until there is more data
    sma = []
    weekAvg = []
    for column in df:
        newIndex.append(column)
        sma.append(df[column].mean())
        weekAvg.append(df[column][df.index[-1]])

    # Takes letter company symbol and uses dict to change it to real name + the title of data

    temp = []
    for i in range(len(newIndex)):
        if newIndex[i][0] in names:
            temp.append(names[newIndex[i][0]] + ' Busyness')
    newIndex = temp

    plotDf = pd.DataFrame({'Average':sma,'Current Week Average':weekAvg},index = newIndex)

    # Change "black" to desired text color
    plt.rcParams.update({'text.color' : "black",'axes.labelcolor' : "black"})

    # Change title= for main title or ylabel= for y axis title 

    plotFrame = plotDf.plot.bar(rot=90,color={"Average": "grey", "Current Week Average": "purple"},title='Companies Busyness', ylabel='Busyness',fontsize=10)
    ax = plotFrame.axes
    plotFrame.legend(bbox_to_anchor=(1.0, 1.0))
    plotFrame.plot()
    fig = plotFrame.get_figure()

    # Uncomment Desired Output
    fig.savefig('Best_Time_highRes.png',dpi=200,bbox_inches='tight')
    #fig.savefig('Best_Time_Web.png',bbox_inches='tight')
    
def google_trends_plot():

    # Read In PKL
    df = pd.read_pickle('dfGoogleTrends.pkl')

    # Transfer PKL DataFrame to a plot ready DataFrame

    newIndex = []
    # SMA is Currently the Col mean until there is more data
    sma = []
    weekAvg = []
    for column in df:
        newIndex.append(column)
        sma.append(df[column].mean())
        weekAvg.append(df[column][df.index[-1]])

    # Takes letter company symbol and uses dict to change it to real name + the title of data

    temp = []
    for i in range(len(newIndex)):
        if newIndex[i][0] in names:
            temp.append(names[newIndex[i][0]] + ' Interest')
    newIndex = temp

    plotDf = pd.DataFrame({'Average':sma,'Current Week Average':weekAvg},index = newIndex)

    # Change "black" to desired text color
    plt.rcParams.update({'text.color' : "black",'axes.labelcolor' : "black"})

    # Change title= for main title or ylabel= for y axis title 

    plotFrame = plotDf.plot.bar(rot=90,color={"Average": "grey", "Current Week Average": "purple"},title='Google Trends', ylabel='Interest Over Time',fontsize=10)
    ax = plotFrame.axes
    plotFrame.legend(bbox_to_anchor=(1.0, 1.0))
    plotFrame.plot()
    fig = plotFrame.get_figure()

    # Uncomment Desired Output
    fig.savefig('Google_Trends_highRes.png',dpi=200,bbox_inches='tight')
    #fig.savefig('Google_Trends.png',bbox_inches='tight')
    
def similar_web_plot():

    # Read In PKL
    df = pd.read_pickle('dfSimilarWeb.pkl')

    # Transfer PKL DataFrame to a plot ready DataFrame

    newIndex = []
    # SMA is Currently the Col mean until there is more data
    sma = []
    weekAvg = []
    for column in df:
        newIndex.append(column)
        sma.append(df[column].mean())
        weekAvg.append(df[column][df.index[-1]])

    # Takes letter company symbol and uses dict to change it to real name + the title of data

    temp = []
    for i in range(len(newIndex)):
        if newIndex[i][0] in names:
            temp.append(names[newIndex[i][0]] + ' Search Rank')
    newIndex = temp

    plotDf = pd.DataFrame({'Average':sma,'Current Week Average':weekAvg},index = newIndex)

    # Change "black" to desired text color
    plt.rcParams.update({'text.color' : "black",'axes.labelcolor' : "black"})

    # Change title= for main title or ylabel= for y axis title 

    plotFrame = plotDf.plot.bar(rot=90,color={"Average": "grey", "Current Week Average": "purple"},title='Companies Search Rank', ylabel='Search Rank',fontsize=10)

    plotFrame.legend(bbox_to_anchor=(1.0, 1.0))
    plotFrame.plot()
    fig = plotFrame.get_figure()

    # Uncomment Desired Output
    fig.savefig('Simmilar_Web_highRes.png',dpi=200,bbox_inches='tight')
    #fig.savefig('Simmilar_Web.png',bbox_inches='tight')
    
def twitter_plot():
    # Read In NEW PKL
    df = pd.read_pickle('dfTweepy.pkl')

    # Transfer PKL DataFrame to a plot ready DataFrame

    newIndex = []
    # SMA is Currently the Col mean until there is more data
    sma = []
    weekAvg = []
    for column in df:
        newIndex.append(column)
        sma.append(df[column].mean())
        weekAvg.append(df[column][df.index[-1]])

    # Takes letter company symbol and uses dict to change it to real name + the title of data

    temp = []
    for i in range(len(newIndex)):
        if newIndex[i][0] in names:
            temp.append(names[newIndex[i][0]] + ' Mentions')
    newIndex = temp

    plotDf = pd.DataFrame({'Average':sma,'Current Week Average':weekAvg},index = newIndex)

    # Change "black" to desired text color
    plt.rcParams.update({'text.color' : "black",'axes.labelcolor' : "black"})

    # Change title= for main title or ylabel= for y axis title 

    plotFrame = plotDf.plot.bar(rot=90,color={"Average": "grey", "Current Week Average": "purple"},title='Companies Twitter Mentions', ylabel='Volume of Mentions',fontsize=10)
    ax = plotFrame.axes
    plotFrame.legend(bbox_to_anchor=(1.0, 1.0))
    plotFrame.plot()
    fig = plotFrame.get_figure()

    # Uncomment Desired Output
    fig.savefig('Twitter_highRes.png',dpi=200,bbox_inches='tight')
    #fig.savefig('Twitter.png',bbox_inches='tight')
    
def reddit_plot():

    # Company Names
    names = {'A':'Best Buy','B':'Walmart','C':'Lululemon','D':'Crocs','E':'Target','F':'Kohl’s','G':'GameStop','H':'Dicks Sporting','I':'Lowe’s','J':'Home Depot','K':'Bed Bath and Beyond'}

    # Read In NEW PKL
    df = pd.read_pickle('dfReddit.pkl')

    # Transfer PKL DataFrame to a plot ready DataFrame

    newIndex = []
    # SMA is Currently the Col mean until there is more data
    sma = []
    weekAvg = []
    for column in df:
        newIndex.append(column)
        sma.append(df[column].mean())
        weekAvg.append(df[column][df.index[-1]])

    # Takes letter company symbol and uses dict to change it to real name + the title of data

    temp = []
    for i in range(len(newIndex)):
        if newIndex[i][0] in names:
            temp.append(names[newIndex[i][0]] + ' Mentions')
    newIndex = temp

    plotDf = pd.DataFrame({'Average':sma,'Current Week Average':weekAvg},index = newIndex)

    # Change "black" to desired text color
    plt.rcParams.update({'text.color' : "black",'axes.labelcolor' : "black"})

    # Change title= for main title or ylabel= for y axis title 

    plotFrame = plotDf.plot.bar(rot=90,color={"Average": "grey", "Current Week Average": "purple"},title='Companies Reddit Mentions', ylabel='Volume of Mentions',fontsize=10)
    ax = plotFrame.axes
    plotFrame.legend(bbox_to_anchor=(1.0, 1.0))
    plotFrame.plot()
    fig = plotFrame.get_figure()

    # Uncomment Desired Output
    fig.savefig('Reddit_highRes.png',dpi=200,bbox_inches='tight')
    #fig.savefig('Reddit.png',bbox_inches='tight')

if __name__ == "__main__":
    
    best_time_plot()
    google_trends_plot()
    similar_web_plot()
    twitter_plot()
    reddit_plot()

