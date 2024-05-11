# подготовка текста к анализу    

text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

# анализ текста

word_frequency = ...

# вывод результатов

print("Количество разных слов:", ...)
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")