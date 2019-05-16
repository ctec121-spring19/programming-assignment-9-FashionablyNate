# Module 6 - Problem Set No. 9 - Problem 1

"""
READ ALL INFORMATION CAREFULLY AND THEN READ IT AGAIN

IMPORTANT - PROVIDE AN IPO (Inputs, Processes, and Output) AT THE TOP OF 
EACH PROGRAM USING COMMENTS.

Write a program that gets a string containing the person's first, middle and 
last names using input(), and then displays their first, middle and last 
initials. For example, the user enters "Bruce Lawrence Elgort", the program 
should display B.L.E. It must display exactly like this with the .'s after 
each letter with no spaces.

IPO
==========
INPUTS: a string containing the persons first, middle, and last name
PROCESSES: gets the first letter of every word in string
OUTPUTS: outputs initials with '.'s in between

"""

def main():
    # your code goes here
    name = input("What's your full name? ")
    initials = ""
    for word in name.split():
        initials = initials + word[0] + "."
    initials = initials.upper()
    print(initials)

main()