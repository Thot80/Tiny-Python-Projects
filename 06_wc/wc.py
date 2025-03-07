#!/usr/bin/env python3
"""
Author : Thoth80 <jeremykessous@yahoo.fr>
Date   : 2025-02-24
Purpose: Emulate wc (word count)
"""

import argparse
import sys

# TODO How to manage flags order dependencies ?

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

    parser.add_argument('-c',
                        action='store_true',
                        help='Display Bytes count',
                        )
    parser.add_argument('-w',
                        action='store_true',
                        help='Display Words count',
                        )
    parser.add_argument('-l',
                        action='store_true',
                        help='Display Lines count',
                        )
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
            
        lines_out = f'{num_lines:8}'
        words_out = f'{num_words:8}'
        bytes_out = f'{num_bytes:8}' 
        if (args.c):
            output += f'{bytes_out}'
        if (args.w):
            output += f'{words_out}'
        if (args.l):
            output += f'{lines_out}'
        if (not args.c and not args.w and not args.l):
            output += f'{lines_out}{words_out}{bytes_out}'
        output += f' {fh.name}\n'
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
    if len(args.file) > 1:
        if (args.c):
            output += f'{total_bytes:8}'
        if (args.w):
           output += f'{total_words:8}'
        if (args.l):
            output += f'{total_lines:8}'
        if (not args.c and not args.w and not args.l):
            output += f'{total_lines:8}{total_words:8}{total_bytes:8}'
            
        output += f' total'
    print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
