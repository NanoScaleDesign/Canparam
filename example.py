#! /usr/bin/env python3

import canparam.read as cpr
params = cpr.main('parameters.dat')

import canparam.write as cpw
template = cpw.readfile('template.dat')
keys = cpw.getkeys(template)

text = cpw.formattext(template,keys,params)

with open('template.dat.filled','w') as fout:
    fout.write(text)
