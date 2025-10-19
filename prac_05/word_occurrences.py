"""
Word Occurrences
Estimate: 30 minutes
Actual:    minutes
"""

text = input("Text: ")
word_to_count = {}
for word in text.split( ):
    word_to_count[word] = word_to_count.get(word, 0) + 1
print(word_to_count)