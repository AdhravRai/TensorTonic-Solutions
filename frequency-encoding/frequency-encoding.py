def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    counts={}
    for v in values:
        counts[v]=counts.get(v,0)+1

    total=len(values)
    encoded=[]
    for v in values:
        encoded.append(counts[v]/total)

    return encoded
    