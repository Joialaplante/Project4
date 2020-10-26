import random
# Joia LaPlante


# the main function asks the user what file they would like to open
def main():
    name = (input("What file would you like to open?"))
    fortunes(name)


# this fortunes function reads the file and prints the sayings
def fortunes(name):
    file = open(name, 'r')
    all_of_file = file.readlines()
    random_line = random.choice(all_of_file)
    print(random_line)


# display function
def display_fortunes():
    more_fortunes = (input("Would you like more fortunes?"))
    print(more_fortunes)
    yes = "yes"
    yes.startswith("ye")
    if more_fortunes == "yes":
        print(random_line)


main()
display_fortunes()