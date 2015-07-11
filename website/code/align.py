# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-11 09:19
# modified : 2015-07-11 09:19
"""
Wagner-Fisher Algorithmus in Python
"""

__author__="Johann-Mattis List"
__date__="2015-07-11"

def wf_align(seqA, seqB):
    """
    Align two sequences using the Wagner-Fisher algorithm.
    """
    
    # check for empty seqs
    if not seqA or not seqB:
        return

    # store length of sequences
    m = len(seqA)+1
    n = len(seqB)+1
    
    # create matrix and traceback
    M = [[0 for i in range(n)] for j in range(m)]
    T = [[0 for i in range(n)] for j in range(m)]

    # initialize M and T
    for i in range(m): 
        M[i][0] = i
    for i in range(n):
        M[0][i] = i
    for i in range(1,m):
        T[i][0] = 1
    for i in range(1,n):
        T[0][i] = 2

    # start the main loop
    for i in range(1,m):
        for j in range(1,n):

            # get the chars
            charA = seqA[i-1]
            charB = seqB[j-1]

            # check identity
            if charA == charB:
                match = M[i-1][j-1]
            else:
                match = M[i-1][j-1] + 1

            # get the gaps
            gapA = M[i-1][j] + 1
            gapB = M[i][j-1] + 1

            # compare the stuff
            if match <= gapA and match <= gapB:
                M[i][j] = match
            elif gapA <= gapB:
                M[i][j] = gapA
                T[i][j] = 1 # don't forget the traceback
            else:
                M[i][j] = gapB
                T[i][j] = 2 # don't forget the traceback
    
    # get the edit distance
    ED = M[i][j]

    # start the traceback
    i,j = m-1,n-1

    almA,almB = [],[]

    while i > 0 or j > 0:
        if T[i][j] == 0:
            almA += [seqA[i-1]]
            almB += [seqB[j-1]]
            i -= 1
            j -= 1
        elif T[i][j] == 1:
            almA += [seqA[i-1]]
            almB += ["-"]
            i -= 1
        else:
            almA += ["-"]
            almB += [seqB[j-1]]
            j -= 1

    # reverse
    almA = almA[::-1]
    almB = almB[::-1]

    return almA,almB,ED




