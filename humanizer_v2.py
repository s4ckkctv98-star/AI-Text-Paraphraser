import random
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return list(set(synonyms))

def synonym_replace(text):
    words = text.split()
    new_words = []

    for w in words:
        syns = get_synonyms(w)
        if syns and random.random() > 0.7:
            new_words.append(random.choice(syns))
        else:
            new_words.append(w)

    return " ".join(new_words)


def sentence_variation(text):
    sentences = text.split(".")
    random.shuffle(sentences)
    return ". ".join(sentences)


def add_human_noise(text):
    fillers = [
        "to be honest",
        "kind of",
        "in a way",
        "I mean",
        "actually"
    ]
    sentences = text.split(".")
    for i in range(len(sentences)):
        if random.random() > 0.6:
            sentences[i] += ", " + random.choice(fillers)
    return ". ".join(sentences)


def humanize_advanced(text):
    text = synonym_replace(text)
    text = sentence_variation(text)
    text = add_human_noise(text)
    return text
