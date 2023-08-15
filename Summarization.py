import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

text = input("Insert text here:")

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
words = [word for word in words if word.lower() not in stop_words]

sentences = sent_tokenize(text)

word_freq = {}
for word in words:
    if word in word:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

sent_score = {}

for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq.keys():
            if len(sentence.split()) < 30:
                if sentence not in sent_score.keys():
                    sent_score[sentence] = word_freq[word]
                else:
                    sent_score[sentence] += word_freq[word]

summary_sentences = nlargest(3, sent_score, key=sent_score.get)
summary = '\n'.join(summary_sentences)
print(summary)