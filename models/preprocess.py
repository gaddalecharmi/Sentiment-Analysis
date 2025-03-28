import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')
stp_words = set(stopwords.words('english'))

def clean_review(review):
    """
    Function to clean a review by removing stopwords.
    """
    return " ".join(word for word in review.split() if word.lower() not in stp_words)
