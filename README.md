 # Search guide

## Tools

**postag.py**: employ stanza package for multiple corpus annotation (with dependency)

**paternn_searcher.py**: search through annotated corpus with a given search pattern. Search pattern format: POS>dependency-feature|word. All parameters are free. Numbers can be specified for words skipped in a search (e.g., >nsubj 1 VB-Past）

**POS tagging** (https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

**dependency** (https://universaldependencies.org/u/dep/index.html)

**features** (https://universaldependencies.org/u/feat/index.html)

## Sample run (with bash) 

    -python pattern_searcher.py 'sample.txt' '/Users/search/result.txt' 'WP>nsubj 1 VB-Past'

## Searches 

### RC

1. all RC

   'WP>nsubj'
   
2. RC with who/whom/whose

   'WP>nsubj|who'
   
3. RC with which/that

   'WP>nsubj|which'
   'WP>nsubj|that'
   
5. RC with where/when/why

   'WRB-PronType=Rel' 
   
6. Passive RC

    'WP>nsubj|wh VB-Past'

### Passive

   '-Pass'

### Funtion words frequency



