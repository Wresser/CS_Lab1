import collections
import sys
import numpy as np
import os

file_name = sys.argv[1]

c = None
with open(file_name, encoding="utf-8") as f:
    text = f.read()
    text_len = len(text)
    c = collections.Counter(text)

frequencies = dict()
for letter in c:
    frequencies[letter] = c[letter] / text_len


avg_entropy = 0
for letter in frequencies:
    freq = frequencies[letter]
    avg_entropy -= freq * np.log2(freq)

information = avg_entropy * text_len / 8

with open(os.path.splitext(file_name)[0] + "_analysis.txt", 'w+') as f:
    f.write("Frequencies:\n")
    for letter in frequencies:
        freq = frequencies[letter]
        if (letter == '\n'):
            f.write(f"\\n: {freq}\n")
        else:
            f.write(f"{letter}: {freq}\n")
    f.write(f"avg entropy: {avg_entropy} bits\n")
    f.write(f"information: {information} bytes\n")
    f.write(f"file size: {os.path.getsize(file_name)} bytes\n")
    f.write(f"text length: {text_len}\n")

print(f"Analysis outputed to {os.path.splitext(file_name)[0]}_analysis.txt")