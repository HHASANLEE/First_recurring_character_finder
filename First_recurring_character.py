def first_recurring_character(frc):
    counts = set()
    for char in frc:
        if char in counts:
            return char
        counts.add(char)
    return None

characters = input("You have to write the characters: ")

result = first_recurring_character(characters)
if result:
    print(f"The first recurring character is: {result}")
else:
    print(None)

