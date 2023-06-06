import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Fred order a cup of hot tea")
for token in doc:
    print(token.text, token.pos_, token.dep_)