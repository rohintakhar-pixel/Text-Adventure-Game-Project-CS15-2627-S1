

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