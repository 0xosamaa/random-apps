numbers = [3,3,5,1,6,6,5]
duplicates = []
for number in numbers:
    if number in numbers[numbers.index(number) + 1:]:
        if number not in duplicates:
            duplicates.append(number)
print(duplicates)