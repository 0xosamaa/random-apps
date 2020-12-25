print("Type 'Help'")
is_started = False
while True:
    Order = input()
    if Order.title() == "Help":
        print(""" 
        -Start to start car
        -Stop to stop car
        -Quit to exit
        """)
    elif Order.title() == "Start":
        if not is_started: 
            is_started = True
            print("Car started")
        else:
            print("Car is already started")
    elif Order.title() == "Stop":
        if is_started:
            is_started = False
            print("Car stopped")
        else:
            print("Car is already stopped")
    elif Order.title() == "Quit":
        break
    else:
        print("""I don't understand that
        """)
