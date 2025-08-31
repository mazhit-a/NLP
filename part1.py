import nltk
from nltk.tokenize import word_tokenize, TweetTokenizer
import spacy

# Download NLTK data if not already done
nltk.download('punkt')

texts = [
    "ATG-CGA-TTT-AGC",
    "The quick brown fox jumps over the lazy dog.",
    "Just landed in NYC!!! 😎✈ #travel #blessed"
]

# Method 1: NLTK word_tokenize
for text in texts:
    print("NLTK:", word_tokenize(text))

# Method 2: TweetTokenizer
tweet_tokenizer = TweetTokenizer()
for text in texts:
    print("TweetTokenizer:", tweet_tokenizer.tokenize(text))

# Method 3 (optional): spaCy
nlp = spacy.load("en_core_web_sm")
for text in texts:
    doc = nlp(text)
    print("spaCy:", [token.text for token in doc])
