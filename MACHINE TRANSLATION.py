!pip install indic-nlp-library
!pip install indic-transliteration
from indicnlp.tokenize.indic_tokenize import trivial_tokenize
text = "VELS University एक बेहतरीन प्लेटफार्म है।"
tokens = trivial_tokenize(text)
detokenized_text = ' '.join(tokens)
print("Original Text:", text)
print("Tokens:", tokens)
print("De-tokenized Text:", detokenized_text)
from indicnlp.tokenize.sentence_tokenize import sentence_split
text = "ಇದು ಒಂದು ಉದಾಹರಣೆಯ ವಾಕ್ಯ. ಇದು ಮತ್ತೊಂದು ವಾಕ್ಯ."
sentences = sentence_split(text, lang='kn')
print("Original Text:", text)
print("Sentences:", sentences)
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
text = "ఇది ప్రముఖ కంప్యూటర్ సైన్స్ ప్లాట్‌ఫారమ్."
converted_text = UnicodeIndicTransliterator.transliterate(text, "te", "hi")
print("Original Text:", text)
print("Converted Text:", converted_text)
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
english_text = "This is a popular computer science platform."
tamil_text = transliterate(english_text, sanscript.ITRANS, sanscript.TAMIL)
print("Transliterated Text:", tamil_text)
