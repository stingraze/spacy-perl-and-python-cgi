import sys
#Scratch idea brainstorm for AI-ish function using spacy. (C) Tsubasa Kato 2020/6/18 1:25AM JST
import spacy
import re
#Gets Input from argv[1]
text = sys.argv[1]

nlp = spacy.load('en_core_web_sm')
def understand(input_to_understand):
	print(extract_keywords(input_to_understand))

def extract_keywords(input_to_parse):
	#list for keeping top 3 words that is "subj"
	top_2_words = []

	top_2_words_counter = 0
	
	subj_list = []
	pos_list = []
	doc = nlp(input_to_parse)
	for d in doc:
	#print((d.text, d.pos_, d.dep_))
		word = d.text
		pos = d.pos_
		dep = d.dep_
#If it matches subject, append word
		if re.search(r'subj', dep):
			subj_list.append(word)
#If it matches noun, append word
		if re.search(r'NOUN',pos):
			pos_list.append(word)

	for noun in pos_list:
		print ("NOUN_list")
		print (noun)

	print("###########################################")

	for subj in subj_list:
		print ("SUBJ_list")
		print (subj)

		if(top_2_words_counter < 2):
			top_2_words.append(subj)
			top_2_words_counter = top_2_words_counter + 1	
	if(len(top_2_words) >= 2):
		return top_2_words[0], top_2_words[1]
	if(len(top_2_words) <= 1):
		return "not enough to list top 2"


understand(text)