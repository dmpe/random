import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys
import sqlalchemy
import pandas as pd
from pandas import DataFrame
from sqlalchemy import *
from sqlalchemy import schema
from sqlalchemy.types import *
import sqlalchemy.schema

'''

Copyright:
https://github.com/agalea91/twitter_search/blob/master/twitter_search.py
http://tweepy.readthedocs.io/en/v3.5.0/api.html#API.search
https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

In order to use this script you should register a data-mining application
with Twitter.  Good instructions for doing so can be found here:
http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

After doing this you can copy and paste your unique consumer key,
consumer secret, access token, and access secret into the load_api()
function below.

The main() function can be run by executing the command:
python twitter_search.py

I used Python 3 and tweepy version 3.5.0.  You will also need the other
packages imported above.
'''

def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = 'NOrVFOrKaGpOsD1LHjlDmD9lA'
    consumer_secret = '8Lg3hdsmIbEn9Q1fLTiWbCqHD7vp2OSc21mvTGElnudCr5jM7p'
    access_token = '49683260-3LQ6XoNAFi9R7MVaSGU1igwNxJkfxL6aFpUJfe7pG'
    access_secret = 'zNXNyrewzVYC2kIqQ1GlGQoLIDHmTJtjXpMFZhwKGxYb8'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

def return_id(searched_tweets):
    forma = [(a.created_at,
          a.text,
          a.retweet_count,
          a.favorite_count,
          a.id,
          a.user.name,
          a.user.screen_name,
          a.user.description,
          a.user.id,
          a.user.location,
          a.user.favourites_count,
          a.user.followers_count,
          a.user.friends_count,
          a.user.statuses_count,
          a.user.created_at,
          a.user.verified,
          a.user.time_zone,
          a.coordinates,
          a.in_reply_to_status_id,
          a.in_reply_to_user_id,
          a.in_reply_to_screen_name) if a.coordinates is None else (a.created_at,
          a.text,
          a.retweet_count,
          a.favorite_count,
          a.id,
          a.user.name,
          a.user.screen_name,
          a.user.description,
          a.user.id,
          a.user.location,
          a.user.favourites_count,
          a.user.followers_count,
          a.user.friends_count,
          a.user.statuses_count,
          a.user.created_at,
          a.user.verified,
          a.user.time_zone,
          str(a.coordinates['coordinates']),
          a.in_reply_to_status_id,
          a.in_reply_to_user_id,
          a.in_reply_to_screen_name) for a in searched_tweets]
    return(forma[0][4])

def main():
    api = load_api()
    max_tweets = 99
    #since_id=1 
    #max_id = -1
    min_days_old, max_days_old = 1, 2
    twe = api.list_timeline('ChillinQuillen', "Apple")
    max_id = return_id(twe)

    with open('alpha.json', 'r') as f:
        lines = f.readlines()
        since_id = json.loads(lines[-1])['id']
        print('Searching from the bottom ID in file', since_id, '   ', max_id)

    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
    #, per_page = 99)
        try:
            new_tweets = api.list_timeline('ChillinQuillen', "Apple" ,since_id=str(since_id),max_id=str(max_id-1))
            print('found',len(new_tweets),'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
            max_id = new_tweets[-1].id

        except api.error.TwitterError as e:
            print('exception raised, waiting 15 minutes', str(e))
            print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
            time.sleep(15*60)
            # open the json file and get the latest tweet ID



    with open('alpha.json', 'a') as f:
        for tweet in searched_tweets:
            json.dump(tweet._json, f)
            f.write('\n')

    forma = [(a.created_at,
          a.text,
          a.retweet_count,
          a.favorite_count,
          a.id,
          a.user.name,
          a.user.screen_name,
          a.user.description,
          a.user.id,
          a.user.location,
          a.user.favourites_count,
          a.user.followers_count,
          a.user.friends_count,
          a.user.statuses_count,
          a.user.created_at,
          a.user.verified,
          a.user.time_zone,
          a.coordinates,
          a.in_reply_to_status_id,
          a.in_reply_to_user_id,
          a.in_reply_to_screen_name) if a.coordinates is None else (a.created_at,
          a.text,
          a.retweet_count,
          a.favorite_count,
          a.id,
          a.user.name,
          a.user.screen_name,
          a.user.description,
          a.user.id,
          a.user.location,
          a.user.favourites_count,
          a.user.followers_count,
          a.user.friends_count,
          a.user.statuses_count,
          a.user.created_at,
          a.user.verified,
          a.user.time_zone,
          str(a.coordinates['coordinates']),
          a.in_reply_to_status_id,
          a.in_reply_to_user_id,
          a.in_reply_to_screen_name) for a in searched_tweets]

    data = {'created_at': [],'text': [],
        'retweet_count': [], 'tweet_id':[],
        'user_favorites_count': [], 'tweet_location': [],
        'user_followers_count':[], 'user_time_zone':[],
        'user_id':[], 'user_name':[], 'in_reply_to_status_id':[],
        'in_reply_to_user_id':[], 'in_reply_to_screen_name':[],
        'screen_name':[], 'user_verified':[],
        'user_location':[], 'user_description':[],
        'user_statuses_count': [], 'user_created_at':[],
        'user_friends_count': [], 'favorite_count': []}

    for t in forma:
        data['created_at'].append(t[0])
        data['text'].append(t[1])
        data['retweet_count'].append(t[2])
        data['favorite_count'].append(t[3])
        data['tweet_id'].append(t[4])
        data['user_name'].append(t[5])
        data['screen_name'].append(t[6])
        data['user_description'].append(t[7])
        data['user_id'].append(t[8])
        data['user_location'].append(t[9])
        data['user_favorites_count'].append(t[10])
        data['user_followers_count'].append(t[11])
        data['user_friends_count'].append(t[12])
        data['user_statuses_count'].append(t[13])
        data['user_created_at'].append(t[14])
        data['user_verified'].append(t[15])
        data['user_time_zone'].append(t[16])
        data['tweet_location'].append(t[17])
        data['in_reply_to_status_id'].append(t[18])
        data['in_reply_to_user_id'].append(t[19])
        data['in_reply_to_screen_name'].append(t[20])

    df = pd.DataFrame(data)
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['user_created_at'] = pd.to_datetime(df['user_created_at'])

    RT = []
    for t in data['text']:
        RT.append(t.split()[0]=='RT')
    df['RT'] = RT

    engine = create_engine('mysql+pymysql://root:@localhost/sawi_tweets?charset=utf8mb4', encoding='utf8', echo = False)
    df.to_sql('sawi_tweets_historical_test', engine, if_exists='append', dtype={'in_reply_to_status_id': sqlalchemy.types.Text, 'in_reply_to_user_id': sqlalchemy.types.Text} )

if __name__ == "__main__":
    main()
