import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    freq = {}

    for token in tokens:
        freq[token] = freq.get(token, 0) + 1

    vector = []

    for word in vocab:
        vector.append(freq.get(word, 0))

    return np.array(vector)