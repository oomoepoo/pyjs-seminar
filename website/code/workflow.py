# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-13 16:00
# modified : 2015-07-13 16:00
"""
Berechne Kognaten, Bäume und Alignments der chinesischen Dialektdaten.
"""

__author__="Johann-Mattis List"
__date__="2015-07-13"

from lingpy import *

# Schritt 1
## 1.1 Einlesen der Daten
lex = LexStat('data/chinese.tsv')
## 1.2 Kognatenerkennung
lex.cluster(method='sca', threshold=0.4)
## 1.3 Auslesen der Daten
lex.output('tsv', filename='data/chinese_lexstat', ignore='all')

# Schritt 2
## 1.1 Berechnen des Baums
lex.calculate('tree', ref="scaid") # scaid sind die automatischen kognaten
lex.output('dst', filename="data/chinese_distances")
## 1.2 Plotten des Baums
from lingpy.convert.plot import plot_tree
plot_tree(lex.tree, degree=160, filename="data/chinese_tree", fileformat="svg")

# Schritt 3
## 1.1 Einlesen der Daten
alm = Alignments('data/chinese_lexstat.tsv', ref="scaid")
## 1.2 Alinierung
alm.align()
## 1.3 Auslesen der Daten in HTML
alm.output('html', filename='data/chinese_alignments')


