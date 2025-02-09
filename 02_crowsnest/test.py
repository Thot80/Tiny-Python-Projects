#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
win_prg = f'python3 {prg}'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the {} bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{win_prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{win_prg} {word}')
        assert out.strip() == template.format('a', word, 'larboard')


# --------------------------------------------------
def test_consonant_title():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{win_prg} {word.title()}')
        assert out.strip() == template.format('A', word.title(), 'larboard')


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{win_prg} {word.upper()}')
        assert out.strip() == template.format('A', word.upper(), 'larboard')

# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{win_prg} {word}')
        assert out.strip() == template.format('an', word, 'larboard')


# --------------------------------------------------
def test_vowel_title():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{win_prg} {word.title()}')
        assert out.strip() == template.format('An', word.title(), 'larboard')
        

# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{win_prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper(), 'larboard')
        
def test_starboard():
    for word in consonant_words:
        out = getoutput(f'{win_prg} {word} --starboard=True')
        assert out.strip() == template.format('a', word, 'starboard')