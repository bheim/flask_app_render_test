from flask import Flask
import pandas as pd
import numpy as np
import pickle
from gensim.models.word2vec import Word2Vec
import gensim.downloader as api

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


with open('mt_predict.pkl', 'rb') as file:
    mt_predict = pickle.load(file)

corpus = api.load('text8')
model = Word2Vec(corpus)


vocab = list(model.wv.index_to_key)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
