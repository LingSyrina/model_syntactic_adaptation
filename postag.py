#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 09:25:21 2023

@author: leasyrin
"""

import stanza
import pandas as pd

import sys
import os
import openpyxl

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

folder_path = "./Author_data_book_corpus"

# os.environ['KMP_DUPLICATE_LIB_OK']='True'

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through the files
i = 0
for file in files:
    i+=1
    if file.endswith(".txt"):  # Check if the file is a .txt file
        file_path = os.path.join(folder_path, file)  # Get the full path to the file
        # Open and read the file, and perform your code here
        with open(file_path, 'r') as txt_file:
            file_contents = txt_file.read()
            doc = nlp(file_contents)
            
            # Create an empty list to store the data
            data = []
            # Iterate through the sentences and words in your document
            for sent in doc.sentences:
                for word in sent.words:
                    word_id = word.id
                    word_text = word.text
                    word_pos = word.xpos
                    word_feats = word.feats if word.feats else "_"
                    word_headid = word.head
                    word_head = sent.words[word.head-1].text if word.head > 0 else "root"
                    word_deprel = word.deprel
                    
                    data.append([word_id,word_text,word_pos, word_feats, word_headid, word_head,word_deprel])
            
            # Create a DataFrame from the data
            df = pd.DataFrame(data, columns=['ID', 'WORD', 'POS', 'FEATURE', 'HEAD ID', 'HEAD','DEPREL'])
            
            # Display the DataFrame
            directory = f'./Tagging/ragging_{i}.txt'
            df.to_csv(directory, sep='\t', index=False)
            
            