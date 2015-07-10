# Sitzung 1: Sequenzvergleiche in der historischen Linguistik


@data-background:#ffffff
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 2 (Tag 3)

----

#### 22.07.2015

----

### &quot;Sequenzalinierung in JavaScript&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Automatische Sequenzalinierung"
    * @unstroked:"Das Problem"
    * @unstroked:"Die Lösungsstrategie"
    * @unstroked:"Der Algorithmus"
* @unstroked:"Sequenzalinierung in JavaScript"
    * @unstroked:"Vorüberlegungen"
    * @unstroked:"Implementierung der Matrixberechnung"
    * @unstroked:"Implementierung des Traceback"
* @unstroked:"Interaktive Sequenzalinierung"
    * @unstroked:"Grundlagen"
    * @unstroked:"Implementierung"
    * @unstroked:"Demo"

---

## @head:"Automatische Sequenzalinierung"
### @subhead:"Das Problem"

**Wir wollen zwei Sequenzen automatisch alinieren, aber wie?**

* @fragment:"Eine einfache automatische Lösung wäre es, einfach alle verschiedenen Kombinationen durchzutesten."
* @fragment:"In einem weiteren Schritt könnten wir dann alle Alinierungen testen und ihren &quot;Score&quot; berechnen, also sie bewerten, indem wir, zum Beispiel, zählen, wie viele Mismatches und leere Matches sie aufweisen."
* @fragment:"Dann könnten wir den Score für jedes Paar aufsummieren und würden einfach die Alinierung mit dem besten Score nehmen."

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Das Problem"

**Leider dauert das zu lange!**

Die Zahl aller Möglichen Alinierungen zwischen zwei Strings hängt von deren Länge ab: Es gilt:

$N = \sum_{k=0}^{\min(m,n)} 2^{k} \cdot \binom{m}{k} \cdot \binom{n}{k}$, 

für zwei Strings der Länge $m$ und $n$.

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Das Problem"

**Und was soll das heißen?**

Das wir für die Alinierung von "Herz" und "heart" 681 verschiedene Alinierungen testen müssten, und für die Alinierung von "Werdegänge" und "Kinderpass" 8 097 453 verschiedene Möglichkeiten!

---


## @head:"Automatische Sequenzalinierung"
### @subhead:"Die Lösungsstrategie"

**Sei faul und mach Dir keine unnötige Arbeit!**

Die Lösungsstrategie beruht auf der Idee, dass man bestimmte Teillösungen, die man schon berechnet hat, ja eigentlich nicht noch ein zweites Mal berechnen muss, und ferner, dass man Lösungswege, die so abwegig sind, dass klar ist, dass sie nicht zum Erfolg führen können, einfach nicht weiterverfolgt.

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Die Lösungsstrategie"

**Dynamische Programmierung**

Der Algorithmus, mit dem man die optimale Alinierung von zwei Strings relativ schnell und effizient berechnen kann, gehört zur Familie der dynamischen Programmieralgorithmen (*dynamic programming*). Die Idee dieser Algorithmen ist es, ein Problem in umgekehrter Richtung anzugehen: Anstatt alle möglichen Alinierungen zwischen zwei Sequenzen zu testen, baut man eine Alinierung auf, indem man Gebrauch macht von "previous solutions for optimal alignments of smaller subsequenze" ([Durbin et al. 1998[2002]](:bib:Durbin2002)).

---

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Grundlegende Bestandteile**

1. **Scoring Schema:** bestimmt, wie wir uniforme, divergente, und leere Matches bewerten.
2. **Matrizzenkonstruktion:** erstellt eine Matrix, in der wir alle möglichen Kombinationen der Sequenzen miteinander einander gegenüberstellen.
3. **Traceback:** Merkt sich alle Zwischenentscheidungen, die getroffen wurden, so dass wir nachher ermitteln können, welchen "Pfad" wir gelaufen sind, umz um besten Ergebnis zu gelangen.

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Scoring Schema**

<table class="mytabs">
<tr><th>Matching Type</th><th>Score</th><th>Example</th></tr>
<tr><td> uniform match </td>   <td>0 </td><td> A / A </td></tr>
<tr><td> divergent match </td> <td>1 </td><td> A / B</td></tr>
<tr><td> emtpy match </td>     <td>1 </td><td> A / -, - / A </td></tr>
</table>

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Matrix**

<table class="mytabs">
<tr><td>  </td><td> B </td><td> Ä </td><td> R </td></tr>
<tr><td> A </td><td style="color:white">A / B</td><td style="color:white">A / Ä</td><td style="color:white">A / Ä</td></tr>
<tr><td> B </td><td style="color:white">B / B</td><td style="color:white">B / Ä</td><td style="color:white">B / Ä</td></tr>
<tr><td> E </td><td style="color:white">E / B</td><td style="color:white">E / Ä</td><td style="color:white">E / Ä</td></tr>
<tr><td> R </td><td style="color:white">R / B</td><td style="color:white">R / Ä</td><td style="color:white">R / Ä</td></tr>
</table>

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Matrix**

<table class="mytabs">
<tr><td> - / - </td><td> - / B </td><td> - / Ä </td><td> - / R </td></tr>
<tr><td> A / - </td><td style="color:Crimson">A / B</td><td style="color:Crimson">A / Ä</td><td style="color:Crimson">A / R</td></tr>
<tr><td> B / - </td><td style="color:Crimson">B / B</td><td style="color:Crimson">B / Ä</td><td style="color:Crimson">B / R</td></tr>
<tr><td> E / - </td><td style="color:Crimson">E / B</td><td style="color:Crimson">E / Ä</td><td style="color:Crimson">E / R</td></tr>
<tr><td> R / - </td><td style="color:Crimson">R / B</td><td style="color:Crimson">R / Ä</td><td style="color:Crimson">R / R</td></tr>
</table>

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Matrix**

<table><tr><td>
<table class="mytabs">
<tr><td> - / - </td><td> - / B </td><td> - / Ä </td><td> - / R </td></tr>
<tr><td> A / - </td><td style="color:black">A / B</td><td style="color:black">A / Ä</td><td style="color:black">A / R</td></tr>
<tr><td> B / - </td><td style="color:black">B / B</td><td style="color:Crimson;font-weight:bold">B / Ä</td><td style="color:black">B / R</td></tr>
<tr><td> E / - </td><td style="color:black">E / B</td><td style="color:black">E / Ä</td><td style="color:black">E / R</td></tr>
<tr><td> R / - </td><td style="color:black">R / B</td><td style="color:black">R / Ä</td><td style="color:black">R / R</td></tr>
</table></td><td style="font-size:100px;font-weight:bold;vertical-align:top;">→</td><td>
<table class="mytabs">
<tr><td style="color:Crimson"> - </td><td style="color:Crimson"> Ä </td></tr>
<tr><td style="color:Crimson"> B </td><td style="color:Crimson"> Ä </td></tr>
<tr><td style="color:Crimson"> B </td><td style="color:Crimson"> - </td></tr>
</table></td></tr></table>

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Traceback**

<table class="mytabs">
<tr><td style="background:lightgray;"> - / - </td><td> - / B </td><td> - / Ä </td><td> - / R </td></tr>
<tr><td style="background:lightgray"> A / - </td><td style="color:black">A / B</td><td style="color:black">A / Ä</td><td style="color:black">A / R</td></tr>
<tr><td> B / - </td><td style="color:black;background:lightgray;">B / B</td><td style="color:black">B / Ä</td><td style="color:black">B / R</td></tr>
<tr><td> E / - </td><td style="color:black">E / B</td><td style="color:black;background:lightgray">E / Ä</td><td style="color:black">E / R</td></tr>
<tr><td> R / - </td><td style="color:black">R / B</td><td style="color:black">R / Ä</td><td style="color:black;background:lightgray">R / R</td></tr>
</table>

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

**Traceback**

<table><tr><td>
<table class="mytabs">
<tr><td style="background:lightgray;"> - / - </td><td> - / B </td><td> - / Ä </td><td> - / R </td></tr>
<tr><td style="background:lightgray"> A / - </td><td style="color:black">A / B</td><td style="color:black">A / Ä</td><td style="color:black">A / R</td></tr>
<tr><td> B / - </td><td style="color:black;background:lightgray;">B / B</td><td style="color:black">B / Ä</td><td style="color:black">B / R</td></tr>
<tr><td> E / - </td><td style="color:black">E / B</td><td style="color:black;background:lightgray">E / Ä</td><td style="color:black">E / R</td></tr>
<tr><td> R / - </td><td style="color:black">R / B</td><td style="color:black">R / Ä</td><td style="color:black;background:lightgray">R / R</td></tr>
</table></td><td style="font-size:100px;font-weight:bold;vertical-align:top;">→</td><td>
<table class="mytabs">
<tr><td style="background:lightgray"> 0 </td><td> 2 </td><td> 2 </td><td> 2 </td></tr>
<tr><td style="background:lightgray"> 1 </td><td> 0 </td><td> 2 </td><td> 2 </td></tr>
<tr><td> 1 </td><td style="background:lightgray;"> 0 </td><td> 2 </td><td> 2 </td></tr>
<tr><td> 1 </td><td> 1 </td><td style="background:lightgray"> 0 </td><td> 2 </td></tr>
<tr><td> 1 </td><td> 1 </td><td> 1 </td><td style="background:lightgray"> 0 </td></tr>
</table></td></tr></table>

--

## @head:"Automatische Sequenzalinierung"
### @subhead:"Der Algorithmus"

<iframe src="../demos/nw-demo.html" style="width:950px;height:600px"></iframe>

---
@data-transition:none

## @head:"Agenda 2015"

* @stroked:"Automatische Sequenzalinierung"
    * @stroked:"Das Problem"
    * @stroked:"Die Lösungsstrategie"
    * @stroked:"Der Algorithmus"
* @unstroked:"Sequenzalinierung in JavaScript"
    * @unstroked:"Vorüberlegungen"
    * @unstroked:"Implementierung der Matrixberechnung"
    * @unstroked:"Implementierung des Traceback"
* @unstroked:"Interaktive Sequenzalinierung"
    * @unstroked:"Grundlagen"
    * @unstroked:"Implementierung"
    * @unstroked:"Demo"

---

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Vorüberlegungen"

**Um den Algorithmus zu implementieren, brauchen wir:**

* einige numerische Variablen
* die Repräsentation der Sequenzen
* Wege, Alinierungen zu repräsentieren
* Wege, die Matrix zu repräsentieren
* eine Möglichkeit, das Scoring-Schema umzusetzen

--

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Vorüberlegungen"

**JavaScript bietet uns:**

* Variablen, kein Problem
* Listen (Arrays) für die Alinierungen
* und auch für die Sequenzen
* mehrdimensionale Arrays für die Matrix und den Traceback
* if/else-Verzweigungen und String-Vergleiche für das Scoring-Schema

---

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Implementierung der Matrixberechnung"

<pre><code class="javascript">
function seqAlign(seqA, seqB) {
  /* Vorbereitung der Daten hier */
  /* Matrix-Initialisierung hier */
  /* Haupt-Loop hier, darin auch die Scoring Function */
  /* Traceback hier */
  /* Nachbearbeitung hier */
}
</code></pre>

--
## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Implementierung der Matrixberechnung"

<pre><code class="javascript">
function seqAlign(seqA, seqB) {
  /* return nothing if either of the lists is empty */
  if(seqA.length == 0 || seqB.length == 0) {
    return;
  }
  /* get the lengths of the sequences */
  var alen = seqA.length;
  var blen = seqB.length;
  /* declare variables in local environment */
  var i, j; // numbers
  var gapA, gapB, dist; // floats
  var charA, charB; // characters
  /* Matrix-Initialisierung hier */
  /* Haupt-Loop hier, darin auch die Scoring Function */
  /* Traceback hier */
  /* Nachbearbeitung hier */
}
</code></pre>

--

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Implementierung der Matrixberechnung"

<pre><code class="javascript">
function seqAlign(seqA, seqB) {
  /* Vorbereitung hier */
  /* create the matrix */
  var matrix = [];
  for(var i=0;i&lt;alen+1;i++) {
    var inline = [];
    for(var j=0;j&lt;blen+1;j++) {
      inline.push(0);
    }
    matrix.push(inline);
  }
  /* initialize matrix */
  for(i=1;i&lt;blen+1;i++) {
    matrix[0][i] = i;
  }
  for(i=1;i&lt;alen+1;i++) {
    matrix[i][0] = i;
  }
  /* create the traceback */
  var traceback = [];
  for(var i=0;i&lt;alen+1;i++) {
    var inline = [];
    for(var j=0;j&lt;blen+1;j++) {
      inline.push(0);
    }
    traceback.push(inline);
  }
  /* initialize traceback */
  for(i=1;i&lt;blen+1;i++) {
    traceback[0][i] = 2;
  }
  for(i=1;i&lt;alen+1;i++) {
    traceback[i][0] = 1;
  }
  /* Haupt-Loop hier, darin auch die Scoring Function */
  /* Traceback hier */
  /* Nachbearbeitung hier */
}
</code></pre>

--

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Implementierung der Matrixberechnung"

<pre><code class="javascript">
function seqAlign(seqA, seqB) {
  /* Vorbereitung hier */  
  /* Matrix-Initialisierung hier */ 
  /* start the iteration to fill the matrix */
  for(i=1;i&lt;alen+1;i++) {
    for(j=1;j&lt;blen+1;j++) {      
      /* get the character in both sequences at their respective position */
      charA = seqA[i-1];
      charB = seqB[j-1];      
      /* check the similarity between the characters to get the local distance */
      if(charA == charB) {
        dist = matrix[i-1][j-1];
      }
      else {
        dist = matrix[i-1][j-1]+1;
      }      
      /* we have the distance for substitution, now we need the gaps */
      gapA = matrix[i-1][j]+1;
      gapB = matrix[i][j-1]+1;    
      /* find the minimal value */
      if(dist &lt; gapA && dist &lt; gapB) {
        matrix[i][j] = dist;
      }
      else if(gapA &lt; gapB) {
        matrix[i][j] = gapA ;
        traceback[i][j] = 1;
      }
      else {
        matrix[i][j] = gapB;
        traceback[i][j] = 2;
      }
    }
  }
  /* Traceback hier */
  /* Nachbearbeitung hier */
}
</code></pre>

---

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Implementierung des Traceback"

<pre><code class="javascript">
function seqAlign(seqA, seqB) {
  /* Vorbereitung hier */
  /* Matrix-Initialisierung hier */
  /* get indices for the last cells of the matrix */
  i = matrix.length-1;
  j = matrix[0].length-1;
  /* get the edit-dist */
  var ED = matrix[i][j];
  /* initialize the alignment arrays */
  var almA = [];
  var almB = [];
  /* start the traceback */
  while(i &gt; 0 || j &gt; 0) {
    if(traceback[i][j] == 0) {
      almA.push(seqA[i-1]);
      almB.push(seqB[j-1]);
      i--;
      j--;
    }
    else if(traceback[i][j] == 1) {
      almA.push(seqA[i-1]);
      almB.push("-");
      i--;
    }
    else {
      almA.push("-");
      almB.push(seqB[j-1]);
      j--;
    }   
  }
  /* Nachbearbeitung hier */
}
</code></pre>

--

## @head:"Sequenzalinierung in JavaScript"
### @subhead:"Implementierung des Traceback"

<pre><code class="javascript">
function seqAlign(seqA, seqB) {
  /* Vorbereitung hier */
  /* Matrix-Initialisierung hier */
  /* Haupt-Loop hier, darin auch die Scoring Function */
  /* reverse alignments */
  almA = almA.reverse();
  almB = almB.reverse();
}
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Automatische Sequenzalinierung"
    * @stroked:"Das Problem"
    * @stroked:"Die Lösungsstrategie"
    * @stroked:"Der Algorithmus"
* @stroked:"Sequenzalinierung in JavaScript"
    * @stroked:"Vorüberlegungen"
    * @stroked:"Implementierung der Matrixberechnung"
    * @stroked:"Implementierung des Traceback"
* @unstroked:"Interaktive Sequenzalinierung"
    * @unstroked:"Grundlagen"
    * @unstroked:"Implementierung"
    * @unstroked:"Demo"

---

## @head:"Interaktive Sequenzalinierung"
### @subhead:"Grundlagen"



---

## @head:"Interaktive Sequenzalinierung"
### @subhead:"Implementierung"

<pre><code class="html">

</code></pre>

---

## @head:"Interaktive Sequenzalinierung"
### @subhead:"Demo"

<iframe src="../demos/nw-aktiv.html" style="width:950px;height:700px"></iframe>

---

## @head:"Agenda 2015"

* @stroked:"Automatische Sequenzalinierung"
    * @stroked:"Das Problem"
    * @stroked:"Die Lösungsstrategie"
    * @stroked:"Der Algorithmus"
* @stroked:"Sequenzalinierung in JavaScript"
    * @stroked:"Vorüberlegungen"
    * @stroked:"Implementierung der Matrixberechnung"
    * @stroked:"Implementierung des Traceback"
* @stroked:"Interaktive Sequenzalinierung"
    * @stroked:"Grundlagen"
    * @stroked:"Implementierung"
    * @stroked:"Demo"
---

@data-background:#000000

<p style="font-size:120px;color:white;font-weight:bold;">
pause(30, "min");
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
Ende der zweiten Sitzung
</p>



