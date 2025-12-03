"""
1. import os
2. create a relative path for poem_original and poem_remix using os.path.join
3. def read text()
    A. Opens poem_original.txt for reading
    B. Reads all the lines into a list .
    C. Prints the original poem to the screen (line by line).
4. def read_backwards()
    A. Opens poem_original.txt for reading
    B. reads all the reversed lines into a list.
    C. Prints the reversed poem to the screen (line by line).
5. def change_words()
    A. creates an empty list for new lines
    B. changes the word 'woods' to 'trees' and appends to list
    C. returns list of new_lines
6. def change_punctuation():
    A. creates an empty list for new lines
    B. changes the punctuation from '.' to '!' and appends to list
    C. returns list of new_lines
7. def write_text()
    A. opens poem_remix.txt in write mode
    B. writes all the remixed lines into poem_remix.txt
8. def append_text()
    A. opens poem_remix.txt in append mode
    B. appends 3 lines to bottom of poem
9. c
"""

import os

# Creates relative file paths
file_path1 = os.path.join("docs", "poem_original.txt")
file_path2 = os.path.join("docs", "poem_remix.txt")

def read_text(file_path):
    """
    reads the poem in poem_original.txt line by line
    """
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines() # read through each line and saves as a list
            for line in lines: # strips each line and prints it
                print(line.strip())
            return lines
    except FileNotFoundError as e:
        print("File not found", e)



def read_backwards():
    """
    reads the poem in poem_original.txt backwards
    """
    try:
        with open(file_path1, 'r') as f:
            lines = f.readlines() # read through each line and saves as a list
            for line in lines[::-1]:  # reverses the list
                print(line.strip())
            return lines[::-1]  #returns reversed lines

    except FileNotFoundError as e:
        print("File not found", e)


def change_words(lines):
    """
    Switches the word 'woods' to 'trees'
    """
    new_line = []
    for line in lines:
        new_line.append(line.replace("woods", "trees"))
    return new_line

def change_punctuation(lines):
    """
    Changes punctuation from '.' to '!' and appends to list
    """
    new_line = []
    for line in lines:
        new_line.append(line.replace(".", "!"))
    return new_line

def write_text(new_lines):
    """
    Writes the reversed poem into poem_remix.txt
    """
    try:
        with open(file_path2, "w") as f:  # opens poem_remix.txt and writes in it.
            for line in new_lines:
                f.write(line.strip() + "\n")  # Writes each line remixed

    except FileNotFoundError as e:
        print("File not found", e)


def append_text():
    """
    appends to the poem the reason why this is my favorite poem and my name, saving the result in poem_remix.txt
    """
    try:
        with open(file_path2, "a") as f:  # Opens poem_remix.txt and appends to it.
            f.write("\n")  # Prints a blank line
            f.write("----------------------------------------------------\n")
            f.write("I switched 'woods' for 'trees' and reversed the poem")
            f.write("\n")  # Prints a blank line
            f.write("Remixed by: Miriam Stern\n")

    except FileNotFoundError as e:
        print("File not found", e)


def main():
    """
    Runs the full poem remix program:
    reads original, remixes, writes, appends, and prints final result.
    """

    print("\n----original----")
    read_text(file_path1)  # Reads original poem
    print("\n----reversed----")
    reversed_lines = read_backwards()
    print("\n----remix----")
    changed_lines = change_words(reversed_lines)  # Changes words in reversed lines
    changed_punctuation = change_punctuation(changed_lines)  # Changes punctuation in changed lines
    for line in changed_punctuation:  # Prints each line with changes as remixed poem
        print(line.strip())
    write_text(changed_punctuation)  # Writes the poem with changed punctuation to pem_remix
    append_text()  # Appends text to poem_remix.txt


main()



