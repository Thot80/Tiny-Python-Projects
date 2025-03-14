#!/usr/bin/env python3
"""
Author : Thoth80 <jeremykessous@yahoo.fr>
Date   : 2025-02-12
Purpose: Howler (upper-cases input)
"""

import argparse
import os
import io
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type=str,
                        help='Output filename',
                        default='',
                        )
    
    parser.add_argument('--ee',
                        action='store_true',
                        help='Output in lower case',
                        )
    
    #TODO Add functionnality to write in multiples output files 
    args = parser.parse_args()
    
    # In both case, filr or text passed, we want to return a file handler as args to read it line by line (this allows to deal with large files)
    # sys.stdout is always open, no concise way i can think of, wrap loop in if and add else for stdout....
    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')
    
    return args 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.lower()) if args.ee else out_fh.write(line.upper())
    out_fh.close()

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
