def word_longest_length(word_list):
    word_length = []
    for n in word_list:
        word_length.append((len(n),n))
        word_length.sort()
        return word_length[-1][1]
print(word_longest_length(["Python","Java","Azure"]))


