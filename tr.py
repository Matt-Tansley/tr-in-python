#!/usr/bin/env python3

import argparse

# argparse setup
help_description = "Adding description"
parser = argparse.ArgumentParser(description=help_description)

parser.add_argument("-f", "--fun",
                    help = "Have some fun",
                    action = "store_true")

parser.add_argument("strings",
                    help = "The original string to search for",
                    nargs = "+")

# Read args from command line
args = parser.parse_args()

# Fun flag
if args.fun:
    print("Fun turned on")

# Process strings
strings = args.strings

if len(strings) > 2:
    # Using this condition as a workaround because as far as I can tell,
    # I can't specify an argument to take a range of values (e.g between 1 - 2)
    print("ERROR: Too many string arguments provided, maximum 2. First is original string, second is replacement "
          "string")
    quit()
elif len(strings) > 1:
    # Step 1: Replace one character with another
    text = input("Enter text input: ")
    print("Text input is: " + text)

    new_text = text.replace(strings[0], strings[1])
    print(new_text)
else:
    print("No implemention for 1 or 0 strings yet")
