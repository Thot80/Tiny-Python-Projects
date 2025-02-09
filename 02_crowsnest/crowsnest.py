#!/usr/bin/env python3
"""
Author : Thoth80 <jeremykessous@yahoo.fr>
Date   : 2025-02-09
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A Word')
    parser.add_argument('-s',
                        '--starboard',
                        help='Side of the boat',
                        metavar='starboard',
                        type=bool,
                        default=False)
    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    char = word[0]
    boat_side = "larboard" if not args.starboard else 'starboard'
    if (char.islower() and char.lower() in 'aeiou'):
        article = 'an'
    elif (char.isupper() and char.lower() in 'aeiou'):
        article = 'An'
    elif (char.islower() and not char.lower() in 'aeiou'):
        article = 'a'
    else:
        article = 'A'
    print(f'Ahoy, Captain, {article} {word} off the {boat_side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
