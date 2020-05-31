#(C)Inspire Search 2020/5/31 Coded by Tsubasa Kato (@_stingraze)
import sys
import spacy
import re

text = sys.argv[1]

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

ahref = "<a href=\""
ahref2 = "\"\>"
for d in doc:
	#print((d.text, d.pos_, d.dep_))
	word = d.text
	pos = d.pos_
	dep = d.dep_
#If it matches subject, do this
	if re.search(r'subj', dep):
		
		word2 = ahref + 'http://www.superai.online/solr/search.php?query='+ word + ahref2 + word + '</a>'
		print (word2)
		print (pos)
		print (dep)
#If it matches object, do this
	if re.search(r'obj', dep):
		word2 = ahref + 'http://www.superai.online/solr/search.php?query='+ word + ahref2 + word + '</a>'
		print (word2)
		print (pos)
		print (dep)
