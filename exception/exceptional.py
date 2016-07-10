'''A module for demonstrating exceptions.'''

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
        print("Conversion succeeded! x =",x)
    except (ValueError, TypeError):
        return -1
