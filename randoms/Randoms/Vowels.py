word = input("Enter a word: ")
found = []
vowels = ['a','e','i','o','u']

for letters in word:
    if letters in vowels:
        if letters not in found:
            found.append(letters)
for vowel in found:
    print(vowel)
if len(found) == 0:
    print("No vowels found")
    
