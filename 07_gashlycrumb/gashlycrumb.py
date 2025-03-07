#!/usr/bin/env python3
"""
Author : Thoth80 <jeremykessous@yahoo.fr>
Date   : 2025-03-07
Purpose: Gashlycrumb
"""

import argparse

from pprint import pprint as pp


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+',
                        type=str)

    
    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType(mode='rt', encoding='UTF-8'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lookup = {}
    
    for line in args.file:
        lookup[line[0].lower()] = line.strip()

    
    for letter in args.letter:
        print(lookup.get(letter.lower(), f'I do not know "{letter}".'))
    
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
