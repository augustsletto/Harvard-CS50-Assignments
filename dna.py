import csv
import sys

csv_file = sys.argv[1]
txt_file = sys.argv[2]

rows = []
with open(csv_file) as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames
    for row in reader:
        rows.append(row)


with open(txt_file) as t:
    text = t.read()


def dna_sampler(text, word):
    word_len = len(word)
    max_count = 0
    current_count = 0
    i = 0


    while i <= len(text) - word_len:
        if text[i:i+word_len] == word:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
            i += word_len
        else:
            current_count = 0
            i += 1
    return max_count



def matcher():
    dna_results = ["name", ]
    for word in header[1:]:
        dna_results.append(dna_sampler(text, word))
    for row in rows:
        values = [int(value) for value in list(row.values())[1:]]
        name = row["name"]
        if values == dna_results[1:]:
            return name
    return "No Match"
        

print(matcher())

