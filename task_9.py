def count_letters(word, letter):
    count = 0
    list_word = list(word.lower())
    if len(letter) == 1:
        for i in list_word:
            if i == letter.lower():
                count += 1
            else:
                pass
    else:
        return print("Need to enter only one letter")

    return print(count)


count_letters('wildberries', 'r')
count_letters('wildberries', 'a')
count_letters('wildberries', 'i')
count_letters('aaaaaaAaaa', 'a')