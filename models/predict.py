import joblib
from preprocess import clean_review  # Import preprocessing function
import nltk
nltk.download('stopwords')

# Load the trained model and vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Take input from the user
review = input("Enter a review: ")  # This allows user input

# Preprocess and predict
cleaned_review = clean_review(review)
vectorized_review = vectorizer.transform([cleaned_review])
prediction = model.predict(vectorized_review)

# Display the sentiment
sentiment = "Positive" if prediction[0] == 1 else "Negative"
print("Predicted Sentiment:", sentiment)
