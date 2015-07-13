# Sitzung 2: Erste Schritte in Python

@data-background:LightYellow
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 2 (Tag 1)

----

#### 20.07.2015

----

### &quot;Erste Schritte in Python&quot;

---

## @head:"Agenda 2015"

* Allgemeines zu Python
    - Herkunft
    - Charakteristik
    - Installation
* Bibliotheken und Entwicklertools
    - Allgemeines
    - Empfohlene Bibliotheken
    - Empfohlene Tools
* Ein erstes Programmierbeispiel
    - Das Problem
    - Der Algorithmus
    - Die Python-Implementierung
      
---

## @head:"Allgemeines zu Python"
### @subhead:"Herkunft"

[Python](http://python.org) 

* @fragment:"wurde Anfang der 1990er Jahre von Guido van Rossum entwickelt"
* @fragment:"erhielt seinen Namen in Anspielung auf die Monty Pythons"
* @fragment:"erschien 1994 in der ersten Version 1.0"
* @fragment:"erschien 2000 in der Version 2.0, die viele Neuerungen enthielt"
* @fragment:"erschien 2008 in der Version 3.0, die nicht mehr kompatibel mit 2.0 ist, eine Vielzahl von Verbesserungen aufweist und von uns verwendet wird"

--

## @head:"Allgemeines zu Python"
### @subhead:"Charakteristik"

[Python](http://python.org) 

* @fragment:"ist eine universelle, interpretierte höhere Programmiersprache"
* @fragment:"ist sehr stark auf gute Lesbarkeit ausgerichtet"
* @fragment:"relativ einfach zu erlernen"
* @fragment:"sehr flexibel (unterstützt objektorientierte und funktionale Programmierung)"
* @fragment:"bietet in der Version 3 endlich eine volle Unicode-Unterstützung"
* @fragment:"besticht durch einfache Syntax und relativ wenige Schlüsselwörter"
* @fragment:"ist eine wunderschöne Sprache"

--

## @head:"Allgemeines zu Python"
### @subhead:"Installation"

* <span class="fragment">Download unter [http://python.org](http://python.org) (wir verwenden ausschließlich Python 3 im Rahmen des Seminars!)</span>
* <span class="fragment">Installationsanleitung unter [https://www.python.org/about/gettingstarted/](https://www.python.org/about/gettingstarted/)</span>
* @fragment:"die Installation sollte generell problemlos auf fast allen Plattformen verlaufen"

---

## @head:"Agenda 2015"

* @stroked:"Allgemeines zu Python"
    - @stroked:"Herkunft"
    - @stroked:"Charakteristik"
    - @stroked:"Installation"
* Bibliotheken und Entwicklertools
    - Allgemeines
    - Empfohlene Bibliotheken
    - Empfohlene Tools
* Ein erstes Programmierbeispiel
    - Das Problem
    - Der Algorithmus
    - Die Python-Implementierung

---

## @head:"Bibliotheken und Entwicklertools"
## @subhead:"Allgemeines"

[Wikipedia](:wiki:Programmbibliothek) zur "Programmbibliothek":

<blockquote class="fragment">
Eine Programmbibliothek bezeichnet in der
Programmierung eine Sammlung von
Programmfunktionen für zusammengehörende
Aufgaben. Bibliotheken sind im Unterschied zu
Programmen keine eigenständig lauffähigen Einheiten,
sondern Hilfsmodule, die Programmen zur Verfügung
gestellt werden.
</blockquote>

--

@data-transition:none

## @head:"Bibliotheken und Entwicklertools"
## @subhead:"Allgemeines"

**Installation von Python-Bibliotheken mit [pip](http://pypa.io)**

Die Installation von Python-Bibliotheken ist relativ einfach, wenn man auf das
Installationstool *pip* ("pip installs packages")
zurückgreift. Dieses ist bei den neuesten Pythonversionen (3.4) bereits
vorinstalliert, und kann daher direkt verwendet werden. Die verwendung ist
denkbar einfach. In der Kommandozeile ("cmd" in der Suchleiste bei Windows
eingeben) gibt man einfach Folgendes ein:

<pre><code>$ pip install packagename</code></pre>

Daraufhin wird die Bibliothek dann installiert.

--

## @head:"Bibliotheken und Entwicklertools"
## @subhead:"Empfohlene Programmierbibliotheken"

* <span class="fragment">[NumPy](http://numpy.org), "Numeric Python",
  [http://numpy.org](http://numpy.org):  Sehr gute Bibliothek, die eine Vielzahl
  effizienter numerischer Berechnungen erlaubt und häufig als Grundlage für
  weitere Bibliotheken gefordert wird. </span>
* <span class="fragment">[SciPy](http://scipy.org), "Scientific Python",
  [http:/scipy.org](http://scipy.org): Sehr wichtige (leider etwas langsame)
  Bibliothek für wissenschaftliche Programmierung. </span>
* <span class="fragment">[Matplotlib](http://matplotlib.org),
  [http://matplotlib.org](http://matplotlib.org): Exzellente Bibliothek für das
  Erstellen hochwertiger Plots von Daten.</span>
* <span class="fragment">[Networkx](http://networkx.org),
  [http://networkx.org](http://networkx.org): Sehr gute Bibliothek für
  Netzwerkkalkulationen.</span>
* <span class="fragment">[LingPy](http://lingpy.org), "Linguistic Python",
  [http://lingpy.org](http://lingpy.org): Bibliothek zur Durchführung von
  quantitativen Analysen in der historischen Linguistik (Download unter:
  [https://github.com/lingpy/lingpy/releases/tag/v2.4.1-alpha](https://github.com/lingpy/lingpy/releases/tag/v2.4.1-alpha)).</span>

--

## @head:"Bibliotheken und Entwicklertools"
## @subhead:"Empfohlene Entwicklertools"

* <span class="fragment">[IPython](http://ipython.org),
  [http://ipython.org](http://ipython.org): Sehr gutes Kommandozeileninterpreter
  für Python, der vor allem auch das Testen von Code ungemein erleichtert.
  </span>
* <span class="fragment">Installation unter Windows (kann etwas kompliziert
  werden, aber Sie sollten das schon schaffen!):
  [http://ipython.org/ipython-doc/2/install/install.html#windows](http://ipython.org/ipython-doc/2/install/install.html#windows)</span>
* <span class="fragment">Installation unter Linux/Ubuntu:
  <pre><code>$ sudo apt-get install ipython3</code></pre></span>
* <span class="fragment">Installation unter Archlinux:
  <pre><code>$ sudo pacman -S ipython</code></pre></span>

---

## @head:"Agenda 2015"

* @stroked:"Allgemeines zu Python"
    - @stroked:"Herkunft"
    - @stroked:"Charakteristik"
    - @stroked:"Installation"
* @stroked:"Bibliotheken und Entwicklertools"
    - @stroked:"Allgemeines"
    - @stroked:"Empfohlene Bibliotheken"
    - @stroked:"Empfohlene Tools"
* Ein erstes Programmierbeispiel
    - Das Problem
    - Der Algorithmus
    - Die Python-Implementierung

---

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Das Problem"

<blockquote class="fragment">
Karlheinz, ein Düsseldorfer Student der Lingustik im 20. Semester, hat auf einer
Mediziner-Party in Köln eine Medizinstudentin
kennengelernt, die ihr Physikum bereits abgeschlossen hat, und
möchte sie gerne wiedersehen. Dummerweise kann er sich
jedoch nicht mehr genau daran erinnern wie sie heißt. Ihr
Nachname klang irgendwie nach <span style="font-style:normal">[maiɐ]</span>, und ihr Vorname war
irgendwas in Richtung <span style="font-style:normal">[krɪstiːnə]</span>, jedoch weiß er nicht, welche
Schreibung er zugrunde legen soll. 

--
@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Das Problem"

<blockquote>
Zufällig hat er eine Liste mit
den wirklichen Namen und den dazugehörigen
Facebook-Namen von allen Bürgern aus Köln und Umgebung
als Excel-Tabelle auf seinem Computer zu Hause. Wenn er jetzt
noch ein Verfahren finden könnte, das ihm alle Namen anzeigt,
die wie <span style="font-style:normal">[krɪstiːnə maiɐ]</span> klingen, dann wäre es sicherlich ein
Leichtes, herauszufinden, wo die unbekannte Studentin ihre
Tierversuche veranstaltet, und sie mit einem Pausenkaffee von
. Starbucks zwischen Frosch und Kaninchen zu überraschen...
</blockquote>

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Der Algorithmus"

<span class="fragment">
Die Lösung besteht darin, alle Namen, die auf der Liste
auftauchen, in ein anderes Format umzuwandeln, welches den
Sprachklang der Wörter wiedergibt und nicht ihre Schreibung.
Ein Algorithmus, der für diesen Zweck geschaffen wurde, ist die
sogenannte "Kölner Phonetik" (vgl. [Postel 1969](:bib:Postel1969)). 
Die Kölner
Phonetik wandelt Wörter der deutschen Sprache in einen
phonetischen Kode um, mit dessen Hilfe auch Wörter, die
unterschiedlich geschrieben werden, aber gleich klingen,
verglichen werden können. So werden die beiden Namen
*Christina Maier* und *Kirsten Mayr* durch den Algorithmus jeweils
in die gleiche Zahlenfolge “47826-67” umgewandelt.</span>

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Der Algorithmus"

[<img src="img/kphon.svg" alt="kphon" width="800px" />](img/kphon.svg)

--
@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Der Algorithmus"

**Das Verfahren**

1. Wandle jeden Buchstaben schrittweise um und beachte die
   Kontextregeln.
2. Reduziere alle mehrfach hintereinander auftauchenden
   Ziffern auf eine.
3. Entfernen die Ziffer “0” an allen Stellen des Wortes, außer
   am Anfang.

--
@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Der Algorithmus"

**Aufgabe an alle Seminarteilnehmer**

Wenden Sie die Kölner Phonetik auf Ihren Vor- und Nachnamen an
und dokumentieren Sie dabei explizit, welche Schritte Sie dabei
durchführen. Warum ist das Verfahren komplizierter, als man am
Anfang vermuten könnte?

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Python-Implementierung"

Die Kölner Phonetik ist in Python von Robert Schindler implementiert worden und
unter der URL (http://pypi.python.org/pypi/kph/0.3) erhältlich. Wir ignorieren
vorerst die Details der Umsetzung und konzentrieren uns auf die Anwendung.
Die Installation ist dank "pip" denkbar einfach:

<pre><code class="fragment shell">$ pip install kph</code></pre>


<span class="fragment">Die Verwendung auch:</span>

<pre><code class="fragment python" data-trim>
>>> import kph
>>> kph.encode("Mattis List")
'628582'
</code></pre>

<span class="fragment">Aber wie können wir eine lange Liste von Namen
abfragen, ohne jeden Namen einzeln in der Konsole eingeben zu müssen?</span>

<span class="fragment">Richtig, wir brauchen ein Skript!</span>

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Python-Implementierung"

**Aufbau von Python-Skripten: Shebang und Kodierung**

Die erste Zeile von Python-Skripten sieht oft wie folgt aus:

<pre><code class="python" data-trim>
#! /usr/bin/env python
# *-* coding:utf-8 *-*

YOUR CODE HERE
</code></pre>

Die erste Zeile, die sogenannte [Shebang line](:wiki:Shebang), erlaubt es, das
Programm durch Doppelklick in Linux- und Mac-Systemen ("unixoide Systeme")
auszuführen. Die zweite Zeile legt die Kodierung fest und erlaubt es, bei der
Verwendung von Python-2 Programmen, alle Arten von nicht-ASCII Zeichen zu
verwenden. Streng genommen brauchen wir aber keine der Funktionen, da wir
Programme auf Unix-Computern auch leicht über die Konsole ausführen können, und
Python3 UTF-8 voll unterstützt. 

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Python-Implementierung"

**Aufbau von Python-Skripten: Kommentare**

<pre><code class="python fragment" data-trim>
# Dies ist eine Kommentarzeile,
# durch welche es möglich ist, Dinge in das
# Programm zu schreiben, die nachher
# nicht ausgeführt werden.

# Man kann Kommentare Überall einsetzen, man 
# muss aber beachten, dass, wenn man
# sie einsetzt, alles was hinter dem Kommentar-Zeichen folgt, nicht mehr
# interpretiert wird.

1 + 1 # wird hier interpretiert
# 1 + 1 wird nicht interpriert
1 + # ruft einen Fehler hervor, weil das "+" ohne Gegenstück ist
</code></pre>

<pre><code class="python fragment" data-trim>
"Alternativ kann man Dinge auch in Anführungsstriche setzen."

"""
Sicherer ist es allerdings, drei Anführungsstriche auf
einmal zu verwenden, weil man dann auch Anführungsstriche
inerhalb des Kommentars benutzen kann, bzw. auch über
mehrere Zeilen hinweg schreiben kann.
"""
</pre></code>

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Python-Implementierung"

**[Die Print-Funktion](code/hallo_welt.py)**

<pre><code class="python fragment" data-trim>
# file: hallo_welt.py
print("Hallo Welt!")
</code></pre>

<pre><code class="fragment shell" data-trim>
$ python3 hallo_welt.py
Hallo Welt!
</code></pre>

**[Einbinden von Modulen (Bibliotheken)](code/test_kph.py)**

<pre><code class="python fragment" data-trim>
# file: test_kph.py

import kph 
# importiert die Kölner Phonetik, vorher kann man
# die Bibliothek nicht verwenden

print(kph.encode('Monty Python'))
</code></pre>

<pre><code class="shell fragment" data-trim>
$ python3 test_kph.py
662126
</code></pre>

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Python-Implementierung"

**Einige kurze Ideen zum Experimentieren und Nachdenken**

1. <span class="fragment">Experimentieren Sie mit der Kölner Phonetik. Welche Ausgaben erhalten Sie,
wenn Sie</span>
    * <span class="fragment">eine Zahl in Anführungsstrichen,</span>
    * <span class="fragment">eine Zahl ohne Anführungsstriche, oder</span>
    * <span class="fragment">Buchstaben mit diakritischen Zeichen ("áłň")
      eingeben?</span>
2. <span class="fragment">Gibt man statt <code class="python">encode("Kirsten")</code>,<code class="python">encode("Maier")</code>
   die Zeile
   <code>encode("Kirsten Maier")</code> ein, verändert sich die Ausgabe.
   Woran liegt das?</span>
3. <span class="fragment">Was brauchen wir (welche Routinen, Verfahren), um alle Daten aus der Excel-Tabelle von Karlheinz einlesen
    und in ihre Werte entsprechend der Kölner Phonetik umwandeln zu
    können?</span>

---

## <span id="time" class="head" onmouseover="startTime('time')">Agenda 2015</span>

* @stroked:"Allgemeines zu Python"
    - @stroked:"Herkunft"
    - @stroked:"Charakteristik"
    - @stroked:"Installation"
* @stroked:"Bibliotheken und Entwicklertools"
    - @stroked:"Allgemeines"
    - @stroked:"Empfohlene Bibliotheken"
    - @stroked:"Empfohlene Tools"
* @stroked:"Ein erstes Programmierbeispiel"
    - @stroked:"Das Problem"
    - @stroked:"Der Algorithmus"
    - @stroked:"Die Python-Implementierung"

---

@data-background:#000000

<p style="font-size:200px;color:white;font-weight:bold;">
ENDE
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
der zweiten Sitzung
</p>
<p><code style="font-size:160px">:wq!</code></p>



