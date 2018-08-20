#!/usr/bin/env python3

import sys
import argparse 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first')
    parser.add_argument('second')
    args = parser.parse_args()

    print(funnel(args.first, args.second))
    print("Bonus 1: " + ", ".join(bonus_1(args.first)))

def funnel(first, second):
    for i, val in enumerate(first):
        if first[:i] + first[i+1:] == second:
            return True
    return False

def bonus_1(string):
    enable1 = open('enable1.txt').read().split('\n')
    words = []
    for i, val in enumerate(string):
        string_letter_removed = string[:i] + string[i+1:]
        if string_letter_removed in enable1 and string_letter_removed not in words:
            words.append(string_letter_removed)
    return words

if __name__ == "__main__":
    sys.exit(main())
