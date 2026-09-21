def remove_stopwords(tokens: list, stopwords: list) -> list:
    """
    Returns a list of tokens.
    """
    # Write code here
    notastopword=[]
    for stopword in tokens:
        if stopword not in stopwords:
            notastopword.append(stopword)
        else:
            continue
    return notastopword