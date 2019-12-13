# Group infos

ENGG5108 course project

* Group 12

* Name: ωετhεbεsτ

* Members:
  * WONG Tsz Fung
  * XIA Xin
  * HUANG Ruiyang
  * WU Mengyang

## Plan

1. Use datasets for training (https://github.com/ivangundampc/stocknet-dataset), since Twitter API only allow retrieving tweets from last 7 days
2. Pre-processing
   1. Merging price data and tweets with correct time range (data_to_tsv.ipynb)
   2. Other pre-processing ? (Manual labelling of tweets, remove unwanted symbols)
   3. Prepare tweet data for BERT fine-tune (converter.py)
   4. May write a MapReduce program to do one of the task above to fulfill the project requirement
3. BERT fine-tuning for stock market related tweets
6. Twython streaming data for future prediction
5. Automatic script for getting new twitter data and perform prediction

## Files

* data/
  * feature/: converted feature file for BERT training
  * tsv/: pre-processed tweet csv for specific stocks
  * price/: price data for specific stocks
  * tweet/: related tweets for specific stocks
  
* output/: fine-tune weight files ([download here](https://drive.google.com/file/d/1i37uI8FsnQX62vuyQt9gRLD8cqzHJ92s/view?usp=sharing))

* doc/: documents

* src/
  
  * Common files
    * config.py: class for storing common configs
    * input_example.py: InputExample class and related functions
    * input_features.py: InputFeatures class and related functions
  * Twitter data loader
    * twitter-cred/: credential files of accessing Twitter API
    * twitter.ipynb: Twitter data loader (notebook version)
    * twitter.py: Twitter data loader
  
  * Training system
    * data_to_tsv.ipynb: Pre-processor (only notebook provided)
    * converter.py: Converter
    * trainer.ipynb: Trainer (only notebook provided)
  * Predictor
    * predictor.ipynb: Predictor (only notebook provided)
  * Web visualization
    * vision_new.html: read **result.js** (generated from predictor) and generates prediction chart

## Work distribution

* Mengyang: Proposal, Training system, Model fine-tuning, Final report, PowerPoint
* Tsz Fung: Proposal, Training system, Twitter data loader, Predictor, Final report, PowerPoint, Video
* Ruiyang: Proposal, Pre-processor, Web visualization, Final report, PowerPoint
* Xia xin: Proposal, Project status report, Final report, PowerPoint

## Twitter

* Account
  * email: wethebestcuhk@protonmail.com
  * password: engg5108project
* API key and Twitter API usage: https://medium.com/@cyeninesky3/%E4%BD%BF%E7%94%A8-nltk-%E6%90%AD%E9%85%8D-twitter-api-%E6%8B%BF%E5%8F%96%E7%A4%BE%E7%BE%A4%E8%B3%87%E6%96%99-%E4%BB%A5%E5%B7%9D%E6%99%AE%E7%9A%84-twitter%E8%B3%87%E6%96%99%E7%82%BA%E4%BE%8B-2bd493f452a6
* Stock price + related tweets dataset: https://github.com/ivangundampc/stocknet-dataset
* Sentiment 140 (tweets with sentiment classification) dataset: https://www.kaggle.com/kazanova/sentiment140

## Reference

* A Simple Guide On Using BERT for Binary Text Classification **(we mainly followed this guide)**: https://medium.com/swlh/a-simple-guide-on-using-bert-for-text-classification-bbf041ac8d04
* Using the latest advancements in AI to predict stock market movements: https://github.com/borisbanushev/stockpredictionai
* 進擊的 BERT：NLP 界的巨人之力與遷移學習: https://leemeng.tw/attack_on_bert_transfer_learning_in_nlp.html
* BERT fine tuning: https://mccormickml.com/2019/07/22/BERT-fine-tuning/
* 两行代码玩转Google BERT句向量词向量: https://zhuanlan.zhihu.com/p/50582974
* BERT fine-tune 实践终极教程: https://www.jiqizhixin.com/articles/2018-11-23-15
* 5 分钟入门 Google 最强NLP模型：BERT: https://www.jianshu.com/p/d110d0c13063
* 【NLP】Google BERT详解: https://zhuanlan.zhihu.com/p/46652512
* The Transformer – Attention is all you need: https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/#.XE_kC1xKiUk