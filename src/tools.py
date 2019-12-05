
# coding: utf-8

# In[4]:


from __future__ import absolute_import, division, print_function

import csv
import os
import sys
import logging
import pandas as pd
from datetime import datetime


# In[2]:


logger = logging.getLogger()
csv.field_size_limit(2147483647) # Increase CSV reader's field limit incase we have long text.


# In[3]:


class InputExample(object):
    """A single training/test example for simple sequence classification."""

    def __init__(self, guid, text_a, text_b=None, label=None):
        """Constructs a InputExample.

        Args:
            guid: Unique id for the example.
            text_a: string. The untokenized text of the first sequence. For single
            sequence tasks, only this sequence must be specified.
            text_b: (Optional) string. The untokenized text of the second sequence.
            Only must be specified for sequence pair tasks.
            label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
        """
        self.guid = guid
        self.text_a = text_a
        self.text_b = text_b
        self.label = label


# In[6]:


class DataProcessor(object):
    """Base class for data converters for sequence classification data sets."""

    def get_train_examples(self):
        """Gets a collection of `InputExample`s for the train set."""
        raise NotImplementedError()

    def get_dev_examples(self):
        """Gets a collection of `InputExample`s for the dev set."""
        raise NotImplementedError()

    def get_labels(self):
        """Gets the list of labels for this data set."""
        raise NotImplementedError()


# In[7]:


class BinaryClassificationProcessor(DataProcessor):
    """Processor for binary classification dataset."""
    
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.name = ""
        self.breakpoint = datetime.now()
        self.train = None
        self.dev = None
        
    def set_dataset(self, name, breakpoint):
        self.name = name
        self.breakpoint = datetime.strptime(breakpoint, '%Y-%m-%d')
        tsv = pd.read_csv(os.path.join(self.data_dir, name), sep=',')
        self.train = tsv.loc[tsv['date'] < breakpoint]
        self.dev = tsv.loc[tsv['date'] >= breakpoint]

    def get_train_examples(self):
        """See base class."""
        return self._create_examples(self.train, "train")

    def get_dev_examples(self):
        """See base class."""
        return self._create_examples(self.dev, "dev")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, df, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for i, row in df.iterrows():
            guid = "%s-%s" % (set_type, i)
            text_a = row[4]
            label = row[2]
            examples.append(
                InputExample(guid=guid, text_a=text_a, text_b=None, label=label))
        return examples

