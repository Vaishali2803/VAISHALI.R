import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
def dw(sent,aw):
    t=word_tokenize(sent)
    sense=lesk(t,aw,'n')
    return sense
sent=[
    'He went to the bank to withdraw money',
    'she sat on the river bank to enjoy the view']
aw='bank'
for s in sent:
    sense=dw(s,aw)
    if sense:
        print(s)
        print("Disambiguated sense:",sense.name())
        print(sense.definition())
    else:
        print("no sense found")

