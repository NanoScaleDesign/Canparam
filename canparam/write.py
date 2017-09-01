#!/usr/bin/evn python3

def readfile(fname):
    with open(fname,'r') as fin:
        text = fin.read()
    return text


def getkeys(text):
    record = False
    varlist = []
    for i,char in enumerate(text):
        if char == '{':
            record = True
            varname = ''
        elif char == '}':
            if record:
                if varname not in varlist:
                    varlist.append(varname)
                record = False
        elif record:
            varname += char
    return varlist


def formattext(text,keys,params):
    keydict = {}
    import importlib
    import context
    for key in keys:
        try:
            module = importlib.import_module('context.{0}'.format(key))
        except ImportError: # Try local directory
            module = importlib.import_module(key)
        value = module.main(params)
        keydict[key] = value

    formattedtext = text.format(**keydict)
    return formattedtext

