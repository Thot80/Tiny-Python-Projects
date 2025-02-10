#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'
win_prg = f'python3 {prg}'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{win_prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'{win_prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{win_prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{win_prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{win_prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{win_prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected
    
# --------------------------------------------------
def test_no_oxford_comas():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{win_prg} {arg} --no-oxford')
    expected = ('You are bringing apples, bananas, cherries and dates.')
    assert out.strip() == expected