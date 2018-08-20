#!/usr/bin/env python3

import sys
import argparse 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first')
    parser.add_argument('second')
    args = parser.parse_args()

    print(funnel(args.first, args.second))

def funnel(first, second):
    for i, val in enumerate(first):
        if first[:i] + first[i+1:] == second:
            return True
    return False

if __name__ == "__main__":
    sys.exit(main())
