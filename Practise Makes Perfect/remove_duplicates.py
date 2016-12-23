def remove_duplicates(n):
    m = []
    for i in range(len(n)):
        if n[i] not in m:
            m.append(n[i])
    return m