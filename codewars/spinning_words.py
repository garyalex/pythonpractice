def spin_words(sentence):
    nwords = []
    words = sentence.split()
    for w in words:
        if len(w) >= 5:
            nwords.append(w[::-1])
        else:
            nwords.append(w)
    return " ".join(nwords)


print(spin_words("Welcome"))
print(spin_words("I am the walrus"))
