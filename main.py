""" Welcome to my escape room game!"""


def get_valid_choice(valid_options: list) -> str:
    """Ask for input until the player enters one of the valid options."""
    choice = input("What would you like to do? ").lower()
    while choice not in valid_options:
        choice = input("That is not a valid choice. Try again: ").lower()
    return choice


def bedroom() -> str:
    """Show the bedroom and return the next room."""
    print("You wake up on the floor of an unfamiliar bedroom with no memory of how you got here. The door is slightly open.")
    print("1. Leave the room")
    get_valid_choice(["1"])
    return "hallway"


def hallway() -> str:
    """Show the hallway and return the next room."""
    print("You are standing in the main hallway. Doors lead to several rooms.")
    print("1. Kitchen")
    print("2. Office")
    print("3. Library")
    print("4. Bathroom")
    print("5. Closet")
    print("6. Basement stairs")
    choice = get_valid_choice(["1", "2", "3", "4", "5", "6"])
    if choice == "1":
        return "kitchen"
    if choice == "2":
        return "office"
    if choice == "3":
        return "library"
    if choice == "4":
        return "bathroom"
    if choice == "5":
        return "closet"
    return "basement_stairs"


def kitchen() -> str:
    """Show the kitchen and return the next room."""
    global has_key
    print("You are in the kitchen. Pots and pans are scattered across the counter.")
    if has_key:
        print("You already searched the counter here.")
        print("1. Go back to the hallway")
        get_valid_choice(["1"])
        return "hallway"
    print("1. Search the counter")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        has_key = True
        print("You search through the pots and pans and find a rusty old key!")
        return "kitchen"
    return "hallway"


def office() -> str:
    """Show the office and return the next room."""
    global found_code_part_two
    global drawer_unlocked
    print("You are in the office. A heavy wooden desk sits in the corner, its bottom drawer locked tight.")
    if drawer_unlocked:
        print("The drawer is already open and empty.")
        print("1. Go back to the hallway")
        get_valid_choice(["1"])
        return "hallway"
    if not has_key:
        print("The drawer is locked. You probably need a key.")
        print("1. Go back to the hallway")
        get_valid_choice(["1"])
        return "hallway"
    print("1. Unlock the drawer with your key")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        drawer_unlocked = True
        found_code_part_two = True
        print("The drawer clicks open. Inside is a torn note that reads: 'Second half of the code: 92'")
        return "office"
    return "hallway"


def library() -> str:
    """Show the library and return the next room."""
    global found_code_part_one
    print("You are in the library. Dusty bookshelves line every wall.")
    if found_code_part_one:
        print("You already read the book here.")
        print("1. Go back to the hallway")
        get_valid_choice(["1"])
        return "hallway"
    print("1. Read the old book on the desk")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        found_code_part_one = True
        print("Inside the book is a note that reads: 'First half of the code: 47'")
        return "library"
    return "hallway"


def bathroom() -> str:
    """Show the bathroom and return the next room."""
    print("You are in a small bathroom. A cracked mirror hangs above the sink.")
    print("1. Look in the mirror")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        print("You see your own tired reflection staring back at you. Nothing useful here.")
        return "bathroom"
    return "hallway"


def closet() -> str:
    """Show the closet and return the next room."""
    global has_flashlight
    print("You are in a narrow closet filled with old coats and boxes.")
    if has_flashlight:
        print("You already grabbed the flashlight from here.")
        print("1. Go back to the hallway")
        get_valid_choice(["1"])
        return "hallway"
    print("1. Search the boxes")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        has_flashlight = True
        print("You find a flashlight buried under an old coat!")
        return "closet"
    return "hallway"


def basement_stairs() -> str:
    """Show the basement stairs and return the next room."""
    print("You are at the top of a dark stairwell leading down to the basement.")
    if not has_flashlight:
        print("It is pitch black down there. You should find a light source first.")
        print("1. Go back to the hallway")
        get_valid_choice(["1"])
        return "hallway"
    print("1. Go downstairs")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "1":
        return "basement_door"
    return "hallway"


def basement_door() -> str:
    """Show the basement door and return the next room."""
    global basement_unlocked
    print("You reach a heavy metal door with a four digit keypad.")
    if basement_unlocked:
        print("1. Go through the door")
        print("2. Go back to the hallway")
        choice = get_valid_choice(["1", "2"])
        if choice == "1":
            return "basement"
        return "hallway"
    print("1. Enter a code")
    print("2. Go back to the hallway")
    choice = get_valid_choice(["1", "2"])
    if choice == "2":
        return "hallway"
    code = input("Enter the four digit code: ").lower()
    if code == "4792":
        basement_unlocked = True
        print("The keypad beeps and the door unlocks!")
        return "basement"
    print("The keypad flashes red. That code is not correct.")
    return "basement_door"


def basement() -> str:
    """Show the basement and return the next room."""
    print("You step into the basement. Moonlight spills in through a small window, and beside it is an unlocked exit door.")
    print("1. Walk through the exit door")
    get_valid_choice(["1"])
    print("You push open the door and step outside into the cool night air. You escaped!")
    print("THE END")
    return "end"


has_key = False
has_flashlight = False
found_code_part_one = False
found_code_part_two = False
drawer_unlocked = False
basement_unlocked = False
current_room = "bedroom"

print("ESCAPE THE HOUSE")
print("Find a way out before it is too late.")

while True:
    if current_room == "bedroom":
        current_room = bedroom()
    elif current_room == "hallway":
        current_room = hallway()
    elif current_room == "kitchen":
        current_room = kitchen()
    elif current_room == "office":
        current_room = office()
    elif current_room == "library":
        current_room = library()
    elif current_room == "bathroom":
        current_room = bathroom()
    elif current_room == "closet":
        current_room = closet()
    elif current_room == "basement_stairs":
        current_room = basement_stairs()
    elif current_room == "basement_door":
        current_room = basement_door()
    elif current_room == "basement":
        current_room = basement()
    else:
        break

print("Thanks for playing!")