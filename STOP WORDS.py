import spacy
nlp=spacy.load('en_core_web_sm')
print(nlp.Defaults.stop_words)
print(len(nlp.Defaults.stop_words))
print(nlp.vocab['mystery'].is_stop)
print(nlp.vocab['even'].is_stop)
nlp.Defaults.stop_words.add('btw') #add stop word
nlp.vocab['btw'].is_stop=True #optional
print(nlp.vocab['btw'].is_stop)
print(len(nlp.Defaults.stop_words))
nlp.Defaults.stop_words.remove("show") # remove stop word
print(nlp.vocab['four'].is_stop)
print(len(nlp.Defaults.stop_words))
