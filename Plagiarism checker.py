import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Reference dataset
reference_texts = [
    "This is the first text in the reference dataset.",
    "This is the second text in the reference dataset.",
    "This is the third text in the reference dataset."
]

# Function to extract features from text
def extract_features(text):
    # Tokenize text
    words = nltk.word_tokenize(text)
    # Extract word frequency
    fdist = nltk.FreqDist(words)
    # Extract n-grams
    bigrams = nltk.bigrams(words)
    trigrams = nltk.trigrams(words)
    # Return extracted features
    return fdist, bigrams, trigrams

# Function to compare text to reference dataset
def check_plagiarism(text):
    # Extract features from text
    text_features = extract_features(text)
    # Extract features from reference dataset
    reference_features = [extract_features(t) for t in reference_texts]
    # Use cosine similarity to compare text to reference dataset
    similarities = []
    for ref_features in reference_features:
        similarities.append(cosine_similarity(text_features, ref_features))
    # Check for plagiarism
    if max(similarities) > 0.8:
        print("Plagiarism detected.")
    else:
        print("Text is original.")

# Example usage
text = "This is an example text to check for plagiarism."
check_plagiarism(text)
