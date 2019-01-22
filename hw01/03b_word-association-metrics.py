# Part 3: Counting and Comparing
## Word association metrics

from collections import Counter
from nltk.util import ngrams
from math import log
import csv


# read in corpus
with open("tokenized.txt", "r") as f:
	corpus = f.read()
f.close()



# calculate unigram probabilities
unigrams = corpus.split()
unigram_freq = Counter(unigrams)

unigram_prob = {}
for x in unigrams:
	unigram_prob[x] = unigram_freq[x] / len(unigrams)


# calculate bigram probabilities
bigrams = ngrams(unigrams, 2)
bigram_freq = Counter(bigrams)

bigram_prob = {}
for y in bigram_freq.keys():
	bigram_prob[y] = bigram_freq[y] / len(bigram_freq.keys())


# compute PMI values for each bigram
pmi_bigrams = {}
for w1, w2 in bigram_prob.keys():
	pmi_bigrams[(w1, w2)] = log(bigram_prob[w1, w2] / (unigram_prob[w1] * unigram_prob[w2]))
pmi = Counter(pmi_bigrams)


with open("pt3_0.csv", "w") as csv_file: 
	col_names = ["(w1,w2)", "pmi", "p(w1,w2)", "p(w1)", "p(w2)"]
	writer = csv.DictWriter(csv_file, fieldnames = col_names)

	writer.writeheader()

	for bigram, p in pmi.most_common(30):
		writer.writerow({"(w1,w2)": bigram, "pmi": p,
						 "p(w1,w2)": bigram_prob[bigram],
						 "p(w1)": unigram_prob[bigram[0]],
						 "p(w2)": unigram_prob[bigram[1]]})




# Threshhold of 20
bigram_prob_20 = {}
for y in bigram_freq.keys():
	if bigram_freq[y] > 20:
		bigram_prob_20[y] = bigram_freq[y] / len(bigram_freq.keys())


pmi_bigrams_20 = {}
for w1, w2 in bigram_prob_20.keys():
	pmi_bigrams_20[(w1, w2)] = log(bigram_prob_20[w1, w2] / (unigram_prob[w1] * unigram_prob[w2]))
pmi_20 = Counter(pmi_bigrams_20)


with open("pt3_20.csv", "w") as csv_file: 
	col_names = ["(w1,w2)", "pmi", "p(w1,w2)", "p(w1)", "p(w2)"]
	writer = csv.DictWriter(csv_file, fieldnames = col_names)

	writer.writeheader()

	for bigram, p in pmi_20.most_common(30):
		writer.writerow({"(w1,w2)": bigram, "pmi": p,
						 "p(w1,w2)": bigram_prob[bigram],
						 "p(w1)": unigram_prob[bigram[0]],
						 "p(w2)": unigram_prob[bigram[1]]})



# Threshhold of 60
bigram_prob_60 = {}
for y in bigram_freq.keys():
	if bigram_freq[y] > 60:
		bigram_prob_60[y] = bigram_freq[y] / len(bigram_freq.keys())


pmi_bigrams_60 = {}
for w1, w2 in bigram_prob_60.keys():
	pmi_bigrams_60[(w1, w2)] = log(bigram_prob_60[w1, w2] / (unigram_prob[w1] * unigram_prob[w2]))
pmi_60 = Counter(pmi_bigrams_60)


with open("pt3_60.csv", "w") as csv_file: 
	col_names = ["(w1,w2)", "pmi", "p(w1,w2)", "p(w1)", "p(w2)"]
	writer = csv.DictWriter(csv_file, fieldnames = col_names)

	writer.writeheader()

	for bigram, p in pmi_60.most_common(30):
		writer.writerow({"(w1,w2)": bigram, "pmi": p,
						 "p(w1,w2)": bigram_prob[bigram],
						 "p(w1)": unigram_prob[bigram[0]],
						 "p(w2)": unigram_prob[bigram[1]]})





# Threshhold of 100
bigram_prob_100 = {}
for y in bigram_freq.keys():
	if bigram_freq[y] > 100:
		bigram_prob_100[y] = bigram_freq[y] / len(bigram_freq.keys())


pmi_bigrams_100 = {}
for w1, w2 in bigram_prob_100.keys():
	pmi_bigrams_100[(w1, w2)] = log(bigram_prob_100[w1, w2] / (unigram_prob[w1] * unigram_prob[w2]))
pmi_100 = Counter(pmi_bigrams_100)


with open("pt3_100.csv", "w") as csv_file: 
	col_names = ["(w1,w2)", "pmi", "p(w1,w2)", "p(w1)", "p(w2)"]
	writer = csv.DictWriter(csv_file, fieldnames = col_names)

	writer.writeheader()

	for bigram, p in pmi_100.most_common(30):
		writer.writerow({"(w1,w2)": bigram, "pmi": p,
						 "p(w1,w2)": bigram_prob[bigram],
						 "p(w1)": unigram_prob[bigram[0]],
						 "p(w2)": unigram_prob[bigram[1]]})




# Threshhold of 200
bigram_prob_200 = {}
for y in bigram_freq.keys():
	if bigram_freq[y] > 200:
		bigram_prob_200[y] = bigram_freq[y] / len(bigram_freq.keys())


pmi_bigrams_200 = {}
for w1, w2 in bigram_prob_200.keys():
	pmi_bigrams_200[(w1, w2)] = log(bigram_prob_200[w1, w2] / (unigram_prob[w1] * unigram_prob[w2]))
pmi_200 = Counter(pmi_bigrams_200)


with open("pt3_200.csv", "w") as csv_file: 
	col_names = ["(w1,w2)", "pmi", "p(w1,w2)", "p(w1)", "p(w2)"]
	writer = csv.DictWriter(csv_file, fieldnames = col_names)

	writer.writeheader()

	for bigram, p in pmi_200.most_common(30):
		writer.writerow({"(w1,w2)": bigram, "pmi": p,
						 "p(w1,w2)": bigram_prob[bigram],
						 "p(w1)": unigram_prob[bigram[0]],
						 "p(w2)": unigram_prob[bigram[1]]})



print("(NEW, YORK), no threshold")
print(pmi[("NEW", "YORK")])
print(bigram_prob[("NEW", "YORK")])
print(unigram_prob["NEW"])
print(unigram_prob["YORK"])

print("(NEW, YORK), threshold of 100")
print(pmi_100[("NEW", "YORK")])
print(bigram_prob_100[("NEW", "YORK")])
print(unigram_prob["NEW"])
print(unigram_prob["YORK"])





