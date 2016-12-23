def purify(n):
    m = []
    for i in range(len(n)):
        if n[i] %2 == 0:
            m.append(n[i])
    return m