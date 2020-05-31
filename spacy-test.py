import sys
import spacy

text = sys.argv[1]

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
for d in doc:
    print((d.text, d.pos_, d.dep_))
