import nltk
from nltk.tokenize import PunktSentenceTokenizer

class POSGenerator(object):
    def __init__(self, method='nltk'):
        self.method = method

    def process_content(self, tokenized_text):
        try:
            for line in tokenized_text:
                words = nltk.word_tokenize(line)
                tagged = nltk.pos_tag(words)
                print(tagged)
        except Exception as e:
            print(e)

if __name__ =="__main__":
    sample_text = "I ate fish for lunch"
    punktok = PunktSentenceTokenizer()
    tokenized = punktok.tokenize(text=sample_text)
    POSGenerator = POSGenerator(method='nltk')
    POSGenerator.process_content(tokenized_text = tokenized)
