import os
import nltk

# Add local nltk_data path
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# Download the vader_lexicon
nltk.download('vader_lexicon')

# Verify that the lexicon is downloaded
lexicon_path = os.path.join(os.getcwd(), 'nltk_data', 'sentiment', 'vader_lexicon.txt')
print(f"Lexicon file is at: {lexicon_path}")
