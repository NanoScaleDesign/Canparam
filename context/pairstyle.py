#!/usr/bin/env python3

def main(params):
    # Determine if tip4p water is present
    # Otherwise, use the default

    pairstyle = 'lj/cut/coul/long'

    if type(params.liquids) is not list:
        params.liquids = [params.liquids]

    for liq in params.liquids:
        if 'tip4p' in liq:
            pairstyle = 'lj/cut/tip4p/long 1 2 1 1 0.1577'
            break

    return pairstyle
