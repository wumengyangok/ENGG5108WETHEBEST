'''
If you are having trouble multiprocessing inside Notebooks, give this script a shot.
'''

import os
import torch
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import pickle

# locals
from config import Config
from input_example import InputExample, BinaryClassificationProcessor
from input_features import InputFeatures, convert_example_to_feature

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
logging.basicConfig(level=logging.INFO)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# The input data dir. Should contain the .tsv files (or other data files) for the task.
DATA_DIR = "../data/tsv"

# Bert pre-trained model selected in the list: bert-base-uncased,
# bert-large-uncased, bert-base-cased, bert-large-cased, bert-base-multilingual-uncased,
# bert-base-multilingual-cased, bert-base-chinese.
BERT_MODEL = 'bert-base-cased'

# The output directory where the model predictions and checkpoints will be written.
OUTPUT_DIR = '../data/feature/'

CACHE_DIR = '../cache/'

# The maximum total input sequence length after WordPiece tokenization.
# Sequences longer than this will be truncated, and sequences shorter than this will be padded.
MAX_SEQ_LENGTH = 48

TRAIN_BATCH_SIZE = 24
EVAL_BATCH_SIZE = 8
LEARNING_RATE = 2e-5
NUM_TRAIN_EPOCHS = 1
RANDOM_SEED = 42
GRADIENT_ACCUMULATION_STEPS = 1
WARMUP_PROPORTION = 0.1
OUTPUT_MODE = 'classification'

CONFIG_NAME = "config.json"
WEIGHTS_NAME = "pytorch_model.bin"

output_mode = OUTPUT_MODE

# Load pre-trained model tokenizer (vocabulary)
tokenizer = torch.hub.load('huggingface/pytorch-transformers', 'tokenizer', 'bert-base-cased')    # Download vocabulary from S3 and cache.
# tokenizer = BertTokenizer.from_pretrained('bert-base-cased', do_lower_case=False)

processor = BinaryClassificationProcessor(DATA_DIR)
processor.set_dataset("aapl.tsv", "2015-12-31")
train_examples = processor.get_train_examples()
train_examples_len = len(train_examples)

label_list = processor.get_labels() # [0, 1] for binary classification
num_labels = len(label_list)

label_map = {label: i for i, label in enumerate(label_list)}
train_examples_for_processing = [(example, label_map, MAX_SEQ_LENGTH, tokenizer, output_mode) for example in train_examples]

process_count = cpu_count() - 2
if __name__ == '__main__':
    print('Preparing to convert {train_examples_len} examples..')
    print('Spawning {process_count} processes..')
    with Pool(process_count) as p:
        train_features = list(tqdm(p.imap(convert_example_to_feature, train_examples_for_processing), total=train_examples_len))

    with open(os.path.join(OUTPUT_DIR, "aapl.pkl"), 'wb') as f:
        pickle.dump(train_features, f) 
