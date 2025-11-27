words = ["apple", "banana", "apple", "orange", "banana", "banana"]
freq = {}
duplicates = {}

for w in words:
    if w not in freq:
        freq[w] = 1
    else:
        freq[w] += 1

for w in freq:
    if freq[w] > 1:
        duplicates[w] = freq[w]

print(duplicates)
