# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-13 17:28
# modified : 2015-07-13 17:28
"""
<++>
"""

__author__="Johann-Mattis List"
__date__="2015-07-13"

from lingpy import *

alm = Alignments('chinese.tsv', ref='cogid')

alm.align()

# write alignments to file

import json

# get a mapping from concept to cognate id
D = {}
for k in alm:
    t = alm[k,'taxon']
    c = alm[k,'cogid']
    g = alm[k,'concept']
    try:
        D[g][t] = c
    except KeyError:
        D[g] = { t : c}


with open('chinese.words.json','w') as f:
    f.write('var ALMS = '+json.dumps(alm.msa['cogid'], indent=2)+';\n')
    f.write('var REFS = '+json.dumps(D, indent=2)+';\n')

    


