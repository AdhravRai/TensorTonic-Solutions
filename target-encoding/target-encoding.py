def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    counts={}
           
    sums={}
    for c,t in zip(categories,targets):
        counts[c]=counts.get(c,0)+1
        sums[c]=sums.get(c,0)+t

    means={}
    for c in counts:
        means[c]=sums[c]/counts[c]

    e=[]
    for c in categories:
        e.append(means[c])

    return e