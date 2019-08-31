# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:02:00 2019

@author: Mr.Reliable
"""

#load the packages
import nltk
import string
import pandas as pd
import numpy as np
import re
import collections
from collections import Counter

def preprocess(text): 
    return re.findall('[a-zA-Z]+', text.lower()) 

def get_dict(words):
    """
    Get the dictionary via the training data
    """
    return {w for w in words if w in legal_word}


"""
def the edit distance
"""

def edit_0(word): 
    """
    Edit distance=0
    """
    return {word}

def edit_1(word):
    """
    Edit distance=1
    """
    def splits(word):
        return [(word[:i], word[i:]) for i in range(len(word)+1)]               
    pairs      = splits(word)
    deletes    = [a+b[1:]           for (a, b) in pairs if b]
    transposes = [a+b[1]+b[0]+b[2:] for (a, b) in pairs if len(b) > 1]
    replaces   = [a+c+b[1:]         for (a, b) in pairs for c in letters if b]
    inserts    = [a+c+b             for (a, b) in pairs for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edit_2(word):
    """
    Edit distance=2
    """
    return {e2 for e1 in edit_1(word) for e2 in edit_1(e1)}
   
    

"""
def the spelling correction process
"""
   
def correct(word):
    """
    After generating the candidate words, we should return the max possible word
    """
    candidates =  (get_dict(edit_0(word)) or get_dict(edit_1(word)) or get_dict(edit_2(word)) or {word})
    return max(candidates, key=legal_word.get)

def correct_match(match):    
    word = match.group()
    def case_of(text):
        """
        We handle the letters upper or lower via this function
        """
        return (str.upper if text.isupper() else str.lower if text.islower() else str.title if text.istitle() else str)
    return case_of(word)(correct(word.lower()))
    
def correct_text_generic(text):
    return re.sub('[a-zA-Z]+', correct_match, text)


def correct_spell_error(data):
    for i in range(len(data)):
        temp=nltk.word_tokenize(data[i])
        count=0
        for j in range(len(temp)):
            if not(vocab[(vocab[0]==temp[j])].index.tolist()):
                temp[j]=correct_text_generic(temp[j])
                count=count+1
        data[i]=temp
    return data

def get_result(word):
    words=[]
    for i in range(1000):
        pinjie = ' '.join(word[i])
        words.append(pinjie)
    words=pd.DataFrame(words)  
    words.columns=["sentence"]
    words =words.reindex(columns=['id', 'sentence'],fill_value=1)
    words["id"]=test["id"]
    words=words.values.tolist()
    np.savetxt("C:/Users/Mr.Reliable/Desktop/result0.txt",words,delimiter='\t',fmt = '%s')





"""
Do the experiments
"""
#load the dataset
from nltk.corpus import reuters

#choose the datasets you want
text = preprocess(reuters.raw(categories=['acq','alum','barley','bop','carcass''castor-oil','cocoa','coconut',
                            'coconut-oil','coffee','copper','copra-cake','corn','cotton','cotton-oil',
                           'cpi','cpu','crude','dfl','dlr','dmk','earn','fuel','gas','gnp','gold','grain','groundnut',
                            'groundnut-oil','heat','hog','housing','income','instal-debt','interest','ipi','iron-steel']))
legal_word = collections.Counter(text)
letters = 'abcdefghijklmnopqrstuvwxyz' #get the letters


vocab=pd.read_table(r'C:\Users\Mr.Reliable\Desktop\vocab.txt',header=None,encoding='gb2312',delimiter="\t")
test=pd.read_table(r'C:\Users\Mr.Reliable\Desktop\testdata.txt',header=None,encoding='gb2312',delimiter="\t")
test.columns=["id","#","sentence"]
word=test["sentence"].tolist()

word=correct_spell_error(word)
get_result(word)