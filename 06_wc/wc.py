#!/usr/bin/env python3
"""
Author : Thoth80 <jeremykessous@yahoo.fr>
Date   : 2025-02-24
Purpose: Emulate wc (word count)
"""

import argparse
import sys



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt', encoding='UTF-8'),
                        default=[sys.stdin],
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_bytes = 0
    output = ''    
    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        output += f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}\n'
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
    if len(args.file) > 1:
        output += f'{total_lines:8}{total_words:8}{total_bytes:8} total'
    print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
