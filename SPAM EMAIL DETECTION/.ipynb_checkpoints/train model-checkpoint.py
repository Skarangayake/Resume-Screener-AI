import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

print("Loading dataset...")

# Load dataset
data = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "text"]
)

# Clean data
data["text"] = data["text"].str.lower()
data["label"] = data["label"].map({"ham": 0, "spam": 1})

X = data["text"]
y = data["label"]

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")
X_vect = tfidf.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vect, y)

# Save files
pickle.dump(tfidf, open("vectorizer.pkl", "wb"))
pickle.dump(model, open("model.pkl", "wb"))

print("✅ SUCCESS: vectorizer.pkl & model.pkl created")