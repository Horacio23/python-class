'''A module for demonstrating exceptions.'''

import sys

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
        print("Conversion succeeded! x =",x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"\
                .format(str(e)),
                file=sys.stderr)
        raise
