vowels = ["a", "e", "i", "o", "u"]

found = {}

word = input("Enter a word: ")

for char in word:
    if char in vowels:
        found.setdefault(char, 0)
        found[char] += 1 
        
for k, v in sorted(found.items()):
        print(k, "is found ", v, "times")
