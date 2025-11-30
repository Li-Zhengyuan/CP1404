"""
Word Occurrences
Estimate: 30 minutes
Actual:   20 minutes
"""

text = input("Text: ")

word_to_count = {}
for word in text.split( ):
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max(len(word) for word in word_to_count)

sorted_words = sorted(word_to_count.keys())

for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")