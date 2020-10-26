import random


# the main function asks the user what file they would like to open
def main():
    name = (input("What file would you like to open?"))
    display_fortunes()


# this fortunes function reads the file and prints the sayings
def fortunes(name):
    file = open(name, 'r')
    all_of_file = file.readlines()
    print(name)


# this display function
def display_fortunes():
    more_fortunes = (input("Would you like more fortunes?"))
    yes = "yes"
    yes.startswith("ye")
    lower().startswith()
    while more_fortunes == "yes":
        print(name)





main()
fortunes()
display_fortunes()
