import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "python"
tweet_list = []  
limit = 100 

for tweet in sntwitter.TwitterSearchScraper(query).get_items(): 

    if len(tweet_list) == limit: 
    	break
    else:
         tweet_list.append([tweet.date, tweet.user.username, tweet.user.displayname, tweet.content, tweet.url])
        
         
df = pd.DataFrame(tweet_list, columns = ['Date', 'User', 'Nickname', 'Tweet', 'URL'])

print(df) 

df.to_csv('python.csv', encoding='utf-8-sig') 