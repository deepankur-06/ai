import string

def preprocess_text(text):
    """
    Preprocess text by:
    - Converting to lowercase
    - Removing punctuation
    - Tokenizing
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into tokens
    tokens = text.split()
    
    return tokens

def calculate_similarity(tokens1, tokens2):
    """
    Calculate similarity between two token lists
    using Jaccard similarity
    """
    if len(tokens1) == 0 or len(tokens2) == 0:
        return 0.0
    
    set1 = set(tokens1)
    set2 = set(tokens2)
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    if union == 0:
        return 0.0
    
    return intersection / union

def tokenize_text(text):
    """Simple tokenization"""
    return text.lower().split()

def remove_punctuation(text):
    """Remove punctuation from text"""
    return text.translate(str.maketrans('', '', string.punctuation))
