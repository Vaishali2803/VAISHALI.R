import spacy
from spacy import displacy
from IPython.core.display import display
nlp=spacy.load('en_core_web_sm')
d=nlp(u"The quick brown fox jumped over the lazy dog's back")
html=displacy.render(d,style='dep',page=True)
options={'distance':110,'compact':'True','color':'yellow','bg':'black','font':'Times'}
html=displacy.render(d,style='dep',options=options)
