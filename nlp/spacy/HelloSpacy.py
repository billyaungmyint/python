import spacy
from beautifultable import BeautifulTable

nlp = spacy.load('en_core_web_sm')
text = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(text)

table = BeautifulTable()
table.columns.header = ['text', 'POS', 'TAG', 'Dep', 'Shape', 'is_alpha', 'is_stop']

for token in doc:
    table.rows.append([token.text , token.pos_ , token.tag_ , token.dep_ , token.shape_ , token.is_alpha , token.is_stop])

print(table)
