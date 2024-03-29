
# coding: utf-8

# In[2]:


import os
import configparser
from datetime import datetime
import torch
from twython import Twython
import pandas as pd

from config import Config
from input_example import InputExample, BinaryClassificationProcessor
from input_features import InputFeatures, convert_example_to_feature


# In[3]:


# const
CRED_FNAME = 'credentials.txt'
MAX_SEQ_LENGTH = 48
OUTPUT_MODE = 'classification'


# In[12]:


class Twitter(object):
    
    def __init__(self, cred_dir = '../twitter-cred', cred_fname = CRED_FNAME):
        cred_fpath = os.path.join(cred_dir, cred_fname)
        self.global_config = Config()
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
                
            self._twitter = Twython(self._app_key, self._app_secret)
            self._tokenizer = torch.hub.load('huggingface/pytorch-transformers', 'tokenizer', 'bert-base-cased')
        else:
            raise ValueError(f"Failed to read credential file: {cred_fpath}")
            
    # query: search string
    # from_date: start date in "%Y-%m-%d"
    # to_date: end date in "%Y-%m-%d"
    # count: number of tweet to retrieve
    # return: list of InputExample
    def get_online_tweets(self, query, from_date, to_date, count=50):
        tweets = []
        results = self._twitter.search(q=query, until=to_date, count=count, lang='en')
        
        #to_date = datetime.strptime(to_date, "%Y-%m-%d")
        #from_date = datetime.strptime(from_date, "%Y-%m-%d")
        for i, result in enumerate(results['statuses']):
            tweet_date = datetime.strptime(result['created_at'], "%a %b %d %H:%M:%S %z %Y").replace(tzinfo=None)
            if tweet_date < from_date:
                break
                
            tweet_example = InputExample(i, result['text'], label=0) # set default label as 0
            tweets.append(tweet_example)
            
        return tweets
    
    def get_offline_tweets(self, filename, from_date, to_date):
        tweets = []
        
        #to_date = datetime.strptime(to_date, "%Y-%m-%d")
        #from_date = datetime.strptime(from_date, "%Y-%m-%d")
        data_dir = self.global_config.get_tsv_dir()
        
        tsv = pd.read_csv(os.path.join(data_dir, filename), sep=',')
        tsv["datetime"] = pd.to_datetime(tsv["date"])
        tar_df = tsv.loc[tsv["datetime"] >= from_date]
        tar_df = tar_df.loc[tsv["datetime"] <= to_date]
        results = tar_df['text'].tolist()
        
        for i, result in enumerate(results):
            tweet_example = InputExample(i, result, label=0)
            tweets.append(tweet_example)
            
        return tweets
    
    # tweets: list of InputExample
    def conv2features(self, tweets, max_seq_length = MAX_SEQ_LENGTH, output_mode = OUTPUT_MODE):
        examples_for_processing = [(example, 0, max_seq_length, self._tokenizer, output_mode) for example in tweets]
        examples_len = len(examples_for_processing)
        features = []
        
        for example in examples_for_processing:
            features.append(convert_example_to_feature(example))
            
        return features


# In[ ]:


def test_func():
    twitter = Twitter()
    examples = twitter.get_online_tweets("$APPL", "2019-12-08", "2019-12-09", 10)
    features = twitter.conv2features(examples)


# In[13]:


def test_func_2():
    twitter = Twitter()
    examples = twitter.get_offline_tweets("aapl.tsv", "2016-01-01", "2016-01-10")
    print(examples)


# In[14]:


# test_func_2()

