PLACEHOLDER = "[name]"

# Read the names from the invited_names.txt file
with open("Input\\Names\\invited_names.txt") as name_file:
    names = name_file.readlines()  # Read all lines into a list

# Read the letter template from the starting_letter.txt file
with open("C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\Mail Merge\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Loop through each name, replace the placeholder, and write the new letter to a file
for name in names:
    stripped_name = name.strip()  # Remove any leading/trailing whitespace
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    
    # Write the new letter to a file
    with open(f"C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\Mail Merge\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
