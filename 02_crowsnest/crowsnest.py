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
    boat_side = "larboard" if not args.starboard else 'starboard'
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    article = article.title() if word[0].isupper() else article
    print(f'Ahoy, Captain, {article} {word} off the {boat_side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
