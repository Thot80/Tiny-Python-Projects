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
        "item",
        metavar="str",
        nargs="+",
        help="Item(s) to bring",
    )

    parser.add_argument(
        "-s",
        "--sorted",
        action='store_true',
        help="Sort the items",
    )
    
    parser.add_argument(
        "-n",
        "--no-oxford",
        action='store_true',
        help="Remove Oxford trailing comma",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = sorted(args.item) if args.sorted else args.item
    total = len(items)
    if (total == 1):
        print(f"You are bringing {items[0]}.")
    elif(total == 2):
        print(f"You are bringing {items[0]} and {items[-1]}.")
    else:
        comma = "" if args.no_oxford else ","
        print(f"You are bringing {', '.join(items[:-1])}{comma} and {items[-1]}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
