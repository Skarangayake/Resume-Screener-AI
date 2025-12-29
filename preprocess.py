import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Clean text using NLP:
    - lowercase
    - remove stopwords & punctuation
    - lemmatization
    """
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)

