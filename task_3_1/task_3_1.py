def symbols_text(text):
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')
    return text.split()

def meeting_words(text, length = 0):
    repeat_words = []
    qty_word = 0

    for i in text:
        if len(i) > length:
            qty = text.count(i)
            if qty > qty_word:
                qty_word = qty
                repeat_words = [i]
            elif qty == qty_word:
                repeat_words.append(i)

    return list(set(repeat_words))

def longest_word_eng(text):
    longest_word = []
    qty_long_word = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in text:
        for x in i:
            if x not in alphabet:
                xEn = False
                break
            else:
                xEn = True
        if xEn:
            qty = len(i)
            if qty > qty_long_word:
                qty_long_word = qty
                longest_word = [i]
            elif qty == qty_long_word:
                longest_word.append(i)
    return list(set(longest_word))


file_name = input("Введите название файла:  ")
with open(file_name, encoding="utf8") as A:
    text_file = A.read()
text_file = symbols_text(text_file)
print(f"Список самых частых слов длинной более трёх символов: {meeting_words(text_file, 3)}")
print(f"Список самых длинных английских слов: {longest_word_eng(text_file)}")