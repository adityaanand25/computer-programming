#Given a sentence, create a dictionary that counts how many times each word appears.

sentence = "hello world hello"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
