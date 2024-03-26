# variables
PLACEHOLDER = "[name]"

# read names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# for each name, strip out the blank space or new line at end of name, replace [name] placeholder with
# recipients name, then generate new letter for each name.
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)