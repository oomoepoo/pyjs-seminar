# Sitzung 2: Automatischer Sprachvergleiche mit Python 


@data-background:LightYellow
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 2 (Tag 4)

----

#### 23.07.2015

----

### &quot;Automatischer Sprachvergleich mit Python&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Automatischer Sprachvergleich"
    * @unstroked:"Sequenzdistanzen"
    * @unstroked:"Kognatenerkennung"
    * @unstroked:"Phylogenetische Rekonstruktion"
* @unstroked:"Sprachvergleich mit LingPy"
    * @unstroked:"Eingabeformate"
    * @unstroked:"Analysen"
    * @unstroked:"Ausgabeformate"
* @unstroked:"Workflows"
    * @unstroked:"Allgemeines vorweg"
    * @unstroked:"Kognatenerkennung mit LingPy"
    * @unstroked:"Integration mit externen Tools"

---

## @head:"Automatischer Sprachvergleich"
### @subhead:"Sequenzdistanzen"

**Von Alinierungen zu Distanzwerten**

Wenn man Sequenzen (Wörter im Falle der Linguistik) aliniert hat, dann kann man auch ihre Distanz zueinander berechnen. Die ist implizit ja bereits ein Teil der Berechnung der Alinierung, und sie kann entsprechend auch einfach weiterverwendet werden, wobei man vorsichtig sein sollte, was die Aussage einer solchen Distanz betrifft.

--

## @head:"Automatischer Sprachvergleich"
### @subhead:"Sequenzdistanzen"

**Die normalisierte Levenshtein-Distanz**

Eine der bekanntesten und am häufigsten verwendeten Distanzen zwischen Strings
ist die *Levenshtein-Distanz*, die grundlegend die Anzahl der *Editier-Schritte* beschreibt, die notwendig sind, um eine Sequenz in die andere zu überführen. 
Um eine bessere Vergleichbarkeit zu gewährleisten, wird häufig neben der normalen *Levenshtein-Distanz*, die ein ganzzahliger Wert ist, auch die "normalisierte Levenshtein-Distanz" berechnet, bei der man die "normale" Distanz durch die Länge des größeren Strings teilt. 

--

## @head:"Automatischer Sprachvergleich"
### @subhead:"Sequenzdistanzen"

**Die normalisierte Levenshtein-Distanz**

<pre><code class="python" data-trim>
>>> from lingpy import *
>>> seqA = 'levensthein'
>>> seqB = 'levenschtein'
>>> d = edit_dist(seqA,seqB)
>>> d
1
>>> def norm_ed(a,b):
...     return edit_dist(a,b) / max(len(a), len(b))
...
>>> norm_ed(seqA, seqB)
0.08333333333333333
>>> edit_dist(seqA, seqB, normalized=True)
0.08333333333333333
</code></pre>

---

## @head:"Automatischer Sprachvergleich"
### @subhead:"Kognatenerkennung"

**Automatisches Erkennen von kognaten Wörtern**

Kognaten sind, daran sei noch mal erinnert, Wörter, die auf einen gemeinsamen Vorgänger zurückgehen (wie bspw. Deutsch *Hand* und English *hand*). 
Automatisch können wir eine recht einfache Heuristik entwickeln, um festzustellen, ob zwei Wörter kognat sind (was nicht heißt, dass sie das auch wirklich sind!). Wir können einfach sagen, dass, wenn immer zwei Wörter sich mehr ähneln als gewöhnlich, wir annehmen, dass diese kognat sind. Die Ähnlichkeit können wir dabei natürlich unterschiedlich definieren!

--

## @head:"Automatischer Sprachvergleich"
### @subhead:"Kognatenerkennung"

**Die Lautklassenheuristik**

Eine erste einfache Heuristik besagt, dass zwei Wörter immer dann als kognat klassifiziert werden, wenn sie in den ersten beiden Lautklassen, die Konsonanten sind, übereinstimmen ([Turchin et al. 2010](:bib:Turchin2010)).

<pre><code class="python" data-trim>
>>> seqA = sampa2uni('Tri')
>>> seqB = sampa2uni('drai')
>>> seqA, seqB 
('θri', 'drai')
>>> clsA = tokens2class(ipa2tokens(seqA), 'dolgo')
>>> clsB = tokens2class(ipa2tokens(seqB), 'dolgo')
>>> clsA = ''.join(clsA).replace('V','')
>>> clsB = ''.join(clsB).replace('V','')
>>> clsA[:2] == clsB[:2]
True
>>> clsA, clsB
('TR', 'TR')
>>> turchin(seqA, seqB)
0
>>> turchin(seqA, 'test')
1
</code></pre>

--

## @head:"Automatischer Sprachvergleich"
### @subhead:"Kognatenerkennung"

**Schwellenwerte**

Anstelle des Kriteriums von [Turchin et al. (2010)](:bib:Turchin2010) könnenwir natürlich auch andere Verfahren verwenden. Zum Beispiel können wir sagen, dass ab einem bestimmten Schwellenwert der normalisierten Levenshtein-Distanz zwei Wörter nicht mehr kognat sind:

<pre><code class="python" data-trim>
>>> def cognate(seqA, seqB, threshold=0.4):
...     if edit_dist(seqA, seqB, normalized=True) > threshold:
...         return 1
...     return 0
... 
>>> seqA = sampa2uni('t_hOxt@r')
>>> seqB = 
KeyboardInterrupt
>>> seqA = sampa2uni('t_hOxt_h@r')
>>> seqB = sampa2uni('dO:t_h@r')
>>> cognate(seqA, seqB)
</code></pre>

---

## @head:"Automatischer Sprachvergleich"
### @subhead:"Phylogenetische Rekonstruktion"

**Von Distanzen zu Bäumen**

Wenn wir ermittelt haben, welche Wörter in welchen Sprachen miteinander kognat sind, können wir Distanzen zwischen ganzen Sprachen berechnen. Dazu zählen wir einfach alle kognaten Wörter in unserem Sample und teilen dann die Anzahl der kognaten Wörter durch die Gesamt-Anzahl der Wörter und ziehen diesen Wert von 1 ab (ansonsten hätten wir eine Ähnlichkeit und keine Distanzen).

--

## @head:"Automatischer Sprachvergleich"
### @subhead:"Phylogenetische Rekonstruktion"

**Kleines Beispiel zur Distanzberechnung**

<pre><code class="python" data-trim>
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
        if i &lt; j:
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
</code></pre>

--
@data-transition:none

## @head:"Automatischer Sprachvergleich"
### @subhead:"Phylogenetische Rekonstruktion"

**Kleines Beispiel zur Distanzberechnung**

<pre><code class="shell" data-trim>
$ python distances.py
          /-english
-root----|
         |          /-german
          \edge.0--|
                    \-dutch
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Automatischer Sprachvergleich"
    * @stroked:"Sequenzdistanzen"
    * @stroked:"Kognatenerkennung"
    * @stroked:"Phylogenetische Rekonstruktion"
* @unstroked:"Sprachvergleich mit LingPy"
    * @unstroked:"Eingabeformate"
    * @unstroked:"Analysen"
    * @unstroked:"Ausgabeformate"
* @unstroked:"Workflows"
    * @unstroked:"Allgemeines vorweg"
    * @unstroked:"Kognatenerkennung mit LingPy"
    * @unstroked:"Integration mit externen Tools"

---

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Eingabeformate"

**Basisformat für Wortlisten**

<pre><code class="text" data-trim>
ID   CONCEPT     COUNTERPART   IPA         DOCULECT     COGID
1    hand        Hand          hant        German       1
2    hand        hand          hænd        English      1
3    hand        рука          ruka        Russian      2
4    hand        рука          ruka        Ukrainian    2
5    leg         Bein          bain        German       3
6    leg         leg           lɛg         English      4
7    leg         нога          noga        Russian      5
8    leg         нога          noha        Ukrainian    5
9    Woldemort   Waldemar      valdemar    German       6
10   Woldemort   Woldemort     wɔldemɔrt   English      6
11   Woldemort   Владимир      vladimir    Russian      6
12   Woldemort   Володимир     volodimir   Ukrainian    6
13    Harry       Harald        haralt      German       7
14   Harry       Harry         hæri        English      7
15   Harry       Гарри         gari        Russian      7
16   Harry       Гаррi         hari        Ukrainian    7
</code></pre>

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Eingabeformate"

**Key-Value-Erweiterung des Basisformats**

<pre><code class="text" data-trim>
@author: Potter, Harry
@date: 2012-11-07
@note: Be careful with this data, it might have been charmed...
#
ID   CONCEPT     COUNTERPART   IPA         DOCULECT     COGID    ALIGNMENT
1    hand        Hand          hant        German       1        
2    hand        hand          hænd        English      1        
3    hand        рука          ruka        Russian      2        
...  ...         ...           ...         ...          ...      ...
</code></pre>

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Eingabeformate"

**Darstellung von Alinierungen**

<pre><code class="text" data-trim>
@author: Potter, Harry
@date: 2012-11-07
@note: Be careful with this data, it might have been charmed...
#
ID   CONCEPT     COUNTERPART   IPA         DOCULECT     COGID   ALIGNMENT  
...  ...         ...           ...         ...          ...     ...  
9    Woldemort   Waldemar      valdemar    German       6       v a l - d e m a r -
10   Woldemort   Woldemort     wɔldemɔrt   English      6       w ɔ l - d e m ɔ r t 
11   Woldemort   Владимир      vladimir    Russian      6       v - l a d i m i r -
12   Woldemort   Володимир     volodimir   Ukrainian    6       v o l o d i m i r -
...  ...         ...           ...         ...          ...     ...  
</code></pre>

---

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Analysen"

**Kognatenerkennung mit LexStat**

Kognatenerkennung in LingPy lässt sich mit Hilfe des [LexStat-Moduls](http://lingpy.org/reference/lingpy.compare.html#module-lingpy.compare.lexstat) durchführen. Basierend auf einer Datei, die das oben beschriebene Eingabeformat aufweist und zwingend die Spalten "CONCEPT", "IPA", und "DOCULECT" enthalten muss, kann man mit Hilfe des LexStat-Moduls Kognaten auf verschiedene Art und Weise berechnen, diese Werte dann in Distanzen umwandeln, und aus den Distanzen auch direkt einen Baum berechnen. 

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Analysen"

**Beispiel zur Kognatenerkennung mit LexStat**

<pre><code class="python" data-trim>
>>> from lingpy import *
>>> lex = LexStat('data/harry.tsv')
>>> lex.cluster(method='turchin')
>>> lex.cluster(method='turchin')
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
>>> lex.calculate(tree, ref="turchinid")
>>> print(lex.tree.asciiArt())
                    /-English
          /edge.0--|
         |          \-German
-root----|
         |          /-Russian
          \edge.1--|
                    \-Ukrainian
</code></pre>

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Analysen"

**Alinierung von Kognatensets**

Es ist sinnvoll, die automatisch ermittelten Kognaten auch zu alinieren, da man sich so am besten vergewsissern kann, dass man auch keine falschen Kognaten ermittelt oder richtige Kognaten übersehen hat. Hierfür bietet sich das [SCA-Modul](http://lingpy.org/reference/lingpy.align.html#module-lingpy.align.sca) von LingPy an, welches als Eingabe eine Wortliste nimmt und neben den für LexStat geforderten Spalten "DOCULECT", "CONCEPT" und "IPA" eine weitere Spalte erfordert, die dem Programm mitteilt, wo die Kognaten-Identifikationsnummern sind. Normalerweise werden diese Spalten in LingPy nach der Methode beziffert, die ihnen zugrunde liegt ("turchin" == "turchinid", "sca" == "scaid", etc.), wobei der Name "cogid" gewöhnlich für eine von Experten ermittelte Kognatenzuweisung reserviert wird. 

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Analysen"

**Beispiel für die Alinierung von Kognatensets**

<pre><code class="python" data-trim>
>>> from lingpy import *
>>> alm = Alignments('data/harry.tsv', ref="cogid")
>>> alm.align()
|--------------------------- ALIGNMENTS --------------------------------|
>>> alm.output('html', filename='data/harry')
</code></pre>

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Analysen"

**Ausgabe der Daten in HTML-Format**

<iframe src="../code/data/harry.html" style="width:1000px;height:500px"></iframe>

---

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Ausgabeformate"

**Grundlegendes zu Ausgabeformaten in LingPy**

Daten in LingPy können in verschiedenste Formate exportiert werden. Grundlegend unterscheiden können wir dabei zwei Formattypen:

* Endformate, die entweder für Publikationen oder zur manuellen Untersuchung von Ergebnissen verwendet werden können (Plots, Grafiken), und
* Übergangsformate, die zur Weiterverwendung in alternativen Softwarepackungen verwendet werden können.

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Ausgabeformate"

**Spezifizieren von Ausgabeformaten in LingPy**

<pre><code class="python" data-trim>
# grundlegenes Format des Kommandos
wordlist.output(DTYPE, filename=NAME)
# Beispiele
## Exportiere nach Phylip (Distanzformat)
wordlist.output('dst', filename="harry")
## Exportiere nach Nexus (Charakterformat)
wordlist.output('paps.nex', filename="harry")
## Exportiere nach HTML (individuelles LingPy-Format)
wordlist.output('html', filename="harry")
## Exportiere den Baum in Newick-Format
wordlist.output('nwk', filename="harry")
## Exportiere zum LingPy-Wordlist-Format
wordlist.output('tsv', filename='harry')
</code></pre>

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Ausgabeformate"

**Beispiele für die Ausgabeformate**

Newick-Format:
<pre><code class="text">(((English,German),Russian),Ukrainian);</code></pre>
Phylip-Format:
<pre><code class="text"> 4
English    0.00 0.25 0.50 0.50
German     0.25 0.00 0.50 0.50
Russian    0.50 0.50 0.00 0.00
Ukrainian  0.50 0.50 0.00 0.00</code></pre>

--

## @head:"Sprachvergleich mit LingPy"
### @subhead:"Ausgabeformate"

**Beispiele für die Ausgabeformate**


Nexus-Format:
<pre><code class="text" data-trim>#NEXUS
BEGIN DATA;
DIMENSIONS ntax=4 NCHAR=7;
FORMAT DATATYPE=STANDARD GAP=- MISSING=0 interleave=yes;
MATRIX
English   1001011
German    1010011
Russian   0100111
Ukrainian 0100111
;
END;</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Automatischer Sprachvergleich"
    * @stroked:"Sequenzdistanzen"
    * @stroked:"Kognatenerkennung"
    * @stroked:"Phylogenetische Rekonstruktion"
* @stroked:"Sprachvergleich mit LingPy"
    * @stroked:"Eingabeformate"
    * @stroked:"Analysen"
    * @stroked:"Ausgabeformate"
* @unstroked:"Workflows"
    * @unstroked:"Allgemeines vorweg"
    * @unstroked:"Kognatenerkennung mit LingPy"
    * @unstroked:"Integration mit externen Tools"

---

## @head:"Workflows"
### @subhead:"Allgemeines vorweg"

**Workflows in LingPy**

Mit Hilfe der Funktionen, die LingPy bietet, lassens ich komplette Workflows
zum automatisierten Vergleich von Sprachen entwickeln. Das ist nicht immer einfach,
da nur ein Bruchteil der Möglichkeiten von LingPy auch ordentlich dokumentiert ist.
Wir wollen aber trotzdem versuchen, ein allgemeines Template zu erstellen, so dass
es möglich ist, dieses an individuelle Daten anzupassen und weiterzuverwenden.

--

## @head:"Workflows"
### @subhead:"Allgemeines vorweg"

**Workflows zum Sprachvergleich**

<table>
<tr>
<td style="vertical-align:top">
<a href="img/workflow_basic.svg"><img src="img/workflow_basic.svg" style="width:300px" alt="workflow" /></a>
</td>
<td style="vertical-align:top">Dieser Workflow kann als allgemeines Konstrukt der von rohen Daten bis hin zu Rekonstruktionen führt, angesehen werden. Nicht alle Schritte können derzeit schon automatisch ausgeführt werden. Wir beschränken uns daher auf die Schritte, die von den Wortlist-Daten hin zu den Alinierungen führen.</td>
</tr></table>

---

## @head:"Workflows"
### @subhead:"Kognatenerkennung mit LingPy"

**Daten**

Wir nehmen einen Datensatz zu den chinesischen Dialekten, der als TSV-Datei 
im LingPy Format vorliegt (File "[chinese.tsv](https://github.com/LinguList/pyjs-seminar/blob/master/website/code/data/chinese.tsv)").

Die Datei enthält neben den tabularen Daten auch eine JSON-Spezifikation (eine Formaterweiterung in LingPy, die es erlaubt, JSON-Daten mit einzubinden. Wir ignorieren diese Daten jedoch in diesem Zusammenhang.

--

## @head:"Workflows"
### @subhead:"Kognatenerkennung mit LingPy"

**Der Workflow**

Der Workflow gliedert sich in drei Schritte:

* Kognatenberechnung:
    * Einlesen der Datei in LingPy (LexStat Modul)
    * Berechnen von Kognatensets mit Hilfe von LexStat
    * Auslesen der Datei mit den neu berechneten Daten in TSV-Format
* Berechnen und Plotten eines phylogenetischen Baums
* Berechnung der Alinierungen
    * Einlesen der Datei in LingPy (Alignments Modul)
    * Berechnen der Alinierungen mit Hilfe von Alignments
    * Auslesen der Datei in HTML-Format

--

## @head:"Workflows"
### @subhead:"Kognatenerkennung mit LingPy"

**Der Code**

<pre><code class="python" data-trim>
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
## 1.2 Plotten des Baums
from lingpy.convert.plot import plot_tree
plot_tree(lex.tree, degree=160, filename="data/chinese_tree", fileformat="svg")
## 1.3 Schreiben der Distanz-Daten
lex.output('dst', filename="data/chinese_distances")
# Schritt 3
## 1.1 Einlesen der Daten
alm = Alignments('data/chinese_lexstat.tsv', ref="scaid")
## 1.2 Alinierung
alm.align()
## 1.3 Auslesen der Daten in HTML
alm.output('html', filename='data/chinese_alignments')
</code></pre>

--

## @head:"Workflows"
### @subhead:"Kognatenerkennung mit LingPy"

**Die Ergebnisse: Der Baum**

[<img src="../code/data/chinese_tree.svg" alt="tree" style="width:700px" />](../code/data/chinese_tree.svg)

--

## @head:"Workflows"
### @subhead:"Kognatenerkennung mit LingPy"

**Die Ergebnisse: Die Alinierungen**

<iframe src="../code/data/chinese_alignments.html" style="width:1000px;height:500px"></iframe>

---

## @head:"Workflows"
### @subhead:"Integration mit externen Tools"

**Einlesen der Daten in Splitstree**

Mit [SplitsTree](http://splitstree.org) können wir Netzwerke aus Distanzmatrizzen berechnen.
Da wir die Distanzmatrix ja bereits exportiert haben, genügt es, wenn SplitStree erfolgreich installiert wurde, diese entweder direkt als Textdatei einzulesen, oder den Inhalt der Datei [chinese_distances.dst](ttps://github.com/LinguList/pyjs-seminar/blob/master/website/code/data/chinese_distances.dst) zu kopieren und in den Editor von SplitsTree zu pasten.


--

## @head:"Workflows"
### @subhead:"Integration mit externen Tools"

**Das Neighbor-Net der chinesischen Daten**

[<img src="../code/data/chinese_network.svg" alt="network" style="width:400px" />](../code/data/chinese_network.svg)


---

## @head:"Agenda 2015"

* @stroked:"Automatischer Sprachvergleich"
    * @stroked:"Sequenzdistanzen"
    * @stroked:"Kognatenerkennung"
    * @stroked:"Phylogenetische Rekonstruktion"
* @stroked:"Sprachvergleich mit LingPy"
    * @stroked:"Eingabeformate"
    * @stroked:"Analysen"
    * @stroked:"Ausgabeformate"
* @stroked:"Workflows"
    * @stroked:"Allgemeines vorweg"
    * @stroked:"Kognatenerkennung mit LingPy"
    * @stroked:"Integration mit externen Tools"


---
@data-background:#000000

<p style="font-size:120px;color:white;font-weight:bold;">
<code class="python">>>> 3 - 2</code>
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
Ende der zweiten Sitzung
</p>

