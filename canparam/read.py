#!/usr/bin/env python3

def main(fname):
    """Load parameters
Usage: load_params.main(filename)"""

    with open(fname,'r') as fin:
        lines = fin.readlines()

    commandlist = {}
    for line in lines:
        sline = line.split()
        nvars = _number_of_vars(sline)
        if nvars >= 1:
            variable = sline[0]

            valuelist = []
            for val in sline[1:nvars+1]: # +1 because we don't include variable name
                valuelist.append(val)
                valuelist[-1] = _check_var_type(valuelist[-1])

            if len(valuelist) == 1: valuelist = valuelist[0]
            commandlist[variable] = valuelist

    return _Struct(**commandlist)


def _number_of_vars(line):
    """Count the number of variables in the line, excluding comments denoted by
 # and the first word which is expected to be the variable name"""

    ncommands = 0
    for word in line:
        if word[0] != '#':
            ncommands += 1
        else:
            break
    ncommands -= 1 # Ignore first word which must be the variable name
    if ncommands < 0:
        ncommands = 0 # If this is just a comment line, there's no variable name

    return ncommands


def _check_var_type(var):
    # Check for variable type
    if var.lower() == 'true':
        var = True
    elif var.lower() == 'false':
        var = False
    elif var.lower() == 'none':
        var = None
    else: # It's not boolean
        try:
            var = int(var)
            isint = True
        except ValueError: # Not an int
            isint = False
        if not isint:
            try:
                var = float(var)
            except ValueError: # Not a real either
                # Then we give up and treat it as a string
                pass

    return var


class _Struct(object): # http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
    def __init__(self, **entries): 
        self.__dict__.update(entries)
