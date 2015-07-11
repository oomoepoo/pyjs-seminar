# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-11 11:27
# modified : 2015-07-11 11:27
"""
Carry out Sound-Class Based Alignment Analyses.
"""

__author__="Johann-Mattis List"
__date__="2015-07-11"


import json

def segment2class(segment, converter):
    """
    Convert a segment to a sound-class schema.
    """
    
    # erster versuch
    try:
        return converter[segment]
    except KeyError:
        # zweiter versuch
        try:
            return converter[segment[0]]
        except KeyError:
            # ansonsten, gib den "misserfolg"-character zurück
            return '0' 

def load_model(model):
    """
    Load the converter for a sound-class model.
    """
    
    # load the converter with json
    converter = json.load(open(model+'.json'))

    return converter


def segments2classes(segments, converter):
    """
    Convert a sound string to a sound-class string.
    """
    
    # check for segmented string
    if type(segments) == str:
        segments = segments.split(' ')

    # convert the segments
    classes = [segment2class(x, converter) for x in segments]

    return classes

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

def classes2segments(classes, segments):
    """
    Convert an aligned string of sound classes back to the string of segments.
    """
    
    idx = len(segments)-1
    out = []

    for i in range(len(classes)-1,-1,-1):
        print(i,classes[i])
        if classes[i] == '-':
            out += ['-']
        else:
            out += [segments[idx]]
            idx -= 1
            
    return out[::-1] 

def sca_align(stringA, stringB, model="dolgo"):
    """
    Carry out sound-class based alignment analysis.
    """
    # check for strings passed as such 
    if type(stringA) == str:
        stringA = stringA.split(' ')
        stringB = stringB.split(' ')

    # load the converter
    converter = load_model(model)

    # Konvertierung
    seqA = segments2classes(stringA, converter)
    seqB = segments2classes(stringB, converter)
    
    # Alinierung
    almA, almB, ED = wf_align(seqA, seqB)

    # Rück-Konvertierung
    outA = classes2segments(almA, stringA)
    outB = classes2segments(almB, stringB)

    return outA, outB, ED
