def capitalize(string):
    for i in string.split():
        string = string.replace(i, i.capitalize())
    return string

