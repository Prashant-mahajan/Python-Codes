def anti_vowel(text):
    new = text
    for i in range(len(text)):
        if text[i] in "aeiouAEIOU":
            new = new.translate(None, text[i])
            print new
    return new
print anti_vowel("hey look words")