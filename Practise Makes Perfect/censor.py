def censor(text, word):
    text = text.split(" ")
    count = 0
    for i in text:
        if i == word:
            text[count] = "*" * len(word)
        count = count + 1
    text  = " ".join(text)
    return text

