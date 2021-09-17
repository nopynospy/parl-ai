from __future__ import unicode_literals, print_function
import spacy
from spacy.attrs import ORTH, LEMMA, NORM, TAG

nlp = spacy.load('en_core_web_sm')

'''
dealing with contractions by expanding spaCy's tokenizer exceptions
ORTH is the form in the text/corpus
LEMMA is the dictionary form
TAG is part of speech
'''
TOKENIZER_EXCEPTIONS = {
# do
    "don't": [
        {ORTH: "do", LEMMA: "do"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
    "doesn't": [
        {ORTH: "does", LEMMA: "do"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
    "didn't": [
        {ORTH: "did", LEMMA: "do"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
# can
    "can't": [
        {ORTH: "ca", LEMMA: "can"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
    "couldn't": [
        {ORTH: "could", LEMMA: "can"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
# have
    "I've'": [
        {ORTH: "I", LEMMA: "I"},
        {ORTH: "'ve'", LEMMA: "have", NORM: "have", TAG: "VERB"}],
    "haven't": [
        {ORTH: "have", LEMMA: "have"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
    "hasn't": [
        {ORTH: "has", LEMMA: "have"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
    "hadn't": [
        {ORTH: "had", LEMMA: "have"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
# will/shall will be replaced by will
    "I'll'": [
        {ORTH: "I", LEMMA: "I"},
        {ORTH: "'ll'", LEMMA: "will", NORM: "will", TAG: "VERB"}],
    "he'll'": [
        {ORTH: "he", LEMMA: "he"},
        {ORTH: "'ll'", LEMMA: "will", NORM: "will", TAG: "VERB"}],
    "she'll'": [
        {ORTH: "she", LEMMA: "she"},
        {ORTH: "'ll'", LEMMA: "will", NORM: "will", TAG: "VERB"}],
    "it'll'": [
        {ORTH: "it", LEMMA: "it"},
        {ORTH: "'ll'", LEMMA: "will", NORM: "will", TAG: "VERB"}],
    "won't": [
        {ORTH: "wo", LEMMA: "will"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
    "wouldn't": [
        {ORTH: "would", LEMMA: "will"},
        {ORTH: "n't", LEMMA: "not", NORM: "not", TAG: "RB"}],
# be
    "I'm'": [
        {ORTH: "I", LEMMA: "I"},
        {ORTH: "'m'", LEMMA: "be", NORM: "am", TAG: "VERB"}]
}

def de_contraction(doc):
    new_doc = doc
    for i, token in enumerate(doc):
        new_doc = nlp.make_doc(new_doc[:i].text + ' ' + token.norm_ + ' ' + new_doc[((i)+1):].text)
    print(new_doc)

de_contraction(nlp(u"Oh no he didn't. I can't and I won't. I'll know what I'm gonna do."))
