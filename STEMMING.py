import nltk
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
p_stemmer=PorterStemmer()
words=['run','runner','running','ran','runs','easily','fairly']
for s in words:
    print(s, p_stemmer.stem(s))
s_stemmer=SnowballStemmer(language='english')
for s in words:
    print(s,s_stemmer.stem(s))
dict='consolingly'
print( p_stemmer.stem(dict))
print( s_stemmer.stem(dict))
phrase='I am meeting him tommorow at the meeting'
for w in phrase.split():
    print(w ,p_stemmer.stem(w))
