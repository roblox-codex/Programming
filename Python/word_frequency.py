import re

text = input("Enter a paragraph of text: ")
words = re.findall(r'\w+', text.lower())
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
