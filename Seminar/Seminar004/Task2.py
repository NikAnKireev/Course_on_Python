# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.

# Output: 14

text = "She sells sea shells on the sea shore;The shells \
that she sells are sea shells I'm sure.So if she sells sea \
shells on the sea shore,I'm sure that the shells are sea \
shore shells."

znak = ['.', ',', ';', ':', "'"]
print()

for i in znak:
    for j in range(0, len(text)):
        i == text[j]
        text = text.replace(i, " ").lower()

array = set(text.split())

print(array)
print(len(array))
