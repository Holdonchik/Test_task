def is_anagram(text1, text2):
    list_text1 = list(text1.lower())
    list_text2 = list(text2.lower())
    list_text1.sort()
    list_text2.sort()
    if list_text1 == list_text2:
        return True
    else:
        return False


words_pairs = [['car', 'tar'], ['car', 'cart'], ['anagram', 'margana'], ['beluga', 'aguleb']]
for pair in words_pairs:
    print(is_anagram(pair[0], pair[1]))
