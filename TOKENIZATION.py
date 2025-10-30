import spacy
nlp=spacy.load('en_core_web_sm')
doc=nlp(u"Tesla is looking at buying U.S. startup for $6 million. Hi I am Happy")
for token in doc:
    print(token.text,token.pos_,token.dep_)
print(nlp.pipeline)
print(nlp.pipe_names)
print(doc[0])
print(doc)
print(type(doc))
spacy.explain(' nsubj')
print(doc[4].lemma_)
spacy.explain(doc[4].tag_)
print(doc[7].text , doc[7].shape_)
print(doc[4].is_alpha)
print(doc[2].is_stop)
for sent in doc.sents:
    print(sent)
print(doc[0].is_sent_start)