import os

# Root path of data directory
DATA_DIR_PATH = '../data/'

# Data file directory name
TSV_DIR_NAME = 'tsv'
FEATURE_DIR_NAME = 'feature'
TWEET_DIR_NAME = 'tweet'
PRICE_DIR_NAME = 'price'

# The output directory where the fine-tuned model and checkpoints will be written.
OUTPUT_DIR_PATH = '../output/'

# The directory where the evaluation reports will be written to.
REPORTS_DIR_PATH = '../reports/'

# This is where BERT will look for pre-trained models to load parameters from.
CACHE_DIR_PATH = '../cache/'

class Config(object):
    
    def __init__(self):
        self._data_dir = DATA_DIR_PATH
        self._output_dir = OUTPUT_DIR_PATH
        self._reports_dir = REPORTS_DIR_PATH
        self._cache_dir = CACHE_DIR_PATH
        
        self._tsv_dir = os.path.join(self._data_dir, TSV_DIR_NAME)
        self._feature_dir = os.path.join(self._data_dir, FEATURE_DIR_NAME)
        self._tweet_dir = os.path.join(self._data_dir, TWEET_DIR_NAME)
        self._price_dir = os.path.join(self._data_dir, PRICE_DIR_NAME)
        
    def get_data_dir(self):
        return self._data_dir
    
    def get_output_dir(self):
        return self._output_dir
    
    def get_reports_dir(self):
        return self._reports_dir
    
    def get_cache_dir(self):
        return self._cache_dir
    
    def get_tsv_dir(self):
        return self._tsv_dir
    
    def get_featur_dir(self):
        return self._feature_dir
    
    def get_tweet_dir(self):
        return self._feature_dir
    
    def get_price_dir(self):
        return self._price_dir