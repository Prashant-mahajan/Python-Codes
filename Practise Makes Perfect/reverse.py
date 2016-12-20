def reverse(text):
    rev = ""
    j = int(len(text))
    for i in range(len(text)):
        rev += text[j-1]
        j -= 1
    return rev


