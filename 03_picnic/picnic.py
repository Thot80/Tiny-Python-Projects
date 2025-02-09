#!/usr/bin/env python3
"""
Author : Thoth80 <jeremykessous@yahoo.fr>
Date   : 2025-02-09
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "str",
        help="Item(s) to bring",
        metavar="str",
        type=str,
        nargs="+",
    )

    parser.add_argument(
        "-s",
        "--sorted",
        help="Sort the items",
        action='store_true'
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = sorted(args.str) if args.sorted else args.str
    total = len(items)
    if (total == 1):
        print(f"You are bringing {items[0]}.")
    elif(total == 2):
        print(f"You are bringing {items[0]} and {items[-1]}.")
    else:       
        print(f"You are bringing {', '.join(items[:-1])}, and {items[-1]}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
