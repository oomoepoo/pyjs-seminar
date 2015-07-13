# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-13 14:20
# modified : 2015-07-13 14:20
"""
<++>
"""

__author__="Johann-Mattis List"
__date__="2015-07-13"

from lingpy import *

# die daten
data = dict(
    german = ['hant', 'fuːs', 'kɔp͡f'],
    english = ['hænd', 'fʊt', 'hɛd'],
    dutch = ['hant', 'vut', 'kɔp']
    )

# die sprachen
taxa = ['german', 'english', 'dutch']

# die distanzmatrix
matrix = [[0 for i in range(3)] for j in range(3)]

for i,k in enumerate(taxa):
    for j,l in enumerate(taxa):
        
        # wir müssen nur ein mal pro sprachpaar vergleichen
        if i < j:
            score = 0
            for seqA, seqB in zip(data[k], data[l]):
                score += edit_dist(seqA, seqB, normalized=True)
            score = score / 3
            matrix[i][j] = score
            matrix[j][i] = score

# der baum
tree = upgma(matrix, taxa)

# ascii-art mit Hilfe von LingPy
print(Tree(tree).asciiArt())

