#!/usr/bin/env py
"""
Author : Anonymous <Anonymous@DESKTOP-NHPIQ44>
Date   : 2025-03-14
Purpose: Apples and bananas
"""

import argparse
import os
import io
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file',)

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'])


    
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')
    
    return args 

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    for line in args.text:
        output = re.sub("[aeiou]", args.vowel, line)
        output = re.sub("[AEIOU]", args.vowel.upper(), output)
        print(output)

# --------------------------------------------------
if __name__ == '__main__':
    main()
