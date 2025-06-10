def char_frequencies(s):
    freq = {}
    for char in s:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return freq
print(char_frequencies("data structures and algorithms"))