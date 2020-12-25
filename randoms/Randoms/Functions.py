def greetings(first_name, last_name):
    print(f"Hello Mr/Mrs {first_name} {last_name}")


def answer():
    print("Would you like to know how many more days you will live?")
    user_input = input(">")
    if user_input == "yes":
        print("100 years")
    else:
        print("Live today as if it's your last day")


print("What's your first name?")
first_name = input(">")
print("What's your last name?")
last_name = input(">")
greetings(first_name, last_name)
answer()