text = input("input the message: ")
text_bin = ' '.join(format(ord(char), '08b') for char in text)

with open("output.txt", 'w', encoding="utf-8") as out:
    out.write(text_bin)
    print("saved in output.txt")