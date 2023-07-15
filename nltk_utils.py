import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

a = "magical places of the universe"
print("Original Sentence : \n", a)

a = tokenize(a)
print("Tokenized sentence : \n",a)

stemmed = [stem(x) for x in a]
print("stemmetized sentence : \n",stemmed)



