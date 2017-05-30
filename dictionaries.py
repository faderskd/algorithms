def find_largest_word(word, set_words):
    counters = {w: 0 for w in set_words}
    for c in word:
        for w in set_words:
            if counters[w] < len(w) and w[counters[w]] == c:
                counters[w] += 1
    max_w = ""
    for w, c in counters.items():
        if len(w) == c:
            max_w = max(w, max_w, key=lambda k: len(k))
    return max_w

print(find_largest_word('aasdfdfgasdvv g sadhrasdtg  xsd vjasdhturyasp yasd', {"afjfs", "shfxvaybx", "asfhtsb", "sfhfvs", "   dup a"}))
