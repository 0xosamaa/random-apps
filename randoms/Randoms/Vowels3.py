vowels = set('aeiou')
word = input('Enter a word to search for vowels: ')
out = vowels.intersection(set(word))
for vowel in out:
    print(vowel)