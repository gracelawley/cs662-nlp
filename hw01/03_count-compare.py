# Part 3: Counting and comparing

from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

# read in corpus
with open("tokenized.txt", "r") as f:
	corpus = f.read()
f.close()


# count number of unigram tokens
tokens = corpus.split()
print("n tokens:", len(tokens))


# count number of unique types
types = set(tokens)
print("n types:", len(types))


# create a rank-frequency plot
token_freq = Counter(tokens)

plt.loglog([val for word, val in token_freq.most_common()])
plt.xlabel("rank (log scale)")
plt.ylabel("frequency (log scale)")
plt.title("Rank-Frequency Plot")
#plt.show()


# top twenty most common words
print(token_freq.most_common(20))


# type/token counts after removing stopwords
stop_words = set(stopwords.words("english"))
stop_words = [w.upper() for w in stop_words] # change to uppercase


tokens_fil = [t for t in tokens if t not in stop_words]
print("n filtered tokens:", len(tokens_fil))

types_fil = set(tokens_fil)
print("n filtered types:", len(types_fil))


# top twenty most common words after removing stopwords
token_fil_freq = Counter(tokens_fil)
print(token_fil_freq.most_common(20))







