import re
import spacy
from spellchecker import SpellChecker
from contractions import de_contraction

spell = SpellChecker()
nlp = spacy.load("en_core_web_sm")

with open('twitter.txt', 'r', encoding="utf8") as fp:
    Lines = fp.readlines()
    for line in Lines:
        line = str(de_contraction(nlp(line)))
        misspelled = spell.unknown(re.compile('\w+').findall(line))
        for word in misspelled:
            print('\n' + line)
            print(word)
            print(spell.correction(word))
