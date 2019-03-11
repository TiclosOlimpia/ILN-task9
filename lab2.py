import nltk

f = open("UMBC_tokenized.txt", "r")

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
nltk.download('maxent_ne_chunker')
nltk.download('treebank')


str = f.readline()

while str:
    tokens = nltk.word_tokenize(str)

    tagged = nltk.pos_tag(tokens)

    entities = nltk.chunk.ne_chunk(tagged)

    print(tokens)
    print(tagged)
    print(entities)

    str = f.readline()

'''
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0002.mrg')[0]
t.draw()
'''