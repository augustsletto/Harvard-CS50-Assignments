import re

text = input("Text: ")

word_list = text.split(" ")
sentence_list = re.split(r'(?<=[.!?])\s+', text)
letter_list = "".join(re.findall(r'\w', text))


L = (len(letter_list) / len(word_list)) * 100

S = (len(sentence_list) / len(word_list)) * 100


index = 0.0588 * L - 0.296 * S - 15.8


if index <= 1:
    print(f"Before Grade 1")

elif round(index) > 16:
    print("Grade 16+")
else:
    print(f"Grade {round(index)}")
