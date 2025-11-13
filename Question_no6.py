
# QUESTION 6: Count Vowels and Consonants


text = input("Enter a string: ")
vowels_count = 0
consonants_count = 0


for ch in text:
  
    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)
    
   
    if 'a' <= ch <= 'z':
      
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels_count += 1
        else:
            consonants_count += 1


print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
