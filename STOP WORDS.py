import spacy
nlp=spacy.load('en_core_web_sm')
d=nlp(u"I am a runner running in a race because I love to run since I ran today")
for t in d:
    print(t.text,t.pos_,t.lemma,t.lemma_)

def show_lemma(text):
    for t in  text:
        print(t.text,t.pos_,t.lemma,t.lemma_)
show_lemma(d)
