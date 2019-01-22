# Part 2: Structuring the data

# called with python 02_structure-data.py > tokenized.txt

from nltk.tokenize import sent_tokenize, word_tokenize
import string


f = open("deserialized.txt", "r")
raw = f.read()


# split raw text into sentences
text = sent_tokenize(raw)


# reformat to one-line-per-sentence
sentences = [x.replace("\n", " ") for x in text]


# tokenize by words
tokens = [word_tokenize(x) for x in sentences]

# change to upper case
tokens = [[t.upper() for t in l] for l in tokens]



# remove tokens that are solely punctuation
punct_set = set(string.punctuation)
tokens = [[t for t in tokens if t not in punct_set] for tokens in tokens] # 1 case
tokens = [[t for t in tokens if not(all(c in punct_set for c in t))] for tokens in tokens] # 2+ case



# formatting for output .txt
tokens = [" ".join(l) for l in tokens] # add spaces between tokens
tokens = "\n".join(tokens) # add \n between lines

print(tokens)





