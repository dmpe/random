import twitter
import json
from datetime import datetime, timedelta
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
import codecs

def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    api = twitter.Api(consumer_key = 'M4KaokwzlBJipgUu8EuDQ',
    consumer_secret = '2aXzuelP1eaNxbQcHO8J2jyr61MGdyFk9RSt9GGg8',
    access_token_key = '49683260-jt08EFQlE7YO0BKwcaG3NOOQ4ccVLtxiC9ELo1EG7',
    access_token_secret = 'ZFTG35LSSTahObg8aLMGJ7JZ6h4201dYbJTIF43bHYpee')
    #api = twitter.Api(consumer_key = 'NOrVFOrKaGpOsD1LHjlDmD9lA',
    #consumer_secret = '8Lg3hdsmIbEn9Q1fLTiWbCqHD7vp2OSc21mvTGElnudCr5jM7p',
    #access_token_key = '49683260-3LQ6XoNAFi9R7MVaSGU1igwNxJkfxL6aFpUJfe7pG',
    #access_token_secret = 'zNXNyrewzVYC2kIqQ1GlGQoLIDHmTJtjXpMFZhwKGxYb8')

    # load the twitter API via tweepy
    return api

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
    #print(api.VerifyCredentials())
    since= datetime.utcnow() - timedelta(hours=24)
    print(since)
    statuses = []
    fc = api.GetListTimeline(slug='Apple', owner_screen_name= 'ChillinQuillen')
    most_recent = return_id(fc)
    print(most_recent)
    #max_id=str(most_recent-1)
    fd = api.GetListTimeline(slug='Apple', owner_screen_name= 'ChillinQuillen')

    # Find all tweets since the provided datetime
    for status in fd:
        #if status.created_at < str(since):
        #    break
        #else:
        statuses.append(status)

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
                                                                        a.in_reply_to_screen_name) for a in statuses]

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
        df.to_sql('sawi_tweets_historical_test_4', engine, if_exists='replace', dtype={'in_reply_to_status_id': sqlalchemy.types.Text, 'in_reply_to_user_id': sqlalchemy.types.Text})

if __name__ == "__main__":
    main()
