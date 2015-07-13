# Sitzung 1: Sprachvergleiche in der historischen Linguistik 


@data-background:LightYellow
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 1 (Tag 4)

----

#### 23.07.2015

----

### &quot;Linguistischer Hintergrund zum Sprachvergleich&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Phylogenetische Rekonstruktion"
    * @unstroked:"Innere und äußere Sprachgeschichte"
    * @unstroked:"Stammbäume und Wellen"
    * @unstroked:"Darstellung und Analyse"
* @unstroked:"Lexikostatistik"
    * @unstroked:"Hintergrund und Grundannahmen"
    * @unstroked:"Praktische Umsetzung"
    * @unstroked:"Kritik"
* @unstroked:"Computergestützte Rekonstruktion"
    * @unstroked:"Komparanda"
    * @unstroked:"Algorithmen"
    * @unstroked:"Formate"

---

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Innere und äußere Sprachgeschichte"

**Georg von der Gabelentz (1840-1893) und die Sprachgeschichte**

> Der Zweig der Sprachforschung, der uns hier beschäftigt, hat es zunächst mit
> den trockensten Einzelthatsachen zu thun: Sind die Sprachen A und B
> miteinander verwandt, und in welchem Grade? Giebt es dieses Wort oder jene
> Form in der und der Sprache oder in der und der Zeit der Sprachgeschichte? [...] Welche Gesetzmässigkeit herrscht in den lautlichen
> Abweichungen? Besteht im einzelnen Falle Urgemeinschaft oder Entlehnung? [(Gabelentz 1891:
> 145)](:bib:Gabelentz1891)

--
@data-transition:none

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Innere und äußere Sprachgeschichte"

**Georg von der Gabelentz (1840-1893) und die Sprachgeschichte**

> Alles das klingt und ist auch wirklich sehr trocken. Was die menschliche Re-
> de im Innersten bewegt, was sonst die Wissenschaft von den Sprachen der Völker zu
> einer der lebensvollsten macht, das tritt hier zunächst zurück: nur einige ihrer Ausläufer ranken in das Seelen- und Sittenleben der Völker hinüber. Der einzelsprachliche
> Forscher kann gar nicht schnell genug die fremde Sprache in’s eigene Ich aufnehmen:
> der Sprachhistoriker steht draussen vor seinem Gegenstande: hier der Anatom, da der
> Cadaver. [(Gabelentz 1891: 145)](:bib:Gabelentz1891)

--
@data-transition:none

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Innere und äußere Sprachgeschichte"

**Georg von der Gabelentz (1840-1893) und die Sprachgeschichte**

> Wir werden, um Missverständnisse zu vermeiden, gut thun, zwischen äusserer und
> innerer Sprachgeschichte zu unterscheiden. Die äussere Geschichte einer Sprache ist
> die Geschichte ihrer räumlichen und zeitlichen Verbreitung, ihrer Verzweigungen und
> etwaigen Mischungen (Genealogie). Die innere Sprachgeschichte erzählt und sucht
> zu erklären, wie sich die Sprache in Rücksicht auf Stoff und Form allmählich verändert
> hat. [(Gabelentz 1891: 146)](:bib:Gabelentz1891)

---

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Bäume**

August Schleicher war eine herausragende Persönlichkeit in der Geschichte der Linguistik.
Wir verdanken ihm insbesondere die sogenannte *Stammbaumtheorie*, die er in zwei frühen Werken
erstmals im Jahre 1853 veröffentlichte ([Schleicher 1853a](:bib:Schleicher1853), [Schleicher 1853b](:bib:Schleicher1853a)). Schleichers
Theorie zur äußeren Sprachgeschichte war wahrscheinlich direkt beeinflusst von František
Čelakovský (1799 – 1852), den er während einer Professur in Prag kennengelernt hatte,
und der noch vor Schleicher einen ersten Stammbaum der slawischen Sprachen veröf-
fentlichte ([Čelakovský 1853](:bib:Celakovsky1853)).

--

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Bäume**

> Die ältesten teilungen des indogermanischen bis zum entstehen der grundsprachen
> der den sprachstamm bildenden sprachfamilien laßen sich durch folgendes schema
> anschaulich machen. Die länge der linien deutet die zeitdauer an, die entfernung der-
> selben von einander den verwantschaftsgrad. ([Schleicher 1861: 6](:bib:Schleicher1861))

--
## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Bäume**

[<img style="width:600px" src="img/schleicher1861.jpg" alt="schleicher" />](img/schleicher1861.jpg)

[Darstellung aus: Schleicher (1861: 6)](:bib:Schleicher1861)

--

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Wellen**

Nicht lange, nachdem August Schleicher seine berühmte Stammbaumtheorie erstmals
postuliert hatte, regte sich Widerspruch in den Kreisen der Indogermanisten und histori-
schen Linguisten. Am bekanntesten ist in diesem Zusammenhang das Werk von Johannes
Schmidt (1843 – 1901), der die Stammbaumtheorie verwarf, und an ihrer Stelle seine nicht
minder berühmte *Wellentheorie* propagierte.

--

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Wellen**

> Ich möchte an seine
> stelle das bild der welle setzen, welche sich in concentrischen mit der entfernung vom
> mittelpunkte immer schwächer werdenden ringen ausbreitet. Dass unser sprachgebiet keinen kreis bildet, sondern höchstens einen kreissector, dass die ursprünglichste
> sprache nicht im mittelpunkte, sondern an dem einen ende des gebietes ligt, tut nichts
> zur sache. Mir scheint auch das bild einer schiefen vom sanskrit zum keltischen in
> ununterbrochener linie geneigten ebene nicht unpassend. ([Schmidt 1872: 27](:bib:Schmidt1872))

--

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Netze und anderes Gewirr**


Das größte Problem von Schmidts Wellentheorie war, das niemand genau wusste, wie er
die äußere Sprachgeschichte denn nun schematisch darstellen sollte. Und so finden wir im
Laufe der Geschichte eine Vielzahl von Versuchen zur Visualisierung der Wellentheorie.

--

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Stammbäume und Wellen"

**Netze und anderes Gewirr**

[<img style="width:600px" src="img/netze.png" alt="schleicher" />](img/netze.png)

---

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Darstellung und Analyse"

**Darstellung von Daten und Darstellung von Geschichte**


Wir müssen unterscheiden zwischen Schemata (seien es Wellen oder Bäume) zur
Darstellung von Daten, und Schemata zur Darstellung von Geschichte (vgl. die
Unterscheidung zwischen data-display und evolutionary in [Morrison 2011:
42f](:bib:Morrison2011)).

--

@data-transition:none

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Darstellung und Analyse"

**Darstellung von Daten und Darstellung von Geschichte**

Schleichers Baum von 1861 ist dabei ein klares
Beispiel für ein Schema, das den Anspruch hat, ein geschichtliches Schema zu
sein, während die Beispiele für die Visualisierung der Wellentheorie wohl eher
als Datendarstellungsschemata bezeichnet werden sollten, da sie nicht für sich
in Anspruch nehmen, äußere Sprachgeschichte zu modellieren.  Schemata zur
Darstellung von Daten können unter Umständen in Schemata zur Darstellung von
Geschichte überführt werden, jedoch hängt die Überführbarkeit davon ab, ob die
Daten die Rekonstruktion von Geschichte auch erlauben.

--

## @head:"Phylogenetische Rekonstruktion"
### @subhead:"Darstellung und Analyse"

**Welche Daten sind es, die auf die Geschichte schließen lassen?**

> Im ganzen ist also nur wenig, was aus den spezielleren Übereinstimmungen
> zwischen einzelnen von den acht Hauptgruppen [...] mit grösserer Wahrscheinlichkeit entnommen werden kann. Und
> jedenfalls treten [...] nirgends speziellere Gemeinsamkeiten, die als
> gemeinsame Neuerungen erscheinen, in so grosser Anzahl entgegen, dass man auf
> Grund derselben die betreffenden Sprachzweige in derselben Art zu Einheiten
> zusammenschliessen dürfte [...]. ([Brugmann 1904[1970]: 21f](:bib:Brugmann1904))

---

## @head:"Agenda 2015"

* @stroked:"Phylogenetische Rekonstruktion"
    * @stroked:"Innere und äußere Sprachgeschichte"
    * @stroked:"Stammbäume und Wellen"
    * @stroked:"Darstellung und Analyse"
* @unstroked:"Lexikostatistik"
    * @unstroked:"Hintergrund und Grundannahmen"
    * @unstroked:"Praktische Umsetzung"
    * @unstroked:"Kritik"
* @unstroked:"Computergestützte Rekonstruktion"
    * @unstroked:"Komparanda"
    * @unstroked:"Algorithmen"
    * @unstroked:"Formate"

---

## @head:"Lexikostatistik"
### @subhead:"Hintergrund und Grundannahmen"

**Hintergrund**

Die Lexikostatistik stellt ein statistisch basiertes Verfahren zur Ermittlung von Verwandt-
schaftsbeziehungen zwischen Sprachen (und damit zur phylogenetischen Rekonstrukti-
on) dar. Sie wurde von Morris Swadesh (1909 – 1967) in einer Reihe von Artikeln zu
Beginn der 50er Jahre des 20. Jahrhunderts vorgestellt und weiterentwickelt ([Swadesh
1950](:bib:Swadesh1950), [Swadesh 1952](:bib:Swadesh1952), [Swadesh 1955](:bib:Swadesh1955)). In der Folgezeit mehrte sich jedoch die Kritik an
der Methode ([Bergsland und Vogt 1962](:bib:Bergsland1962), [Hoijer 1956](:bib:Hoijer1956), [Rea 1973](:bib:Rea1973)) und kam am Ende aus
der Mode.

--

## @head:"Lexikostatistik"
### @subhead:"Hintergrund und Grundannahmen"

**Hintergrund**

Grundsätzlich werden im Rahmen der Lexikostatistik historisch relevante Ge-
meinsamkeiten zwischen Sprachen ausgezählt. Die zugrunde liegenden Zahlen können
dann weiterverwendet werden, um genealogische Bäume automatisch zu rekonstruieren,
oder um (unter der Annahme konstanten Wandels) Sprachspaltungszeitpunkte zu ermit-
teln. Die Methode erlebte zu Beginn des 21. Jahrhunderts eine Wiedergeburt im Rahmen
neuer quantitativer biologischer Ansätze, mit deren Hilfe genealogische Bäume automa-
tisch aus spezifischen Sprachdaten gewonnen werden können ([Atkinson und Gray 2006](:bib:Atkinson2006),
[Gray und Atkinson 2003](:bib:Gray2003)).

--

## @head:"Lexikostatistik"
### @subhead:"Hintergrund und Grundannahmen"

**Grundannahmen**

Die Grundannahmen der Lexikostatistik wurden in einer Vielzahl von Arbeiten besprochen
([Gudschinsky 1956](:bib:Gudschinsky1956), [Sankoff 1969](:bib:Sankoff1969)). 
Sie lassen sie sich in etwa
wie folgt zusammenfassen (vgl. [Geisler und List im Erscheinen](http://lingulist.de/jump.php?paper=Geisler2014&href=documents/beautiful_trees.pdf)):

* The lexicon of every human language contains words which are relatively resistant
to borrowing and relatively stable over time due to the meaning they express: these
words constitute the *basic vocabulary* of languages.

* *Shared retentions* in the basic vocabulary of different languages reflect their degree
of *genetic relationship*.

---

## @head:"Lexikostatistik"
### @subhead:"Praktische Umsetzung"

**Die praktischen Arbeitsschritte**

1. **Compilation:** Compile a list of basic vocabulary items (a Swadesh-list).
2. **Translation:** Translate the items into the languages that shall be investigated.
3. **Cognate Judgments:** Search the language entries for cognates.
4. **Coding:** Convert the cognate information into a numerical format.
5. **Computation:** Perform a computational analysis (cluster analysis, tree calculation) of the numerical data, which allows to make conclusions regarding the phylogeny of the languages under investigation.

--

## @head:"Lexikostatistik"
### @subhead:"Praktische Umsetzung"

**Diagnostische Testlisten im [Concepticon](http://concepticon.clld.org)**

<iframe src="http://concepticon.clld.org" style="width:1100px;height:500px"></iframe>

---

## @head:"Lexikostatistik"
### @subhead:"Kritik"

**Wichtigste Kritikpunkte in der Literatur**

* **Entlehnung:** Unentdeckte Entlehnungen können die Ergebnisse verfälschen.
* **Aussagekraft:** Lexikalische Ersetzung ist als Prozess nicht aussagekräftig für Sprach-
geschichte.
* **Fehleranfälligkeit:** Die Methode ist fehleranfällig, da die Daten auf eine problemati-
sche Weise erstellt werden.

--

## @head:"Lexikostatistik"
### @subhead:"Kritik"

**Entscheidender Kritikpunkt**

Neuere Vergleiche
haben dabei zeigen können, dass die Daten, die von Forscherteams unabhängig produ-
ziert werden, derartig große Unterschiede aufweisen, dass dies zu Unterschieden von über
30% in von den Daten automatisch berechneten Baumtopologien führt ([Geisler und List im Erscheinen](http://lingulist.de/jump.php?paper=Geisler2014&href=documents/beautiful_trees.pdf)). 
Die größten Probleme liegen dabei weniger im Bereich der Kognatenzuweisungen
(Schritt 3, obwohl auch dieser problematisch ist), sondern bereits im Bereich der Überset-
zung (Schritt 2).

--

@data-transition:none

## @head:"Lexikostatistik"
### @subhead:"Kritik"

**Entscheidender Kritikpunkt**

Bereits hier zeigen sich große Unterschiede zwischen unabhängig
erstellten Datensätzen, die zeigen, dass mangelnde Kompetenz der Forscher in den Ein-
zelsprachen, aber auch mangelnde Beschreibung der Konzepte in den Konzeptlisten, zu
einer Vielzahl von Unterschieden bereits in den Ausgangsdaten führen können.

---

## @head:"Agenda 2015"

* @stroked:"Phylogenetische Rekonstruktion"
    * @stroked:"Innere und äußere Sprachgeschichte"
    * @stroked:"Stammbäume und Wellen"
    * @stroked:"Darstellung und Analyse"
* @stroked:"Lexikostatistik"
    * @stroked:"Hintergrund und Grundannahmen"
    * @stroked:"Praktische Umsetzung"
    * @stroked:"Kritik"
* @unstroked:"Computergestützte Rekonstruktion"
    * @unstroked:"Komparanda"
    * @unstroked:"Algorithmen"
    * @unstroked:"Formate"

---

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Komparanda"

**Distanzbasierte Ansätze**

Aus den Daten werden Distanzwerte zwischen den zu vergleichenden Taxa (in
unserem Falle Sprachen) abgeleitet. Distanzwerte sind dabei beliebige Zahlen
zwischen $0$ (Identität der Taxa) und $\infty$ (Nichtidentität der Taxa), wobei
Taxa, die weiter voneinander entfernt sind, einen größeren Distanzwert
zugewiesen bekommen, als Taxa, die einander näher liegen.

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Komparanda"

**Charakterbasierte Ansätze**

Die Daten werden nicht in Distanzmatrizzen transformiert.
Stattdessen wird jedes Taxon in Bezug auf eine Reihe von Eigenschaften charakterisiert.
Für jede dieser Eigenschaften kann ein Taxon dabei verschiedene Zustände
aufweisen. Die einfachste Zustandsbeschreibung ist dabei die Anwesenheit oder Ab-
wesenheit der jeweiligen Eigenschaft (dargestellt in einer Binärmatrix). Komplexere
Zustände können den Taxa jedoch ebenfalls zugewiesen werden.

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Komparanda"

**Distanzbasierte versus charakterbasierte Ansätze**

[<img src="img/perspective.png" alt="distchar" style="width:1000px" />](img/perspective.png)

---

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Algorithmen"

**Allgemeines Vorweg**

Um aus den in Distanzform oder Charakterform kodierten Daten mit Hilfe des Computers einen Stammbaum abzuleiten, müssen diese geclustert werden. Hierzu sind
in der Biologie verschiedene Verfahren entwickelt worden. Es gibt eine Vielzahl
verschiedenster Softwareprogramme, welche diese Aufgabe erfüllen. Den einzelnen Anwendungen innerhalb dieser Software liegen dabei verschiedene Algorithmen zugrunde, welche aus den Daten sukzessive einen Baum erzeugen, oder aus
einer Vielzahl möglicher Bäume den wahrscheinlichsten Baum ermitteln. 

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Algorithmen"

* **Neighbor-Joining:** Clusterverfahren für Distanzdaten, entwickelt von [Saitou and Nei (1987)](:bib:Saitou1987),
  welches sich insbesondere deshalb großer Beliebtheit erfreut, weil es eine
  sehr geringe Laufzeit hat. Um einen schnellen Überblick über die Daten zu
  bekommen, ist es daher sehr gut geeignet.
* **Likelihood-Verfahren:** Verfahren für Charakterdaten, 
  die auf stochastischen Verfahren beruht und entweder alle 
  möglichen Bäume auf ihre Wahrscheinlichkeit vergleichen ("maximum likelihood", [Nunn 2011:33-35](:bib:Nunn2011)),
  oder ein möglichst großes Sample "guter" Bäume automatisch schätzt ("bayesian methods", [Nunn 2011:35-38](:bib:Nunn2011)). 
* **Maximale Parsimonie:** Verfahren, welches den evolutionären Baum errechnet, 
  der am wenigsten evolutionären Wandel benötigt, um die Daten zu erklären ([Nunn 2011:30-33](:bib:Nunn2011)). 

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Algorithmen"

**Software**

* [LingPy](http://lingpy.org): Bietet distanzbasierte Clusterverfahren, unter anderem Neighbor-Joining ([Saitou und Nei 1987](:bib:Saitou1987)) und UPGMA ([Sokal und Michener 1958](:bib:Sokal1958)).
* [MrBayes](http://mrbayes.sourceforge.net): Bietet bayesianische Methoden, die vor allem in der Biologie verwendet werden ([Ronquist et al. 2009](:bib:Ronquist2009)).
* [SplitsTree](http://splitstree.org): Bietet distanzbasierte Clusterverfahren, aber vor allem auch distanzbasierte Netzwerkanalysen, wie zum Beispiel NeighborNet ([Bryant und Moulton 2002](:bib:Bryant2002)).

---

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Allgemeines Vorweg**

Als Eingabedaten werden in den phylogenetischen Analysen im Rahmen der histo-
rischen Linguistik zumeist Swadesh-Listen (vgl. [Swadesh 1950](:bib:Swadesh1950), [1952](:bib:Swadesh1952), [1955](:bib:Swadesh1955)) verwendet. Jedes Item (“Bedeutungsslot”) wird dabei zunächst als Charakter angesehen. Diesem wird für jede Sprache ein Zustand zugewiesen, wobei der Zustand als
identisch kodiert wird, wenn die jeweiligen Spracheinträge kognat sind.

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Distanzberechnung aus Swadeshlisten**

[<img style="width:1000px" src="img/cognates-1.svg" alt="schleicher" />](img/cognates-1.svg)

--

@data-transition:none

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Distanzberechnung aus Swadeshlisten**

[<img style="width:1000px" src="img/distance-tree.png" alt="schleicher" />](img/distance-tree.png)

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Charaktermodellierung von Kognatensätzen**

[<img style="width:1000px" src="img/cognates-2.svg" alt="schleicher" />](img/cognates-2.svg)

--
## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Charaktermodellierung von Kognatensätzen**

[<img style="width:1000px" src="img/character-tree.png" alt="schleicher" />](img/character-tree.png)



--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Phylip-Format**

<pre><code class="text" data-trim>
12
Germa 0.0 0.19 0.11 0.27 0.19 0.26 0.16 0.16 0.19 0.22 0.11 0.08
Engli 0.19 0.0 0.14 0.27 0.19 0.22 0.16 0.16 0.26 0.22 0.11 0.14
Dutch 0.11 0.14 0.0 0.29 0.21 0.27 0.14 0.18 0.24 0.24 0.13 0.09
Icela 0.27 0.27 0.29 0.0 0.08 0.21 0.14 0.11 0.27 0.08 0.22 0.22
Nynor 0.19 0.19 0.21 0.08 0.0 0.13 0.06 0.03 0.22 0.06 0.14 0.14
Riksm 0.26 0.22 0.27 0.21 0.13 0.0 0.13 0.09 0.29 0.16 0.21 0.21
Swedi 0.16 0.16 0.14 0.14 0.06 0.13 0.0 0.03 0.19 0.09 0.11 0.11
Danis 0.16 0.16 0.18 0.11 0.03 0.09 0.03 0.0 0.19 0.06 0.11 0.11
Gothi 0.19 0.26 0.24 0.27 0.22 0.29 0.19 0.19 0.0 0.22 0.18 0.18
OIcel 0.22 0.22 0.24 0.08 0.06 0.16 0.09 0.06 0.22 0.0 0.14 0.18
OEngl 0.11 0.11 0.13 0.22 0.14 0.21 0.11 0.11 0.18 0.14 0.0 0.06
OHGer 0.08 0.14 0.09 0.22 0.14 0.21 0.11 0.11 0.18 0.18 0.06 0.0
</code></pre>

--

## @head:"Computergestützte Rekonstruktion"
### @subhead:"Formate"

**Nexus-Format**

<pre><code class="text" data-trim>
#nexus
BEGIN Taxa;
DIMENSIONS ntax=12;
TAXLABELS 'Germa' 'Engli' 'Dutch' 'Icela' 'Nynor' 'Riksm' 'Swedi' 'Danis'
'Gothi' 'OIcel' 'OEngl' 'OHGer';
END; [Taxa]
BEGIN Characters;
DIMENSIONS nchar=61;
FORMAT
datatype=STANDARD
missing=?
gap=-
symbols="01"
labels=left
transpose=no
interleave=no
;
MATRIX
'Germa' 0111111111111111111111111111111111111111100000000000000000000
'Engli' 0100011111111111111011111111010110111111111111000000000000000
'Dutch' 0101111111111111111111111111010111111111110010110000000000000
'Icela' 0100111110111111110111110111011110111111110001001111111100000
AH
'Nynor' 0100111110111111110111111111011110111111110001001110010000000
'Riksm' 0100010110111010111111011111011110111111110001001010010010000
'Swedi' 0100111110111111111111111111011110111111110001101010000000000
'Danis' 0100111110111111111111111111011110111111110001001010010000000
'Gothi' 0100111011111111111101110111011111111111100001001000000001111
'OIcel' 0100111110111111111111111111011110111111110001001111010101000
'OEngl' 0101111111111111111111111111011110111111110101000000000001000
'OHGer' 0101111111111111111111111111011111111111110100001000000000000
;
END;
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Phylogenetische Rekonstruktion"
    * @stroked:"Innere und äußere Sprachgeschichte"
    * @stroked:"Stammbäume und Wellen"
    * @stroked:"Darstellung und Analyse"
* @stroked:"Lexikostatistik"
    * @stroked:"Hintergrund und Grundannahmen"
    * @stroked:"Praktische Umsetzung"
    * @stroked:"Kritik"
* @stroked:"Computergestützte Rekonstruktion"
    * @stroked:"Komparanda"
    * @stroked:"Algorithmen"
    * @stroked:"Formate"

---
@data-background:#000000

<p style="font-size:120px;color:white;font-weight:bold;">
<code class="python">>>> 3 - 1</code>
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
Ende der ersten Sitzung
</p>

