# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-07-12 13:45
# modified : 2015-07-12 13:45
"""
Aliniere die germanischen Daten und exportiere sie zu HTML.
"""

__author__="Johann-Mattis List"
__date__="2015-07-12"


# wir importieren LingPy
from lingpy import *

# define a string that stores the html-data-information
html = '<html><head><title>Alignment Data</title></head><body>'
html += '<h2>Select your file</h2><ul>'

# Alle Daten liegen in einem Ordner "germanic-data"
# Die Dateiendungen sind regelmäßig und beginnen bei 369 und enden bei 479
for i in range(369,480):

    msa = MSA('germanic-data/phonalign_'+str(i)+'.msa')

    # export of html, specific filename and new folder for output
    msa.output('html', filename='germanic-data/germanic_'+str(i))

    # write the hyperlink to the file
    html += '<li><a href="germanic-data/germanic_'+str(i)+'.html">File '\
            +msa.seq_id+'</a></li>'

html += '</ul></body></html>'

# open file and write data into there
with open('germanic-data.html', 'w') as f:
    f.write(html)
