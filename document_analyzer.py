def document_analyzer(textfile):
    # Creates a list of all the words in the document
    file = open(textfile, encoding='utf8').read()
    allwords = file.split(" ")

    print(allwords)
    # A list that will contain the words without repeats
    words = []

    # Goes through all the words to add all the words(not repeated) into the list
    for word in allwords:
        if word not in words:
            #print(word)
            words.append(word)

    # List to hold the word and how many times it appears in the document
    wordcount = {}
    for word in words:
        count = 0
        for repeat in allwords:
            if repeat == word:
                count += 1
        wordcount.update({count: word})

    worditems = wordcount.items()
    sortedwords = sorted(worditems, reverse=True)

    for key, value in sortedwords[0:5]:
        print(f"{value}: {key}")
