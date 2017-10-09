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



def tweet_search(api, query, max_tweets, max_id, since_id):
    ''' Function that takes in a search string 'query', the maximum
        number of tweets 'max_tweets', and the minimum (i.e., starting)
        tweet id. It returns a list of tweepy.models.Status objects. '''

    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=remaining_tweets,lang ="en",
                                    since_id=str(since_id),max_id=str(max_id-1))
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
    return searched_tweets, max_id


def get_tweet_id(api, date='', days_ago=9, query='a'):
    ''' Function that gets the ID of a tweet. This ID can then be
        used as a 'starting point' from which to search. The query is
        required and has been set to a commonly used word by default.
        The variable 'days_ago' has been initialized to the maximum
        amount we are able to search back in time (9).'''

    if date:
        # return an ID from the start of the given day
        td = date + dt.timedelta(days=1)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet = api.search(q=query, count=1, until=tweet_date, lang ="en")
    else:
        # return an ID from __ days ago
        td = dt.datetime.now() - dt.timedelta(days=days_ago)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        # get list of up to 10 tweets
        tweet = api.search(q=query, count=10, until=tweet_date, lang ="en")
        print('search limit (start/stop):',tweet[0].created_at)
        # return the id of the first tweet in the list
        return tweet[0].id


def write_tweets(tweets, filename):
    ''' Function that appends tweets to a file. '''

    with open(filename, 'a') as f:
        for tweet in tweets:
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
          a.in_reply_to_screen_name) for a in tweets]

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
    df.to_sql('sawi_tweets_historical', engine, if_exists='append', dtype={'in_reply_to_status_id': sqlalchemy.types.Text, 'in_reply_to_user_id': sqlalchemy.types.Text} )
    #df.to_pickle('my_file.pkl')
    # 

def main():
    ''' This is a script that continuously searches for tweets
        that were created over a given number of days. The search
        dates and search phrase can be changed below. '''



    ''' search variables: '''
    search_phrases = ['#apple #iphoneX', 'iphone', 'apple', 'iphoneX', '#iphone']
    time_limit = 1.5                           # runtime limit in hours
    max_tweets = 100                           # number of tweets per search (will be
                                               # iterated over) - maximum is 100
    min_days_old, max_days_old = 1, 3          # search limits e.g., from 7 to 8
                                               # gives current weekday from last week,
                                               # min_days_old=0 will search from right now
    # loop over search items,
    # creating a new file for each
    for search_phrase in search_phrases:

        print('Search phrase =', search_phrase)

        ''' other variables '''
        name = search_phrase.split()[0]
        json_file_root = name + '/'  + name
        os.makedirs(os.path.dirname(json_file_root), exist_ok=True)
        read_IDs = False

        # open a file in which to store the tweets
        if max_days_old - min_days_old == 1:
            d = dt.datetime.now() - dt.timedelta(days=min_days_old)
            day = '{0}-{1:0>2}-{2:0>2}'.format(d.year, d.month, d.day)
        else:
            d1 = dt.datetime.now() - dt.timedelta(days=max_days_old-1)
            d2 = dt.datetime.now() - dt.timedelta(days=min_days_old)
            day = '{0}-{1:0>2}-{2:0>2}_to_{3}-{4:0>2}-{5:0>2}'.format(
                  d1.year, d1.month, d1.day, d2.year, d2.month, d2.day)
        json_file = json_file_root + '_' + day + '.json'
        if os.path.isfile(json_file):
            print('Appending tweets to file named: ',json_file)
            read_IDs = True

        # authorize and load the twitter API
        api = load_api()

        # set the 'starting point' ID for tweet collection
        if read_IDs:
            # open the json file and get the latest tweet ID
            with open(json_file, 'r') as f:
                lines = f.readlines()
                max_id = json.loads(lines[-1])['id']
                print('Searching from the bottom ID in file')
        else:
            # get the ID of a tweet that is min_days_old
            if min_days_old == 0:
                max_id = -1
            else:
                max_id = get_tweet_id(api, days_ago=(min_days_old-1))
        # set the smallest ID to search for
        since_id = get_tweet_id(api, days_ago=(max_days_old-1))
        print('max id (starting point) =', max_id)
        print('since id (ending point) =', since_id)



        ''' tweet gathering loop  '''
        start = dt.datetime.now()
        end = start + dt.timedelta(hours=time_limit)
        count, exitcount = 0, 0
        while dt.datetime.now() < end:
            count += 1
            print('count =',count)
            # collect tweets and update max_id
            tweets, max_id = tweet_search(api, search_phrase, max_tweets,
                                          max_id=max_id, since_id=since_id)
            # write tweets to file in JSON format
            if tweets:
                write_tweets(tweets, json_file)
                exitcount = 0
            else:
                exitcount += 1
                if exitcount == 3:
                    if search_phrase == search_phrases[-1]:
                        sys.exit('Maximum number of empty tweet strings reached - exiting')
                    else:
                        print('Maximum number of empty tweet strings reached - breaking')
                        break


if __name__ == "__main__":
    main()
