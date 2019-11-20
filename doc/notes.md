# Plan

1. Use given datasets for training, since Twitter API only allow retrieving tweets from last 7 days

2. Processing
   1. Merging price data and tweets with correct time range
   2. Calculating market-sentiment data for modeling as well, such as EMA, MACD
   3. Prepare tweet data for BERT fine-tune
   4. May write a MapReduce program to do one of the task above to fulfill the project requirement

3. BERT fine-tuning for stock market related tweets

4. Use GANs for predicting stock prices
5. matlpotlib for visualization (we may not have time to make a web interface)
6. nltk.twitter streaming data for future prediction

# Preprocess

## Twitter

* Account
  * email: wethebestcuhk@protonmail.com
  * password: engg5108project
* API key and Twitter API usage: https://medium.com/@cyeninesky3/%E4%BD%BF%E7%94%A8-nltk-%E6%90%AD%E9%85%8D-twitter-api-%E6%8B%BF%E5%8F%96%E7%A4%BE%E7%BE%A4%E8%B3%87%E6%96%99-%E4%BB%A5%E5%B7%9D%E6%99%AE%E7%9A%84-twitter%E8%B3%87%E6%96%99%E7%82%BA%E4%BE%8B-2bd493f452a6
* Stock price + related tweets dataset: https://github.com/ivangundampc/stocknet-dataset
* Sentiment 140 (tweets with sentiment classification) dataset: https://www.kaggle.com/kazanova/sentiment140

# Model

## Useful links

* Using the latest advancements in AI to predict stock market movements: https://github.com/borisbanushev/stockpredictionai **(very useful, read this first)**

* 進擊的 BERT：NLP 界的巨人之力與遷移學習: https://leemeng.tw/attack_on_bert_transfer_learning_in_nlp.html
* BERT fine tuning: https://mccormickml.com/2019/07/22/BERT-fine-tuning/
* 两行代码玩转Google BERT句向量词向量: https://zhuanlan.zhihu.com/p/50582974
* BERT fine-tune 实践终极教程: https://www.jiqizhixin.com/articles/2018-11-23-15
* 5 分钟入门 Google 最强NLP模型：BERT: https://www.jianshu.com/p/d110d0c13063

* 【NLP】Google BERT详解: https://zhuanlan.zhihu.com/p/46652512

* The Transformer – Attention is all you need: https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/#.XE_kC1xKiUk