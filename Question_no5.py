# Question 5 - Character Frequency and Count of Vowels/Consonants

text = input("Enter a string: ").lower()  
frequency = {}

for ch in text:
    if ch >= 'a' and ch <= 'z':  
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

for key, value in frequency.items():
    print(f"{key} → {value}")
print("-" * 30)


vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch >= 'a' and ch <= 'z':
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
