import re

import spacy
from nltk.corpus import stopwords

# load pre-trained model
nlp = spacy.load('fr_core_news_sm')

# Grad all general stop words
STOPWORDS = set(stopwords.words('french'))


EDUCATION = ['INGÉNIEUR','MASTER', 'LICENSE', 'TECHNICIEN','BTS']


def extract_education(resume_text):
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]


    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):

        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    # Extract year
    education = []
    for key in edu.keys():
        d = {}
        year = re.search(re.compile(r'(((|20)(\d{4})))'), edu[key])
        if year:
            d["degree"] = key
            d["fulleducation"] = edu[key]
            d["year"] = ''.join(year[0])

        else:
            d["degree"] = key
            d["fulleducation"] = edu[key]
            d["year"] = ""
        education.append(d)
    return education
