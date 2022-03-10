def find_freq_words(textfile):
    # Creates a list of all the words in the document
    file = open(textfile, encoding='utf8').read()
    all_words = file.split(" ")

    # A list that will contain the words without repeats
    words = []

    # Goes through all the words to add all the words(not repeated) into the list
    for word in all_words:
        if word not in words:
            words.append(word)

    # List to hold the word and how many times it appears in the document
    wordcount = []
    for word in words:
        count = 0
        for repeat in all_words:
            if repeat == word:
                count += 1
        wordcount.append((count, word))

    def number(item):
        return item[0]

    # print(wordcount)
    wordcount = sorted(wordcount, key=number, reverse=True)
    # print(wordcount)

    for key, value in wordcount[0:5]:
        print(f"{value}: {key}")
