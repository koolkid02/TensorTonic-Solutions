def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    freq={}
    for sentence in sentences:
        for word in sentence:
            if word not in freq:
                freq[word]=0
            freq[word]+=1
    return freq
            
            

    