#(C)Inspire Search 2020/5/31 Coded by Tsubasa Kato (@_stingraze)
#Last edited on 2020/6/1 11:36AM JST
import sys
import spacy
import re
#gets query from argv[1]
text = sys.argv[1]

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)

ahref = "<a href=\""
ahref2 = "\"\>"

#arrays for storing subject and object types 
subj_array = []
obj_array = []

for d in doc:
	#print((d.text, d.pos_, d.dep_))
	word = d.text
	pos = d.pos_
	dep = d.dep_
#If it matches subject, do this
	if re.search(r'subj', dep):
		
		word2 = ahref + 'http://www.superai.online/solr/search.php?query='+ word + ahref2 + word + '</a>'
		subj_array.append(word)
		print (word2)
		print (pos)
		print (dep)

#If it matches object, do this
	if re.search(r'obj', dep):
		word2 = ahref + 'http://www.superai.online/solr/search.php?query='+ word + ahref2 + word + '</a>'
		obj_array.append(word)
		print (word2)
		print (pos)
		print (dep)


#Sorts both arrays
#ToDo & Note to self: 
#Study more of sorting so I can visualize this as table etc.
subj_array.sort()
obj_array.sort()
for subj in subj_array:
		print (subj)

for obj in obj_array:
		print (obj)



