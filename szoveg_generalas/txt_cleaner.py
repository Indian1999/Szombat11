from tensorflow.keras.preprocessing.text import Tokenizer
import json
import os

path = os.path.join(os.path.dirname(__file__),"hamlet.txt")

with open(path, "r", encoding="utf-8") as f:
    szöveg = f.read().lower()

abc = "qwertzuioplkjhgfdsayxcvbnm"
clean = ""
for char in szöveg:
    if char == "\n" or char  == "\t" or char == " ":
        clean += " "
    if char in abc:
        clean += char

clean = clean.strip()
while "  " in clean:
    clean = clean.replace("  ", " ")

print(clean)
with open(os.path.join(os.path.dirname(__file__), "hamlet_clean.txt"), "w", encoding="utf-8") as f:
    f.write(clean)

tokenizer = Tokenizer()
tokenizer.fit_on_texts([clean])

with open(os.path.join(os.path.dirname(__file__), "token_map.json"), "w", encoding="utf-8") as f:
    json.dump(tokenizer.index_word, f)
