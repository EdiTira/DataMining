def make_stop_words():
    stop_words = set()
    with open('stop_words/stopwords.txt', 'r') as f:
        for line in f:
            stop_words.add(line.strip())
    return stop_words
