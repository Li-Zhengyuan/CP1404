"""
Word Occurrences
Estimate: 30 minutes
Actual:    minutes
"""
from prac_05.state_names import max_length

text = input("Text: ")

word_to_count = {}
for word in text.split( ):
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max(len(word) for word in word_to_count.keys())
for word, count in word_to_count.items():
    print(f"{word}: {count}")