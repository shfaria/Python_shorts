# import nltk
# nltk.download("stopwords")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords



testString = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""
sentenceChunks = sent_tokenize(testString)
wordChunks = word_tokenize(testString)
stop_words = set(stopwords.words("english"))
# print(stop_words)
finalwords = []
for word in wordChunks:
    if word.casefold() not in stop_words:
        finalwords.append(word)
print(finalwords) 