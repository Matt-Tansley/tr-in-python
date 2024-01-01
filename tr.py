#!/usr/bin/env python3

import argparse

# Command line arguments handling
help_description = "Adding description"
parser = argparse.ArgumentParser(description=help_description)

# Add optional arguments
parser.add_argument("-f", "--Fun",
                    help = "Have some fun",
                    action = "store_true")

parser.add_argument("original")

# Read args from command line
args = parser.parse_args()

if args.Fun:
    print("Fun turned on")

# Run program
text = input("Enter text input:")
print("Text input is: " + text)