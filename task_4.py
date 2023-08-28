def change_char(text):
    text_lower = str(text).lower()
    first_char = text_lower[0]
    text_no_first_char = text_lower[1: len(text_lower)]
    new_text = text_no_first_char.replace(first_char, "$")
    print(first_char+new_text)


texts = ["TextToTestthistask", "restart"]
for text in texts:
    change_char(text)

