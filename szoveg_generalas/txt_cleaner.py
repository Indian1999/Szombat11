path = "hamlet.txt"

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
with open("hamlet_clean.txt", "w", encoding="utf-8") as f:
    f.write(clean)