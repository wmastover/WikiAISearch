from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt')
# Initialize the vectorizer outside the function
vectorizer = TfidfVectorizer()

def vectorise_text(text):
    # Split the text into sentences
    paragraphs = text.split('\n\n')
    vectors = vectorizer.fit_transform(paragraphs)
    return vectors, paragraphs

def find_relevant_text(query, vectors, sentences):
    query_vector = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_vector, vectors).flatten()
    most_relevant_index = cosine_similarities.argmax()
    most_relevant_text = sentences[most_relevant_index]
    return most_relevant_text
