#!/usr/bin/env python
# coding: utf-8

# In[110]:


import os
import configparser
from datetime import datetime

from twython import Twython
import pandas as pd


# In[22]:


# const
CRED_FNAME = 'credentials.txt'


# In[111]:


class TweetLoader(object):
    
    def __init__(self, cred_dir = '../twitter-cred', cred_fname = CRED_FNAME):
        cred_fpath = os.path.join(cred_dir, cred_fname)
        print(f"Retrieve twitter credential: {cred_fpath}")
        if os.path.exists(cred_fpath):
            config = configparser.ConfigParser()
            config.read(cred_fpath)
            try:
                self._app_key = config['OAUTH']['app_key']
                self._app_secret = config['OAUTH']['app_secret']
                self._oauth_token = config['OAUTH']['oauth_token']
                self._oauth_token_secret = config['OAUTH']['oauth_token_secret']
            except KeyError as ex:
                raise ValueError(f"Failure to read field: {ex}")
                
            self.twitter = Twython(self._app_key, self._app_secret)
        else:
            raise ValueError(f"Failed to read credential file: {cred_fpath}")
            
    def get_tweets(self, query, from_date, to_date, count=50):
        tweets = []
        results = self.twitter.search(q=query, until=to_date, count=count)
        
        to_date = datetime.strptime(to_date, "%Y-%m-%d")
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        for result in results['statuses']:
            tweet_date = datetime.strptime(result['created_at'], "%a %b %d %H:%M:%S %z %Y").replace(tzinfo=None)
            if tweet_date < from_date:
                break
            tweet_text = result['text']
            tweets.append(tweet_text)
            
        return tweets


# In[113]:


# Usage: 
# loader = TweetLoader()
# loader.get_tweets("$AAPL", "2019-12-07", "2019-12-08", 10)

