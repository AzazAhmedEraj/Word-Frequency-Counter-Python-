from collections import Counter

def word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    words = text.split()
    return Counter(words)

print(word_frequency('example.txt'))
