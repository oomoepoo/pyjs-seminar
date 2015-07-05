# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-05 12:59
# modified : 2015-07-05 12:59
"""
Python script zum testen, ob auch alle Programme ordnungsgemäß installiert
wurden.
"""

__author__="Johann-Mattis List"
__date__="2015-07-05"

import numpy
import scipy
import matplotlib
import networkx 
import lingpy
from urllib.request import urlopen

# we download a website, if this work, everything, that is, lingpy and the
# like, should have been properly installed
data = urlopen('http://lingulist.de/pyjs/code/response_1.html').read().decode('utf-8').split('\n')
sentence = ' '.join([data[x] for x in range(0,16,2)])
print(sentence+'!')
input('CTRL-C to quit')


