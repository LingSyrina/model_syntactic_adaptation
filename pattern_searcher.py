#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:48:07 2023

@author: leasyrin
"""
import pandas as pd
import sys

# Translate pattern to searchable pos, feature, and word
def pattern_translator(pattern):
    pattern = pattern.split()
    pos, word, feature, dep =[], [], [], []   
    for item in pattern:
        parts = item.split('>', 1) 
        dep.append(parts[1] if len(parts) == 2 else '')    
        parts = parts[0].split('-', 1)        
        feature.append(parts[1] if len(parts) == 2 else '')        
        parts = parts[0].split('|', 1)
        word.append(parts[1] if len(parts) == 2 else '')
        pos.append(parts[0])        
    return (pos, dep, feature, word)  

def match(corpus, a, b, pos, dep, feature, word): 
    return (pos[b] in corpus.iloc[a, 2] and feature[b] in corpus.iloc[a, 3] and word[b] in corpus.iloc[a, 1] and dep[b] in corpus.iloc[a, 6])

def pattern_searcher(path, pattern):      
    
    # Read in the txt file
    corpus = pd.read_table(path)
    
    # Translate pattern to searchable pos, feature, and word    
    pos, dep, feature, word = pattern_translator(pattern)
    
    # check for flexibility
    for i in range(len(pos)):
        if pos[i].isdigit():
            int_pos = int(pos[i])
            feature[i:i], dep[i:i], word[i:i] = [(int_pos - 1) * ['']] * 3
            # feature[i:i] = (int_pos-1) * ['']
            # dep[i:i] = (int_pos-1) * ['']
            # word[i:i] = (int_pos-1) * ['']
            pos.pop(i)
            pos[i:i] = int_pos * ['']

    # Perform the search and save the results
    with open(output_file_path, "a") as output_file:
        sys.stdout = output_file 
        print(f'Here are the expressions for {pattern}')    
        count = 0
        for i in range(corpus.shape[0]-len(pos)):
            if all(pos[f] in corpus.iloc[i + f, 2] for f in range(len(pos))) and \
                all(dep[f] in corpus.iloc[i + f, 6] for f in range(len(pos))) and \
                    all(feature[f] in corpus.iloc[i + f, 3] for f in range(len(pos))) and \
                        all(word[f] in corpus.iloc[i + f, 1] for f in range(len(pos))) and \
                            all(char.isalnum() for char in corpus.iloc[i:i+len(pos), 1]):
                                count += 1
                                values = [corpus.iat[n, 1] for n in range(i, i + len(pos))]
                                sent = [corpus.iat[n, 1] for n in range(i - 3, i + 6)]
                                print(' '.join(map(str, values)), '| in |', ' '.join(map(str, sent)))  
        
        print(f'We found {count} occurences in this {corpus.shape[0]}-word corpus ({path}).')
    
    # Reset standard output
    sys.stdout = sys.__stdout__

# allow flexibility of distance
if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: pattern_searcher.py input_file output_file_path pattern (format: POS>dep-feature|word)")
        sys.exit(1)
    
    # Get the command-line arguments
    path = sys.argv[1]
    output_file_path = sys.argv[2]
    pattern = str(sys.argv[3])
    
    # Call the function to process the Excel file
    pattern_searcher(path, pattern)

    
