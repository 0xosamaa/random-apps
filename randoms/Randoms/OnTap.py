phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.insert(2, plist.pop(3))
plist.extend([plist.pop(), plist.pop()])
new_phrase = ''.join(plist)
print()
print(plist)
print(new_phrase)
