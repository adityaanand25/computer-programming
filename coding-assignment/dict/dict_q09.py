#Write a program that counts the frequency of each character in a given string using a dictionary.

text = "hello"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
