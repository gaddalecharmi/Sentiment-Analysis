import sys
import os
import warnings

warnings.filterwarnings('ignore')

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Add the parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.preprocess import clean_review  # Now the import will work

# Load dataset
data = pd.read_csv("data/Amazon-Product-Reviews-Sentiment-Analysis-in-Python-Dataset.csv")
data.dropna(inplace=True)

# Label Sentiment
data.loc[data['Sentiment'] <= 3, 'Sentiment'] = 0  # Negative
data.loc[data['Sentiment'] > 3, 'Sentiment'] = 1   # Positive

# Apply preprocessing
data['Review'] = data['Review'].apply(clean_review)

# Convert text to numerical vectors
vectorizer = TfidfVectorizer(max_features=2500)
X = vectorizer.fit_transform(data['Review']).toarray()
y = data['Sentiment']

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train model
model = LogisticRegression()
model.fit(x_train, y_train)

# Evaluate model
pred = model.predict(x_test)
print(f"Model Accuracy: {accuracy_score(y_test, pred):.2f}")

# Save model & vectorizer
joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
print("Model and vectorizer saved successfully.")
