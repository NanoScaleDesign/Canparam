#! /usr/bin/env python3
"""Context files must contain a 'main' function.
The return from the main function should be the resulting text"""

def main(params):
    if hasattr(params,'gpu'):
        if params.gpu == 'on':
            return """package gpu 1
newton off"""
    return ''
