#!/usr/bin/env python3

import argparse


# Helper functions
def tr_replace(text, str1, str2):
    new_text = text

    if is_range(str1):
        if is_range(str2):
            # Original and replacement are ranges
            str1_range_list = list(char_range(str1[0], str1[2]))
            str2_range_list = list(char_range(str2[0], str2[2]))

            for i in range(len(str1_range_list)):
                replacement = str2_range_list[i] if i < len(str2_range_list) else str2_range_list[-1]
                new_text = new_text.replace(str1_range_list[i], replacement)
        else:
            # Original is a range, replacement is a fixed string
            for c in char_range(str1[0], str1[2]):
                new_text = new_text.replace(c, str2)
    else:
        if is_range(str2):
            # Original is a fixed string, replacement is a range
            new_text = new_text.replace(str1, str2[0])
        else:
            # Original is a fixed string, replacement is a fixed string
            new_text = new_text.replace(str1, str2)

    return new_text


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


def is_range(string: str):
    return (len(string) == 3
            and string[0].isalpha()
            and string[1] == "-"
            and string[2].isalpha())


# argparse setup
help_description = "Adding description"
parser = argparse.ArgumentParser(description=help_description)

parser.add_argument("-f", "--fun",
                    help="Have some fun",
                    action="store_true")

parser.add_argument("strings",
                    help="The original string to search for",
                    nargs="+")

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
    text = input("\nEnter text input: ")
    print("\nText input is: " + text)

    new_text = tr_replace(text, strings[0], strings[1])

    print("\nText output is: " + new_text)
else:
    print("No implemention for 1 or 0 strings yet")
