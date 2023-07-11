#%%
import os
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime
import re

USER_NAME='' 
USE_AND_KEYWORDS=False
SEARCH_AND_KEYWORDS=' AND '.join(['이영지','지구오락실','안유진'])
SEARCH_OR_KEYWORDS=' OR '.join(['이은지','지락실'])
START_DATETIME="2022-01-01"
END_DATETIME="2023-03-19"
MAX_TWEETS=100
DIRECTORY_NAME='result'

SEARCH_TEXT=f"""
{f'from: {USER_NAME}' if USER_NAME else '' } {SEARCH_AND_KEYWORDS if USE_AND_KEYWORDS else SEARCH_OR_KEYWORDS} since:{START_DATETIME} until:{END_DATETIME}
"""

if not os.path.exists(DIRECTORY_NAME):
    os.makedirs(DIRECTORY_NAME)

#%%
tweets = []
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(SEARCH_TEXT).get_items()):
    if i>MAX_TWEETS:
        break
    tweet_date=datetime.datetime.strftime(tweet.date, "%Y-%m-%d")
    tweet_content=re.sub('\n',' ',tweet.rawContent.strip())
    tweets.append([tweet_date, f'{tweet.user.username}({tweet.id})', tweet_content])
    
tweets_df = pd.DataFrame(tweets, columns=['Datetime', 'Username (Tweet Id)', 'Content'])
tweets_df.to_csv(f'{DIRECTORY_NAME}/with_snscrape.csv')
# %%
