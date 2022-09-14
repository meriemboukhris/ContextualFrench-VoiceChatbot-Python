import nltk 
import numpy as np
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer= PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())
    
def bag_of_words(tokenized_sentence, all_words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag= np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentence_word:
            bag[idx]=1
    return bag

