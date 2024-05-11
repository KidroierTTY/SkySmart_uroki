from typing import Counter

# подготовка текста к анализу

text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

# анализ текста

word_frequency = Counter(words)

# вывод результатов

print("Количество разных слов:", int(word_frequency.most_common()[0][1]))
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
