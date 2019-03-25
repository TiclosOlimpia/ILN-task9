import nltk
from nltk.corpus import wordnet as wn

file = open("D:\\nltk_data\\corpora\\UMBC_tokenized.txt", "r")

str1 = file.readline()
#str2 = file.readline()
#str3 = file.readline()

dictionary = {}

#while str1:
tokens = nltk.word_tokenize(str1)

for i in range(0,len(tokens)):
    dictionary[tokens[i]] = 0

    #str1 = file.readline()

print( dictionary)

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)

    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)

    return tfDict

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)

    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))

print(computeTF(dictionary, "To"))



def simplified_lesk(word,sentence) #returns best sense of word
    best-sense = most frequent sense for word
    max-overlap = 0
    context = set of words in sentence
    for each sense in senses of word:
        signature = set of words in the gloss and examples of sense
        overlap = COMPUTEOVERLAP (signature,context)
    if overlap > max-overlap:
        max-overlap = overlap
        best-sense = sense
    return (best-sense)

