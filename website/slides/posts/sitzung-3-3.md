# Sitzung 1: Sequenzvergleiche in der historischen Linguistik


@data-background:#ffffff
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 3 (Tag 3)

----

#### 22.07.2015

----

### &quot;Sequenzalinierung in Python&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Sequenzalinierung in Python"
    * @unstroked:"Allgemeine Strategien"
    * @unstroked:"Implementierung der Matrixberechnung"
    * @unstroked:"Implementierung des Traceback"
* @unstroked:"Lautklassenbasierte Alinierung"
    * @unstroked:"Noch mal zu den Lautklassen"
    * @unstroked:"Lautklassenkonvertierung mit Python"
    * @unstroked:"Implementierung der Lautklassenbasierten Alinierung"
* @unstroked:"Phonetische Alinierung in LingPy"
    * @unstroked:"Was ist LingPy?"
    * @unstroked:"Grundlegende Befehle"
    * @unstroked:"Workflows"

---

## @head:"Sequenzalinierung in Python"
### @subhead:"Allgemeine Strategien"

**Python und JavaScript**

Python und JavaScript sind sich im Prinzip recht ähnlich, was die Datentypen anbelangt. Wir werden auch für unsere Python-Implementierung auf Listen (Arrays in JavaScript) zurückgreifen, und Loops durchführen (**while** für den Traceback und **for** für die Matritzen-Füllung). Allerdings können wir in Python kompakter formulieren und haben es daher etwas leichter, den Kode aufzusetzen.

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Allgemeine Strategien"

**Struktur**

Die Implementierung des Alinierungsalgorithmus in Python (eine Version des [Wagner-Fischer Algorithmus](:bib:Wagner1974)) basiert auf den gleichen Blöcken, wie auch die Alinierung in der JavaScript-Implementierung, die wir in der vorigen Sitzung besprochen haben:

1. Vorbereitung von Konstanten und allgemeine Checks
2. Initialisierung von Matrix und Traceback
3. Ausfüllen von Matrix und Traceback
4. Traceback und Konstruktion der Alinierungen

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Allgemeine Strategien"

**Dann kann's ja losgehen!**

Genau! Denn der Algorithmus ist tatsächlich sehr leicht in Python zu implementieren, vorausgesetzt man ist mit den Datentypen ein wenig vertraut. Aber wir schauen uns das jetzt Schritt für Schritt in Ruhe an.

---

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung der Matrixberechnung"

**Grundlegender Aufbau**

<pre><code class="python" data-trim>

def wf_align(seqA, seqB):
    """
    BLABLABLE
    """

    # Vorgeplänkel
    # Initialisierung von Matrix und Traceback
    # Ausfüllen von Matrix und Traceback
    # Traceback-Vorbereitung
    # Traceback
    # Traceback-Nachbereitung
    
    return almA, almB, ED

</code></pre>

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung der Matrixberechnung"

**Vorgeplänkel**

<pre><code class="python" data-trim>
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
    
    # Initialisierung von Matrix und Traceback
    # Ausfüllen von Matrix und Traceback
    # Traceback-Vorbereitung
    # Traceback
    # Traceback-Nachbereitung
    
    return almA, almB, ED
</code></pre>

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung der Matrixberechnung"

**Initialisierung von Matrix und Traceback**

<pre><code class="python" data-trim>
def wf_align(seqA, seqB):
    """
    Align two sequences using the Wagner-Fisher algorithm.
    """
    # Vorgeplänkel
    # Initialisierung von Matrix und Traceback
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

    # Ausfüllen von Matrix und Traceback
    # Traceback-Vorbereitung
    # Traceback
    # Traceback-Nachbereitung
    
    return almA, almB, ED

</code></pre>

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung der Matrixberechnung"

**Ausfüllen von Matrix und Traceback**

<pre><code class="python" data-trim>
def wf_align(seqA, seqB):
    """
    Align two sequences using the Wagner-Fisher algorithm.
    """
    # Vorgeplänkel
    # Initialisierung von Matrix und Traceback
    # Ausfüllen von Matrix und Traceback
    
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
            if match &lt;= gapA and match &lt;= gapB:
                M[i][j] = match
            elif gapA &lt;= gapB:
                M[i][j] = gapA
                T[i][j] = 1 # don't forget the traceback
            else:
                M[i][j] = gapB
                T[i][j] = 2 # don't forget the traceback

    # Traceback-Vorbereitung
    # Traceback
    # Traceback-Nachbereitung
    
    return almA, almB, ED
</code></pre>

---

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung des Traceback"

**Traceback-Vorbereitung**

<pre><code class="python" data-trim>
def wf_align(seqA, seqB):
    """
    Align two sequences using the Wagner-Fisher algorithm.
    """
    # Vorgeplänkel
    # Initialisierung von Matrix und Traceback
    # Ausfüllen von Matrix und Traceback
    # Traceback-Vorbereitung
    # get the edit distance
    ED = M[i][j]

    # start the traceback
    i,j = m-1,n-1

    almA,almB = [],[]

    # Traceback
    # Traceback-Nachbereitung

    return almA, almB, ED
</code></pre>

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung des Traceback"

**Traceback**

<pre><code class="python" data-trim>
def wf_align(seqA, seqB):
    """
    Align two sequences using the Wagner-Fisher algorithm.
    """
    # Vorgeplänkel
    # Initialisierung von Matrix und Traceback
    # Ausfüllen von Matrix und Traceback
    # Traceback-Vorbereitung
    # Traceback
    while i &gt; 0 or j &gt; 0:
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

    # Traceback-Nachbereitung

    return almA, almB, ED
</code></pre>

--

## @head:"Sequenzalinierung in Python"
### @subhead:"Implementierung des Traceback"

**Traceback**

<pre><code class="python" data-trim>
def wf_align(seqA, seqB):
    """
    Align two sequences using the Wagner-Fisher algorithm.
    """
    # Vorgeplänkel
    # Initialisierung von Matrix und Traceback
    # Ausfüllen von Matrix und Traceback
    # Traceback-Vorbereitung
    # Traceback
    # Traceback-Nachbereitung

    # reverse
    almA = almA[::-1]
    almB = almB[::-1]

    return almA, almB, ED
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Sequenzalinierung in Python"
    * @stroked:"Allgemeine Strategien"
    * @stroked:"Implementierung der Matrixberechnung"
    * @stroked:"Implementierung des Traceback"
* @unstroked:"Lautklassenbasierte Alinierung"
    * @unstroked:"Noch mal zu den Lautklassen"
    * @unstroked:"Lautklassenkonvertierung mit Python"
    * @unstroked:"Implementierung der Lautklassenbasierten Alinierung"
* @unstroked:"Phonetische Alinierung in LingPy"
    * @unstroked:"Was ist LingPy?"
    * @unstroked:"Grundlegende Befehle"
    * @unstroked:"Workflows"

---

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Noch mal zu den Lautklassen"

**Dolgopolskys Idee**

> Sounds which frequently occur in
> correspondence relations in
> genetically related languages can
> be clustered into classes. It is
> thereby assumed that “phonetic
> correspondences inside a ‘type’ are
> more regular than those between
> different ‘types’” [(Dolgopolsky 1986[1964]:35](:bib:Dolgopolsky1986)).

--

@data-transition:none

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Noch mal zu den Lautklassen"

[<img src="img/classes.gif" style="width:500px" alt="classes" />](img/classes.gif)

--

@data-transition:none

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Noch mal zu den Lautklassen"

**Dolgopolskys Lautklassenmodell**

[<img src="img/dolgo.png" style="width:600px" alt="classes" />](img/dolgo.png)

--

@data-transition:none

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Noch mal zu den Lautklassen"

**Erweitertes Lautklassenmodell ([List 2014](:bib:List2014d))**

[<img src="img/sca.png" style="width:400px" alt="classes" />](img/sca.png)

---

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Lautklassenkonvertierung mit Python"

**Grundlegende Idee**

* Um eine Sequenz in Lautklassen zu konvertieren, müssen wir für jeden möglichen Lautbuchstaben den entsprechenden Lautklassenbuchstaben definieren.
* Am besten dafür geeignet ist ein Python-Dictionary, welches aus Key-Value-Paaren besteht und zu jedem Key den Value liefern kann.
* Das Erstellen eines solchen Dictionaries ist zwar nervig, es ist aber die einfachste Möglichkeit, um nachher ein Wort zu konvertieren.
* Das Wort muss allerdings segmentiert vorliegen, da wir ansonsten keine Möglichkeit haben, zu wissen, was jeweils ein Laut sein soll (vgl. Laute wie [tʰ] oder [t͡s], die aus zwei oder mehr Zeichen bestehen).

--

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Lautklassenkonvertierung mit Python"

**Workflow**

[<img src="img/sca_workflow.gif" style="width:800px" alt="workflow" />](img/sca_workflow.gif)

--

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Lautklassenkonvertierung mit Python"

**Segmentierung**

Für die Segmentierung bedienen wir uns eines einfachen Modells: Jede Sequenz wird mit Hilfe des Leerzeichens segmentiert dargestellt:

* *Tochter*: "tʰɔxtʰər" → "tʰ ɔ x tʰ ə r" 
* *daughter*: "dɔːtʰər" → "d ɔː tʰ ə r"

Mit Python können wir diesen Input ganz schnell in eine Liste umwandeln:

<pre><code class="python" data-trim>
>>> my_string = "tʰ ɔ x tʰ ə r"
>>> my_sequence = my_string.split(" ")
>>> my_sequence
['tʰ', 'ɔ', 'x', 'tʰ', 'ə', 'r']
</code></pre>

--

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Lautklassenkonvertierung mit Python"

**Umwandlung**

<p class="bq80">
Bei der Umwandlung mit Hilfe eines Dictionaries sollten wir damit rechnen, dass bestimmte Zeichen nicht vorhanden sind (es gibt so viele Symbole, und es kann fast unmöglich sein, alle zu finden, außerdem können die Daten auch Fehler enthalten). Daher führen wir einen dreistufigen Test ein.</p>

<pre><code class="python" data-trim>
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
</code></pre>

---

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Implementierung"

**Laden des Lautklassenmodells**

Wir speichern und laden den Converter im [json-Format](:wiki:json), welches zu einem der gängigsten Austauschformate geworden ist. Wir laden die Datei mit Hilfe des **json**-Modules, wo uns automatisch ein Python-Dictionary zurückgegeben wird. 

<pre><code class="python" data-trim>
def load_model(model):
    """
    Load the converter for a sound-class model.
    """
    # load the converter with json
    converter = json.load(open(model+'.json'))
    return converter
</code></pre>

--

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Implementierung"

**Lautklassenkonvertierung**

Die Konvertierung lässt sich mit sehr wenigen Zeilen Kode umsetzen, da wir hier von der Listengenerationssyntax in Python Gebrauch machen können (sogenannte [list comprehension](http://www.secnetix.de/olli/Python/list_comprehensions.hawk):

<pre><code class="python" data-trim>
def segments2classes(segments, converter):
    """
    Convert a sound string to a sound-class string.
    """
    # check for segmented string
    if type(segments) == str:
        segments = segments.split(' ')
    # convert the segments
    classes = [segment2class(x) for x in segments]
    return classes
</code></pre>

--

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Implementierung"

**Rückkonvertierung**

Zur Rückkonvertierung brauchen wir den ursprünglichen String. Wir gehen ja davon aus, dass wir die Strings zuerst in Lautklassen umwandeln, diese dann alinieren, und nachher alles zurückkonvertieren. Hierbei müssen wir im Prinzip nur merken, wo die Gaps eingesetzt wurden, wir müssen also die Gaps aus der Lautklassensequenz in die ursprüngliche Sequenz übertragen:

<pre><code class="python" data-trim>
def classes2segments(classes, segments):
    """
    Convert an aligned string of sound classes back to the string of segments.
    """
    idx = len(segments)-1
    out = []
    for i in range(len(classes)-1,-1,-1):
        print(i,classes[i])
        if classes[i] == '-':
            out += [classes[i]]
        else:
            out += [segments[idx]]
            idx -= 1  
    return out[::-1] 
</code></pre>

--

## @head:"Lautklassenbasierte Alinierung"
### @subhead:"Implementierung"

**Vollständige Lautklassenbasierte Alinierung**

<pre><code class="python" data-trim>
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
</code></pre>

---
## @head:"Agenda 2015"

* @stroked:"Sequenzalinierung in Python"
    * @stroked:"Allgemeine Strategien"
    * @stroked:"Implementierung der Matrixberechnung"
    * @stroked:"Implementierung des Traceback"
* @stroked:"Lautklassenbasierte Alinierung"
    * @stroked:"Noch mal zu den Lautklassen"
    * @stroked:"Lautklassenkonvertierung mit Python"
    * @stroked:"Implementierung der Lautklassenbasierten Alinierung"
* @unstroked:"Phonetische Alinierung in LingPy"
    * @unstroked:"Was ist LingPy?"
    * @unstroked:"Grundlegende Befehle"
    * @unstroked:"Workflows"


---

@data-background:#000000

<p style="font-size:120px;color:white;font-weight:bold;">
pause(30, "min");
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
Ende der zweiten Sitzung
</p>

