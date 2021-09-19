import spacy
import re

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("emoji", first=True)   # Add spacymoji to pipeline

def deEmojify(text):
    """
    Uses the following regex pattern to remove emoticons from text.
    """
    regrex_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # Emoticons
                           u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # Transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # Flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'',text)

def text_translate_emoji(input, output):
    """
    Opens two text files, input and output.
    For each line in input, check if there is emoji.
    If there is, use spacymoji to get the emoji's meaning.
    The demoji function defined earlier is called to remove the emoji.
    Output is saved.
    """
    f = open(output,"w", encoding="utf8")
    with open(input, 'r', encoding="utf8") as fp:
        Lines = fp.readlines()
        for line in Lines:
            doc = nlp(line)
            if doc._.has_emoji:
                new_doc = doc
                for e in doc._.emoji:
                    e_index = e[1]
                    e_str = e[2]
                    new_doc = nlp.make_doc(new_doc[:e_index].text + ' ' + e_str + ' ' + new_doc[((e_index)+1):].text)
                new_doc = deEmojify(str(new_doc))
                f.write(new_doc)
            else:
                f.write(line)
    fp.close()
    f.close()

text_translate_emoji('twitter.txt', 'twitter-emojis.txt')
