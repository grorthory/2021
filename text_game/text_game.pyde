has_cup = False
has_toothbrush = False
cabinet_open = False

def bedroom():
    print("You are in a bedroom.")
    print("A door leads to a hallway.")
    response = raw_input("> ").lower()
    if "hallway" in response:
        hallway()
    else:
        print("You can't do that.")
        bedroom()

def hallway():
    print("You are in a hallway. Doors on either side lead to a bedroom and a bathroom.")
    print("Down the hall is the kitchen.")
    response = raw_input("> ").lower()
    if "bedroom" in response:
        bedroom()
    if "bathroom" in response:
        bathroom()
    else:
        print("You can't do that.")
        hallway()

def bathroom():
    global has_cup
    global has_toothbrush
    global cabinet_open
    print("You are in a bathroom. The door leads to a hallway.")
    print("There is a toilet and a sink.")
    if has_toothbrush == False:
        print("There is a toothbrush here.")
    if cabinet_open 
    response = raw_input("> ").lower()
    if "leave" in response or "hallway" in response:
        print(response)
        hallway()
    elif "toothbrush" in response and has_toothbrush == False:
        print("You take the toothbrush.")
        has_toothbrush = True
        bathroom()
    else:
        print("You can't do that.")
        bathroom()

bedroom()
