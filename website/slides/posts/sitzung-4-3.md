# Sitzung 2: Geoplots mit JavaScript und D3 


@data-background:LightYellow
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 3 (Tag 4)

----

#### 23.07.2015

----

### &quot;Geoplots mit JavaScript und D3&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Darstellung geographischer Daten"
    * @unstroked:"GeoJson und TopoJson"
    * @unstroked:"D3"
* @unstroked:"Eine Beispielapplikation"
    * @unstroked:"Idee"
    * @unstroked:"Vorbereitung"
    * @unstroked:"Applikation"

---

## @head:"Darstellung geographischer Daten"
### @subhead:"GeoJson und TopoJson"

**Grundlegendes**

[GeoJson](http://geojson.org) und [TopoJson](https://github.com/mbostock/topojson) sind Formate zur einfachen Beschreibung geographischer Daten. 
Sie bauen beide auf dem JSON-Format auf, welches wir im Laufe des Woche ja schon zuweilen verwendet haben. Beide Formate stellen eine ideale Grundlage für geographische Darstellungen mit JavaScript dar und sind auch ineinander überführbar. Wir werden TopoJson für unser Beispiel verwenden.

--

## @head:"Darstellung geographischer Daten"
### @subhead:"GeoJson und TopoJson"

**GitHub-Integration**

* Das tolle an Geo- und TopoJson ist, dass die Formate direkt in GitHub als Karten dargestellt werden. 

* Wenn wir uns Beispielsweise die Datei [zh-mainland-provinces-topo.json](https://github.com/LinguList/pyjs-seminar/blob/master/website/demos/china/maps/zh-mainland-provinces.topo.json) direkt auf GitHub anschauen, dann sehen wir direkt eine Karte, und auch, was auf der Karte zu sehen ist!

--

## @head:"Darstellung geographischer Daten"
### @subhead:"GeoJson und TopoJson"

**Getting Started**

Grundlegendes zu den Formaten, aber auch zum Gestalten einer Karte kann man im Internet in vielen Beispielen finden. Ich selbst habe meine ersten Erkenntnisse über D3 und die Verwendung von geographischen Daten in JS durch das Beispiel [Let's Make a Map](http://bost.ocks.org/mike/map/) von Mike Bostock gesammelt.

Dort beschreibt Bostock auch, wo man gute geographischen Daten finden kann. Diese liegen meist in Form von "shapefiles" vor, die nicht in JS verwendet werden können. Aber es gibt mit [mapshaper](http://mapshaper.org/) ein sehr gutes Tool, um die Daten direkt in die JSON-Formate umzuwandeln.

---

## @head:"Darstellung geographischer Daten"
### @subhead:"D3"

[D3](http://d3js.org) ist eine wunderbare Bibliothek, um Daten zu Visualisieren und interaktive Applikationen zu schreiben. Leider ist sie auch sehr kompliziert und für Anfänger nur schwer zugänglich, da sich hinter dem Kode viele sehr sinnvolle aber auch eigenwillige Konzepte verbergen. 

Wir haben in diesem Seminar leider keine Zeit, voll auf D3 und die Möglichkeiten einzugehen. Wir werden uns daher auf ein Beispiel beschränken, in dem es weniger um den Kode als um die Idee der Visualisierung geht. 

Denjenigen, die mehr über D3 erfahren möchte, empfehle ich, mit der [offiziellen Homepage](http://d3js.org) anzufangen, und sich dann langsam "hochzuarbeiten".


---

## @head:"Agenda 2015"

* @stroked:"Darstellung geographischer Daten"
    * @stroked:"GeoJson und TopoJson"
    * @stroked:"D3"
* @unstroked:"Eine Beispielapplikation"
    * @unstroked:"Idee"
    * @unstroked:"Vorbereitung"
    * @unstroked:"Applikation"

---

## @head:"Eine Beispielapplikation"
### @subhead:"Idee"

**Die Daten**

Wir haben uns schon mit der Kollektion chinesischer Daten befasst und sie sogar bereits mit Hilfe von LingPy aliniert. Nun wollen wir einen Schritt weiter gehen, und die Diversität der Sprachen nicht nur über die einzelnen Alinierungen, sondern auch im Raum darzustellen. 

--

## @head:"Eine Beispielapplikation"
### @subhead:"Idee"

**Die Idee**

Die Idee ist einfach: Wir plotten alle Dialektpunkte auf eine Karte, und erlauben dann den Benutzern, Konzeptweise Daten aufzurufen und bei Klick auf einen Dialektpunkt sowohl die Verteilung des Kognatensets als auch die Wörter in alinierter Form zu betrachten.

--


## @head:"Eine Beispielapplikation"
### @subhead:"Idee"

**Die Tools**

* Python: zur Alinierung der Daten und zur Aufbereitung der Daten in JavaScript-kompatible Formate (JSON, JS Objekte).
* JavaScript: zum Plotten der Daten mit Hilfe von D3.

---

## @head:"Eine Beispielapplikation"
### @subhead:"Vorbereitung"

**Programmarbeit**


* Erstellen der Daten und Überführung in LingPy-Wortlisten-Format
* Durchführung der Alinierungsanalyse mit Hilfe von LingPy
* Exportieren der Daten in JS-Formate (hauptsächlich JS-Objects, die ja wie ein Hash verwendet werden können und identisch mit JSON-Objekten sind).

--

## @head:"Eine Beispielapplikation"
### @subhead:"Vorbereitung"

**Hintergrundarbeit**

* Geographische Files konnten übernommen werden aus einem [GitHub-Repository](https://github.com/clemsos/d3-china-map).
* Der Kode musste nur geringfügig angepasst werden, und die Dialektpunkte ergänzt werden.


--

## @head:"Eine Beispielapplikation"
### @subhead:"Vorbereitung"

**Planung der Applikation**

* Grundlegende Idee: Teile die Applikation in zwei Teile, einen mit der Karte, einen mit den Alinierungen
* Zur Darstellung der Alinierungen liegt bereits eine [JS-Bibliothek](http://github.com/dighl/prison) vor, die es ermöglicht, Wörter, die segmentiert vorliegen, koloriert darzustellen.
* Erweiterte Ideen wurden in einem nicht ratsamen "trial-and-error-Vefahren" entwickelt (planen ist immer besser als ausprobieren, aber man plant dann am Ende doch immer viel zu wenig...).

---

## @head:"Eine Beispielapplikation"
### @subhead:"Applikation"

<iframe oncklick="window.location.href = '../demos/china/china.html';" src="../demos/china/china.html" style="width:1100px;height:500px"></iframe>

---

## @head:"Agenda 2015"

* @stroked:"Darstellung geographischer Daten"
    * @stroked:"GeoJson und TopoJson"
    * @stroked:"D3"
* @stroked:"Eine Beispielapplikation"
    * @stroked:"Idee"
    * @stroked:"Vorbereitung"
    * @stroked:"Applikation"

---
@data-background:#000000

<p style="font-size:120px;color:white;font-weight:bold;">
<code class="python">>>> 3 - 3</code>
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
Ende des Blockseminars
</p>

