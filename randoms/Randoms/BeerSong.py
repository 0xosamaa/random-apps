word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall")
    print(f"{beer_num} {word} of beer")
    print("Take one down")
    print("Pass it around")
    
    if beer_num == 1:
        print("No more bottles of beer on the wall")
    else:
        word_num = beer_num - 1
        if word_num == 1:
            word = "bottle"
        print(word_num, word, "of beer on the wall")
    print()
    
    