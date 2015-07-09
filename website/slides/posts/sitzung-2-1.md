# Sitzung 1: Variablen und Datentypen

@data-background:#ffffff
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---


@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 1 (Tag 2)

----

#### 21.07.2015

----

### &quot;Variablen und Datentypen&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Variablen"
    - @unstroked:"... im Allgemeinen"
    - @unstroked:"... in Python"
    - @unstroked:"... in JavaScript"
* @unstroked:"Datentypen"
    - @unstroked:"... im Allgemeinen"
    - @unstroked:"... in Python"
    - @unstroked:"... in JavaScript"
* @unstroked:"Praktische Beispiele"
    - @unstroked:"Die Dreiballkaskade"
    - @unstroked:"Die Dreiballkaskade in Python"
    - @unstroked:"Die Dreiballkaskade in JavaScript"

---

## @head:"Variablen"
### @subhead:"... im Allgemeinen"

**Was ist eine Variable?**

* :fragment: *Variable* ist das Substantiv zu *variabel*, welches auf Latein *variabilis* &quot;veränderbar&quot; zurückgeht. ::
* :fragment: Eine Variable ist also etwas, das änderbar ist. ::
* :fragment: Johnny Depp ist ein Beispiel für eine *Variable*, weil er sehr änderbar ist, wie man an seinen Filmen sehen kann. ::

--

## @head:"Variablen"
### @subhead:"... im Allgemeinen"

**[Wikipedias Definition](:wiki:variable_(programming)):**

<blockquote class="fragment">In computer programming, a variable is a symbolic name given to some known or
   unknown quantity or information, for the purpose of allowing the name to be
   used independently of the information it represents. A variable name in
   computer source code is usually associated with a data storage location and
   thus also its contents, and these may change during the course of program
   execution.</blockquote>

--

## @head:"Variablen"
### @subhead:"... im Allgemeinen"

**Definition in [Puttkamer (1990)](:bib:Puttkamer1990):**

<blockquote class="fragment" style="line-height:30px">
Bei jeder Art von Datenverarbeitung beziehen sich die Anweisungen auf
direkte Daten, die eingegeben werden oder auf Variable, die man sich
vorstellen kann als mit Namen versehen Behälter für Daten. 
Jede Zuweisung an eine Variable füllt Daten in diesen Behälter, und der
Wert einer Variablen ist der Inhalt dieses Behälters. So ist z. B. der
Effekt einer Anweisung $A:= 3 + 7$: Bilde mit den direkt eingegebenen Daten
3 und 7 die Summe 10 und weise diesen Wert der Variablen mit Namen A zu.
Ein [sic!] anschließende Anweisung "drucke A" druckt den Inhalt des
Behälters A aus, den Wert der Variablen A, hier 10.
</blockquote>

--

## @head:"Variablen"
### @subhead:"... im Allgemeinen"

**Vereinfachte Begriffserklärung**

* :fragment: Beim Programmieren werden Werte benötigt, deren Inhalt variabel ist. ::
* :fragment: Variabel heißt, dass die Werte sich entweder bei jedem erneuten Programmaufruf ändern können, oder sogar innerhalb des Programms. ::
* :fragment: Bspw. lässt sich ein Programm, dass eine Ganzzahl mit sich selbst multipliziert und das Ergebnis dieser Multiplikation wieder mit sich selbst, nicht schreiben, wenn man nicht eine Möglichkeit hat, auf die Zahl zuzugreifen, obwohl man sie noch nicht kennt. ::
* :fragment: Variablen ermöglichen derartige Programmoperationen. ::
* :fragment: Variablen sind Platzhalter, die, wenn das Programm ausgeführt wird, mit einem Wert gefüllt werden (*Deklaration*). ::

---

## @head:"Variablen"
### @subhead:"... in Python"

**Deklaration von Variablen in Python**

<pre><code class="fragment python" data-trim>
>>> VARIABLE = VALUE
>>> VAR1, VAR2, ... = VAL1, VAL2, ...
>>> VAR1, \*VAR2 = VAL1, VAL2, VAL3, ...
>>> VARIABLE = VAL1, VAL2, ...
</code></pre>

<pre><code class="fragment python" data-trim>
>>> a = 1
>>> b, c = 2, 3
>>> d, \*e = 4, 5, 6
>>> f = 7, 8, 9
>>> print(myvar, myvar1, myvar2, myvar3, myvar4, myvar5)
1 2 3 4 [5, 6] (7, 8, 9)
</code></pre>

--

## @head:"Variablen"
### @subhead:"... in Python"

**Struktur von Variablennamen**

<pre><code class="fragment python" data-trim>
>>> Name = 1
>>> Name_von_mir = 1
>>> Name2 = 1
</code></pre>
<pre><code class="fragment python" data-trim>
>>> 2Name = 1
SyntaxError: invalid syntax
</code></pre>

--

## @head:"Variablen"
### @subhead:"... in Python"

**Programmierbeispiele**

<pre><code class="fragment python" data-trim>
>>> print("Variable")
Variable
>>> Variable = "Variable"
>>> print(Variable)
Variable
>>> Variable
'Variable'
>>> Variable == Variable
True
Variable == 'Variable'
True
>>> var1, var2 = 2, 3
>>> print(var1,"und", var2,"macht",var1 + var2)
2 und 3 macht 5
</code></pre>

--

## @head:"Variablen"
### @subhead:"... in Python"

**Fehlermeldungen**

<pre><code class="fragment python" data-trim>
>>> test = 1,2
>>> test = bla
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
NameError: name 'bla' is not defined
</code></pre>

<pre><code class="fragment python" data-trim>
>>> print(test1)
traceback (most recent call last):
  file "&lt;stdin&gt;", line 1, in &lt;module&gt;
nameerror: name 'test1' is not defined
</code></pre>

<pre><code class="fragment python" data-trim>
>>> test1 = 2
>>> test2 = "2"
>>> test1 + test2
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: unsupported operand type(s) for +: 'int' and 'str'
</code></pre>

---

## @head:"Variablen"
### @subhead:"... in JavaScript"

**Deklaration von Variablen in JavaScript**

<pre><code class="fragment js" data-trim>
> VARIABLE = 1;
> var VAR = 1;
> VAR1 = 1; VAR2 = 2;
> var VAR1, VAR2;
> VAR1 = 1; VAR2 = 1;
</code></pre>

:fragment: Das Schlüsselwort "var" wird in JavaScript verwendet, um sicherzustellen, dass Variablen in Funktionen lokal definiert werden.  Grundsätzlich sollte man (da wir ohnehin nicht global definieren sollten) darauf achten, immer das Schlüsselwort "var" einer Variablendeklaration vorwegzustellen. ::

--

## @head:"Variablen"
### @subhead:"... in JavaScript"

**Struktur von Variablennamen**

<pre><code class="fragment js" data-trim>
> var Name = 1
> var Name_von_mir = 1
> var Name2 = 1
</code></pre>
<pre><code class="fragment js" data-trim>
> var 2Name = 1
SyntaxError: identifier starts immediately after numeric literal
</code></pre>

--

## @head:"Variablen"
### @subhead:"... in JavaScript"

**Programmierbeispiele**

<pre><code class="fragment js" data-trim>
> var myvar = 1;
> var myvar2 = 2;
> var myvar3, myvar4, myvar5;
> myvar3 = 3; myvar4 = 4; myvar5 = 5;
> [myvar1, myvar2, myvar3, myvar4, myvar5].map(function(x){return x+x});
[ 2, 4, 6, 8, 10 ]
</code></pre>

--

## @head:"Variablen"
### @subhead:"... in JavaScript"

**Fehlermeldungen**

<pre><code class="fragment js" data-trim>
> var a = 10;
> var b = '11';
> a + a;
20
> b + b;
1111
> a + b
1011
> a - "10";
0
> a * "10";
100
</code></pre>

:fragment: Vorsicht mit den Operatoren +, -, * und / in JavaScript! Ihr Verhalten kann unberechenbar sein, da im Gegensatz zu Python kein Typcheck durchgeführt wird! ::

---

## @head:"Agenda 2015"

* @stroked:"Variablen"
    - @stroked:"... im Allgemeinen"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @unstroked:"Datentypen"
    - @unstroked:"... im Allgemeinen"
    - @unstroked:"... in Python"
    - @unstroked:"... in JavaScript"
* @unstroked:"Praktische Beispiele"
    - @unstroked:"Die Dreiballkaskade"
    - @unstroked:"Die Dreiballkaskade in Python"
    - @unstroked:"Die Dreiballkaskade in JavaScript"

---

## @head:"Datentypen"
### @subhead:"... im Allgemeinen"

**[Wikipedia-Definition:](:wiki:Datentyp)**

<blockquote class="fragment" style="line-height: 30px;font-size:80%">
Formal bezeichnet ein Datentyp in der Informatik die Zusammenfassung von
Objektmengen mit den darauf definierten Operationen. Dabei werden durch den
Datentyp des Datensatzes unter Verwendung einer so genannten Signatur
ausschließlich die Namen dieser Objekt- und Operationsmengen spezifiziert.
Ein so spezifizierter Datentyp besitzt noch keine Semantik.  Die weitaus
häufiger verwendete, aber speziellere Bedeutung des Begriffs Datentyp stammt
aus dem Umfeld der Programmiersprachen und bezeichnet die Zusammenfassung
konkreter Wertebereiche und darauf definierten Operationen zu einer Einheit.
Zur Unterscheidung wird für diese Datentypen in der Literatur auch der
Begriff Konkreter Datentyp verwendet. Für eine Diskussion, wie
Programmiersprachen mit Datentypen umgehen, siehe
Typisierung.
</blockquote>

--

## @head:"Datentypen"
### @subhead:"... im Allgemeinen"

**Vereinfachte Begriffserklärung**

* :fragment: Variable als Platzhalter, der mit einem bestimmten Wert gefüllt wird. ::
* :fragment: Worum es sich bei dem Wert handelt, ist wichtig für die korrekte Durchführung eines Programms. ::
* :fragment: Wörter kann man beispielsweise nicht addieren. ::
* :fragment: Zahlen kann man dafür nicht einfach aneinanderreihen. ::
* :fragment: Auch im wirklichen Leben teilen wir unsere Zeichen in gewisser Weise in Datentypen ein, denn wenn wir den Satz "Multipliziere mal 1 und 1" hören, dann denken wir bei "1" an eine Zahl und nicht an eine Zeugnisnote, weil man eine Zeugnisnote nicht multiplizieren kann. ::

---

## @head:"Datentypen"
### @subhead:"... in Python"

**Allgemeines**

In Python werden Datentypen bei der Variablendeklaration nicht explizit
angegeben, sondern aufgrund der Struktur der Werte, die den Variablen
zugewiesen werden, automatisch bestimmt. Python weist eine Vielzahl von
Datentypen auf und ermöglicht aufgrund seiner objektorientierten Ausrichtung
auch die Erstellung eigener komplexer Datentypen.

--

## @head:"Datentypen"
### @subhead:"... in Python"

**Wichtigste Datentypen in Python**

* :fragment: *integer*: fasst ganzzahlige Werte (<code>2, 3, -5, 0</code>) ::
* :fragment: *float*: fasst Fließkommawerte (<code>1.2, 1.222, -0.5, -2.5</code>) ::
* :fragment: *string*: fasst Zeichenketten (<code>"Friedrich", "Nietzsche", "孔子"</code>) ::
* :fragment: *list*: fasst jede Art von anderen Datentypen in linearer Anordung und kann verändert werden (<code>["Friedrich", "2", 1998, -0.5]</code>) ::
* :fragment: *tuple*: fasst jede Art von anderen Datentypen, kann aber nicht verändert werden ( <code>("Friedrich", "2", 1998, -0.5)</code>) ::
* :fragment: *dict*: fasst jede Art von anderen Datentypen als Sammlung von Key-Value-Paaren, vobei der Key weder Liste noch Dictionary sein kann (<code>{1:1, "Friedrich" : "Nietzsche"}</code>) ::

--

## @head:"Datentypen"
### @subhead:"... in Python"

**Überprüfen**

<pre><code class="python fragment" data-trim>
>>> a, b, c, d = 1, "2", 2.5, [1,2]
>>> type(a)
&lt;class 'int'&gt;
>>> print(type(b), type(c))
&lt;class 'int'&gt; &lt;class 'str'&gt;
>>> isinstance(d, list)
True
>>> isinstance(d, (int,str))
False
</code></pre>

--

## @head:"Datentypen"
### @subhead:"... in Python"

**Programmbeispiele**

<pre><code class="fragment python" data-trim>
>>> a, b, c = 1, "2", 3.5
>>> words = ["apfel", "wurst", "gurke"]
>>> nahrungs_typ = {"apfel": "vegan", "wurst": "carnivor", "gurke": "vegan"}
>>> b + b
'22'
>>> a / c
-2.5
>>> type(a/c)
&lt;class 'float'&gt;
>>> for word in words: print(word, nahrungs_typ[word])
apfel vegan
wurst carnivor
gurke vegan
>>> print(words[1])
wurst
</code></pre>

---

## @head:"Datentypen"
### @subhead:"... in JavaScript"

**Allgemeines**

Auch in JavaScript werden Datentypen bei der Deklaration nicht explizit
angegeben, sondern dynamisch bestimmt. Auch in JavaScript können komplexe
Datentypen aufgrund der Möglicheit, objekt-orientiert zu programmieren, erstellt
werden. Im Gegensatz zu Python ist es viel leichter, Operationen auf
unterschiedlichen Datentypen durchzuführen, was problematisch werden kann, da
die erwarteten Ergebnisse sich leicht unterscheiden können, wenn ein Programm nicht
sorgfälgit geprüft wird.

--

## @head:"Datentypen"
### @subhead:"... in JavaScript"

**Wichtigste Datentypen in Javascript**

* :fragment: *number*: Ganz- und Fließkommazahlen (<code>1, 1.5</code>) ::
* :fragment: *string*: Zeichenketten (<code>"hallo", 'welt'</code>) ::
* :fragment: *array*: linear angeordnete variable Datentypen (<code>[1, "2", -3]</code>) ::
* :fragment: *object*: Key-Value-Paare (<code>{0:1, 1:2}</code>) ::

:fragment: Beachten Sie, dass es sich bei dem Datentyp "array" offiziell um eine spezielle Form des sehr abstrakten Datentypen "object" handelt, weshalb ein Type-Check auch für einen Array immer den Wert "object" zurückliefern wird. :: 


--

## @head:"Datentypen"
### @subhead:"... in JavaScript"

**Überprüfen**

<pre><code class="fragment javascript" data-trim>
> var a = 1;
> var b = 1.5;
> var c = "1";
> var d = [a, b, c];
> var e = {0 : a, 1 : b, 2 : c};
> typeof a;
number
> typeof b;
number
> typeof c;
string
> typeof d;
object
> typeof e;
object
</code></pre>

--

## @head:"Datentypen"
### @subhead:"... in JavaScript"

**Programmbeispiele**

<pre><code class="fragment js" data-trim>
> var a = 1;
> var b = 1.5;
> var c = "1";
> var d = [a, b, c];
> var e = {0 : a, 1 : b, 2 : c};
> a == d[0];
True
> a === d[0];
True
> e[0] = 2
for (key in e) {alert(key+' '+e[key])}
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Variablen"
    - @stroked:"... im Allgemeinen"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @stroked:"Datentypen"
    - @stroked:"... im Allgemeinen"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @unstroked:"Praktische Beispiele"
    - @unstroked:"Die Dreiballkaskade"
    - @unstroked:"Die Dreiballkaskade in Python"
    - @unstroked:"Die Dreiballkaskade in JavaScript"

---

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade"

**[Dreiballkaskade in Wikipedia](:wiki:Kaskade_(Jonglieren))**

<blockquote class="fragment" style="font-size:80%; line-height:30px">
Als Kaskade wird das am einfachsten zu erlernende Jongliermuster mit einer
ungeraden Anzahl von Gegenständen (Zum Beispiel: Bällen, Keulen oder
Ringen) bezeichnet. Dabei wird mit zwei Gegenständen in einer Hand und
einem in der anderen Hand angefangen. Der erste Wurf wird durch die Hand
ausgeführt, in der zwei Gegenstände sind. 
Wenn der Gegenstand den höchsten
Punkt erreicht, wird der Gegenstand aus der anderen Hand losgeworfen (und
zwar unter dem zuvor geworfenen Gegenstand hindurch). Dadurch ist diese
Hand frei, um den ersten Gegenstand zu fangen. Wenn der zweite Gegenstand
am höchsten Punkt angekommen ist, wird der dritte Gegenstand losgeworfen
(mit der Hand, die auch den ersten Gegenstand geworfen hat) und so weiter.
</blockquote>

--

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade"

<p style="text-align:center"><img src="img/3-ball_cascade_movie.gif" alt="3ballk"
style="width:500px"></p>

---

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade in Python"

<pre><code class="python">
# definiere das jongliermuster
JonglierMuster = """
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
  Dreiball-Jonglage      
+-------------------+
| (L)           (R) |
|                   |
|                   |
|                   |
|                   |
||(l)|         |(r)||
|  |             |  |               
+-------------------+
"""

# deklariere die gegenstände
gegenstand1 = '(1)'
gegenstand2 = '(2)'
gegenstand3 = '(3)'

# halte fest, welcher gegenstand gerade wo ist
RechteHand = gegenstand2
LinkeHand = gegenstand3
RechtsOben = gegenstand1
LinksOben = '   '

# Jetzt kann es losgehen. Das Programm startet, indem wir die Entertaste
# drücken.
input("Los geht's!")

# Wir führen eine Schleife aus (Details dazu kommen später)
i = 0
while i < 20:
    
    # wir deklarieren eine variable snapshot, die in jeweils vier schritten
    # durch das derzeit vorliegende jongliermuster ersetzt wird
    SnapShot = JonglierMuster
    SnapShot = SnapShot.replace('(R)',RechtsOben)
    SnapShot = SnapShot.replace('(L)',LinksOben)
    SnapShot = SnapShot.replace('(l)',LinkeHand)
    SnapShot = SnapShot.replace('(r)',RechteHand)

    # Wir benutzen nicht print, um das ganze auszugeben, sondern input(),
    # weil damit immer gleichzeitig auch eine Pause verbunden ist (erst wenn
    # man Enter drückt geht es weiter). (in Python2 brauchen wir "raw_input")
    input(SnapShot)
    
    # jetzt passen wir die variablen an, wobei wir schauen, wo gerade der
    # ball ist.
    if RechtsOben == '   ':
        RechtsOben = LinkeHand
        LinkeHand = '   '
        i += 1
    
    elif RechteHand == '   ':
        RechteHand = RechtsOben
        RechtsOben = '   '
        i += 1

    elif LinkeHand == '   ':
        LinkeHand = LinksOben
        LinksOben = '   '
        i += 1

    elif LinksOben == '   ':
        LinksOben = RechteHand
        RechteHand = '   '
        i += 1

# Wenn alles geschafft ist, kann man schon mal darauf hinweisen, dass das
# ziemlich anstrengend ist...
input("Puh, war das anstrengend!")
</code></pre>

--

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade in Python"

Dies ist eine Python-2 Version, das heißt, dass die Funktion "input" durch
"raw_input" ersetzt werden muss:
 
<iframe src="https://trinket.io/embed/python/cc2cb33b2d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

---

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade in Javascript"

**HTML Kode**

<pre><code class="fragment html">
&lt;html>
&lt;head>
  <title>Kaskade Demo</title>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
&lt;/head>
<body>
  <table>
    <tr>
      <td id="lo" class="ball"></td>
      <td class="white">
      </td>
      <td id="ro" class="ball">(1)</td>
    </tr>
    <tr> <td class="white"> </td> <td class="white"> </td> <td class="white"> </td> </tr>
    <tr>
      <td id="lu" class="hand left ball">(2)</td>
      <td class="white">
      </td>
      <td id="ru" class="hand right ball">(3)</td>
    </tr>
  </table>
  <button onclick="nextCatch();">Next Catch</button>
  ...
</code></pre>

--

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade in Javascript"

**CSS Kode**

<pre><code class="fragment css">
.white {
  color: red;
  width: 50px;
  height: 50px;
  background: lightgray;
}
.hand {
  border-bottom: 10px solid Orange;
}
.right {
  border-right: 10px solid Orange;
}
.left {
  border-left: 10px solid Orange;
}

.ball {
  font-size: 20px;
  color: Crimson;
  font-weight: bold;
  text-align: center;
  background: lightgray;
}
</code></pre>

--

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade in Javascript"

**JavaScript Kode**

<pre><code class="javascript">
function nextCatch() {

  // get items for all the values in the cells
  var ro = document.getElementById('ro');
  var lo = document.getElementById('lo');
  var ru = document.getElementById('ru');
  var lu = document.getElementById('lu');

  console.log(ro.innerHTML, lo.innerHTML);

  // get emtpy value 
  if (ro.innerHTML == '') {
    ro.innerHTML = lu.innerHTML;
    lu.innerHTML = '';
  }
  else if (lo.innerHTML == '') {
    lo.innerHTML = ru.innerHTML;
    ru.innerHTML = '';
  }
  else if (lu.innerHTML == '') {
    lu.innerHTML = lo.innerHTML;
    lo.innerHTML = '';
  }
  else if (ru.innerHTML == '') {
    ru.innerHTML = ro.innerHTML;
    ro.innerHTML = '';
  }
}
</code></pre>

--

## @head:"Praktische Beispiele"
### @subhead:"Die Dreiballkaskade in Javascript"

**DEMO**

<iframe src="../code/kaskade.html" style="width:600px;height:400px;"></iframe>

---

## @head:"Agenda 2015"

* @stroked:"Variablen"
    - @stroked:"... im Allgemeinen"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @stroked:"Datentypen"
    - @stroked:"... im Allgemeinen"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @stroked:"Praktische Beispiele"
    - @stroked:"Die Dreiballkaskade"
    - @stroked:"Die Dreiballkaskade in Python"
    - @stroked:"Die Dreiballkaskade in JavaScript"

---

@data-background:#000000

<p style="font-size:200px;color:white;font-weight:bold;">
ENDE
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
der ersten Sitzung
</p>
<p><code style="font-size:160px">sys.exit()</code></p>



