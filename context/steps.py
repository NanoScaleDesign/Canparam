#! /usr/bin/env python3
"""Context files must contain a 'main' function.
The return from the main function should be the resulting text"""

def main(params):
    if hasattr(params,'time'):
        # 1e6 steps per ns
        steps = int(params.time * 1e6)
    else:
        steps = 10000
    return steps



