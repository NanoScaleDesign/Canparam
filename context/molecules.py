#! /usr/bin/env python3
"""Context files must contain a 'main(params)' function.
The return from the main function should be the resulting text"""

def main(params):
    # Convert to list even if there's just one molecule type
    if type(params.nmols) is not list:
        params.nmols = [params.nmols]
    if type(params.liquids) is not list:
        params.liquids = [params.liquids]
    
    # Check validity
    if not hasattr(params,'liquids'):
        raise Exception('Molecule types must be specified')
    if not hasattr(params,'nmols'):
        raise Exception('Number of molecules must be specified')
    for liquid,nmols in zip(params.liquids,params.nmols):
        if type(nmols) == str:
            if liquid != 'spce' and liquid != 'tip4pice':
                raise Exception('Cannot use density calculation for molecules other than water')

    # Look for water
    iwater = None
    for imol,liquid in enumerate(params.liquids):
        if liquid.lower() == 'spce' or liquid.lower() == 'tip4pice':
            iwater = imol
            break # There can only be one specification of water

    # Convert to number of water molecules in case of use of dens(123)
    if iwater is not None:
        if type(params.nmols[iwater]) == str:
            # Assume input is dens(123)
            dens = extract_dens(params.nmols[iwater])
            vol = params.box[0] * params.box[1] * params.box[2] # A3
            vol = vol * 10.**-30 # m3
            molmass = 18. # g/mol
            molmass *= 1.6605390e-27 # kg/molecule
            params.nmols[iwater] = int(dens * vol / molmass)

    # Write out molecule informatoin
    output = ''
    for liquid,nmols in zip(params.liquids,params.nmols):
        output += '    {0} {1}\n'.format(liquid, nmols)

    return output


def extract_dens(densstr):
    dens = ''
    for char in densstr:
        if char in '1234567890':
            dens += char
    return float(dens)
