# Sitzung 3: Funktionen


@data-background:#ffffff
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 3 (Tag 2)

----

#### 21.07.2015

----

### &quot;Funktionen&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Funktionen im Allgemeinen"
    * @unstroked:"Begriffserklärung"
    * @unstroked:"Typen von Funktionen"
* @unstroked:"Funktionen in Python"
    * @unstroked:"Grundlagen"
    * @unstroked:"Parameter und Schlüsselwörter"
    * @unstroked:"Spezialfälle"
* @unstroked:"Funktionen in JavaScript"
    * @unstroked:"Grundlagen"
    * @unstroked:"Parameter und Schlüsselwörter"
    * @unstroked:"Spezialfälle"

---

## @head:"Funktionen im Allgemeinen"
### @subhead:"Begriffserklärung"

**[Funktionen in der Mathematik (laut Wikipedia)](:wiki:Funktion (Mathematik))**

<blockquote class="fragment">
In der Mathematik ist eine Funktion oder Abbildung eine Beziehung zwischen
zwei Mengen, die jedem Element der einen Menge (Funktionsargument,
unabhängige Variable, x-Wert) genau ein Element der anderen Menge
(Funktionswert, abhängige Variable, y-Wert) zuordnet. Das Konzept der
Funktion oder Abbildung nimmt in der modernen Mathematik eine zentrale
Stellung ein; es enthält als Spezialfälle unter anderem parametrische
Kurven, Skalar- und Vektorfelder, Transformationen, Operationen, Operatoren
und vieles mehr. 
</blockquote>

--

## @head:"Funktionen im Allgemeinen"
### @subhead:"Begriffserklärung"

**[Funktionen in der Programmierung (laut Wikipedia)](:wiki:Funktion (Programmierung))**

<blockquote class="fragment">
Eine Funktion (engl.: function, subroutine) ist in der Informatik die
Bezeichnung eines Programmierkonzeptes, das große Ähnlichkeit zum Konzept
der Prozedur hat. Hauptmerkmal einer Funktion ist es, dass sie ein Resultat
zurückliefert und deshalb im Inneren von Ausdrücken verwendet werden kann.
Durch diese Eigenschaft grenzt sie sich von einer Prozedur ab, die nach
ihrem Aufruf kein Ergebnis/Resultat zurück liefert. Die genaue Bezeichnung
und Details ihrer Ausprägung ist in verschiedenen Programmiersprachen
durchaus unterschiedlich.
</blockquote>

--

## @head:"Funktionen im Allgemeinen"
### @subhead:"Typen von Funktionen"

Da entscheidend für Funktionen der Eingabewert und der Rückgabewert sind,
können wir ganz grob die folgenden speziellen Typen von Funktionen 
identifizieren:

* :fragment: Funktionen ohne Rückgabewert (Prozedur) ::
* :fragment: Funktionen ohne Eingabewert ::
* :fragment: Funktionen mit einer festen Anzahl von Eingabewerten ::
* :fragment: Funktionen mit einer beliebigen Anzahl von Eingabewerten ::

---

## @head:"Agenda 2015"

* @stroked:"Funktionen im Allgemeinen"
    * @stroked:"Begriffserklärung"
    * @stroked:"Typen von Funktionen"
* @unstroked:"Funktionen in Python"
    * @unstroked:"Grundlagen"
    * @unstroked:"Parameter und Schlüsselwörter"
    * @unstroked:"Spezialfälle"
* @unstroked:"Funktionen in JavaScript"
    * @unstroked:"Grundlagen"
    * @unstroked:"Parameter und Schlüsselwörter"
    * @unstroked:"Spezialfälle"

---

## @head:"Funktionen in Python"
### @subhead:"Grundlagen"

**Vorweg**

In Python sind Funktionen spezielle Datentypen. Sie unterscheiden sich von
anderen Datentypen wie **strings** oder **integers** dadurch, dass sie
zusätzlich aufgerufen werden können (*callable types*).

--

## @head:"Funktionen in Python"
### @subhead:"Grundlagen"

**Allgemeine Struktur**

<pre><code class="python" data-trim>
def functionName(
        parameterA,
        ...,
        keywordA='defaultA',
        ...,
        ):
    """
    docString
    """
    functionBody
    return functionValue
</code></pre>

--

## @head:"Funktionen in Python"
### @subhead:"Grundlagen"

**Erstes Beispiel**

<pre><code class="python data-trim">
def stoneAgeCalculator(intA, intB, calc='+'):
    """
    This is the famous stoneAgeCalculator, a program written by the very first
    men on earth who brought the fire to us and were the first to dance naked
    on the first of May.
    """
    # check for inconsistencies in the input for keyword calc
    if calc not in ['+', '-', '*', '/']:
        raise ValueError('The operation you chose is not defined.')

    # start the calculation, catch errors from input with a simple
    # try-except-structure
    try:
        if calc == '+':
            return intA + intB
        elif calc == '-':
            return intA - intB
        elif calc == '*':
            return intA * intB
        else:
            return intA / intB
    except:
        raise ValueError('No way to operate on your input.')
</code></pre>

--

## @head:"Funktionen in Python"
### @subhead:"Grundlagen"

**Aufrufen und Ausführen**

> Eine Funktion wird aufgerufen, indem der Name der Funktion angegeben wird,
> gefolgt von einer Liste aktueller Parameter in Klammern.
> [(Weigend 2008:144)](:bib:Weigend2008)

<pre><code class="fragment python" data-trim>
>>> a = range(5)
>>> a = int('1')
>>> range(5)
range(0,5)
>>> int('1')
1
>>> float(1)
1.0
>>> print('Hallo Welt!')
Hallo Welt!
>>> list('hallo')
['h', 'a', 'l', 'l', 'o']
</code></pre>

--

## @head:"Funktionen in Python"
### @subhead:"Grundlagen"

**Die Funktionsdokumentation**

Für jede Funktion, die in Python definiert wird, steht eine automatische
Dokumentation bereit, welche mit Hilfe der Parameter und der Angaben im
Docstring generiert wird. Die Dokumentation einer Funktion wird mit Hilfe von
<code>help(function)</code> aufgerufen. Mit Hilfe der Funktionsdokumentation
lässt sich leicht ermitteln, welche Eingabewerte eine Funktion benötigt, wie
sie verwendet wird, und welche Werte sie zurückliefert. Docstrings lassen sich
am besten interaktiv einsehen.

--

## @head:"Funktionen in Python"
### @subhead:"Parameter und Schlüsselwörter"

**Parameter**

Mit Hilfe von Funktionen werden Eingabewerte (Parameter) in Ausgabewerte
umgewandelt. Bezüglich der Datentypen von Eingabewerten gibt es in Python keine
Grenzen. Alle Datentypen (also auch Funktionen selbst) können daher als
Eingabewerte für Funktionen verwendet werden. Gleichzeitig ist es möglich,
Funktionen ohne Eingabewerte oder ohne Ausgabewerte zu definieren. Will man
eine beliebige Anzahl an Parametern als Eingabe einer Funktion verwenden, so
erreicht man dies, indem man der Parameterbezeichnung einen Stern (\*)
voranstellt. Die Parameter von Eingabeseite werden innerhalb der Funktion dann
automatisch in eine Liste umgewandelt, auf die mit den normalen
Listenoperationen zugegriffen werden kann.

--

## @head:"Funktionen in Python"
### @subhead:"Parameter und Schlüsselwörter"

**Parameter**

<pre><code class="python" data-trim>
>>> def leer():
...     print "leer"
>>> def empty():
...     pass
>>> def gruss1(wort):
...     print wort
>>> def gruss2(wort):
...     return wort
>>> def eins():
...     """Gibt die Zahl 1 aus."""
...     return 1
>>> leer()
leer
>>> empty
... <function empty at 0xb76ef374>
>>> empty()
>>> type(empty)
<type 'function'>
>>> a = eins()
>>> a
1
>>> print bla.func_doc
Gibt die Zahl 1 aus.
>>> def printWords(\*words):
...     for word in words:
...         print(word)
...
>>> printWords('mama','papa','oma',opa')
mama
papa
oma
opa
</code></pre>

--

## @head:"Funktionen in Python"
### @subhead:"Parameter und Schlüsselwörter"

**Schlüsselwörter**

Als Schlüsselwörter bezeichnet man Funktionsparameter, die mit einem
Standardwert belegt sind. Werden diese beim Funktionsaufruf nicht angegeben,
gibt es keine Fehlermeldung, sondern anstelle der fehlenden Werte wird einfach
auf den Standardwert zurückgegriffen. Gleichzeitig braucht man beim Aufrufen
nicht auf die Reihenfolge der Parameter zu achten, da diese ja durch die
Anbindung der Schlüsselwörter vordefiniert ist. Weist eine Funktion hingegen
Schlüsselwörter und Parameter auf, so müssen die Parameter den Schlüsselwörtern
immer vorangehen.

--

## @head:"Funktionen in Python"
### @subhead:"Parameter und Schlüsselwörter"

**Schlüsselwörter**

<pre><code class="python" data-trim>
>>> def wind(country, season='summer')
...     """Return the typical wind conditions for a given country."""
...     if country == "Germany" and season == 'summer':
...         print("There's strong wind in",country)
...     else:
...         print("This part hasn't been programmed yet.")
...
>>> wind('Germany'):
There's strong wind in Germany.
>>> wind('Germany,season='winter')
This part hasn't been programmed yet.
</code></pre>

--

## @head:"Funktionen in Python"
### @subhead:"Spezialfälle"

**Prozeduren**

> Prozeduren sind Funktionen, die den Wert **None** zurückgeben. Fehlt in
> einer Funktionsdefinition die **return**-Anweisung, wird automatisch der
> Wert **None** zurückgegeben. [(Weigend 2008: 155)](:bib:Weigend2008)

<pre><code class="fragment python" data-trim>
>>> def quak(frosch=''):
...     print("quak")
...
>>> quak()
quak
>>> a = quak()
quak
>>> type(a)
<type 'NoneType'>
</code></pre>
--

## @head:"Funktionen in Python"
### @subhead:"Spezialfälle"

**Rekursive Funktionen**

> Rekursive Funktionen sind solche, die sich selbst aufrufen.
> [(Weigend 2008: 151)](:bib:Weigend2008)

<pre><code class="fragment python">
>>> def factorial(number):
...     """
...     Aus: http://www.dreamincode.net/code/snippet2800.htm
...     """
...     if number == 0:
...         return 1
...     else:
...         value = factorial(n-1)
...         result = n * value
...         return result
...
>>> factorial(4)
24
</code></pre>
--

## @head:"Funktionen in Python"
### @subhead:"Spezialfälle"

**Globale und lokale Variablen**

Es muss bei Funktionen zwischen lokalen und globalen Variablen unterschieden
werden. Lokale Variablen haben nur innerhalb einer Funktion ihren
Gültigkeitsbereich. Globale Variablen hingegen gelten auch außerhalb der
Funktion. Will man mit Hilfe einer Funktion eine Variable, die global, also
außerhalb der Funktion deklariert wurde, verändern, so muss man ihr das 
*Keyword* **global** voranstellen. Dies sollte man jedoch nach Möglichkeit
vermeiden, da dies schnell zu Fehlern im Programmablauf führen kann. Lokale und
globale Variablen sollten nach Möglichkeit getrennt werden.

--

## @head:"Funktionen in Python"
### @subhead:"Spezialfälle"

**Globale und lokale Variablen**

<pre><code class="python" data-trim>
>>> s = 'globaler string'
>>> def f1():
...     print(s)
...
>>> def f2():
...     s = 'lokaler string'
...     print(s)
...
>>> f1()
globaler string
>>> f2()
lokaler string
>>> def f3():
...     global s
...     s = 'lokaler string'
...     print(s)
>>> s = 'globaler string'
>>> f3()
lokaler string
>>> print(s)
lokaler string
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Funktionen im Allgemeinen"
    * @stroked:"Begriffserklärung"
    * @stroked:"Typen von Funktionen"
* @stroked:"Funktionen in Python"
    * @stroked:"Grundlagen"
    * @stroked:"Parameter und Schlüsselwörter"
    * @stroked:"Spezialfälle"
* @unstroked:"Funktionen in JavaScript"
    * @unstroked:"Grundlagen"
    * @unstroked:"Parameter und Schlüsselwörter"
    * @unstroked:"Spezialfälle"

---

## @head:"Funktionen in JavaScript"
### @subhead:"Grundlagen"

**Allgemeines vorweg**

<p class="fragment">Wie in Python, so sind auch in JavaScript Funktionen spezielle Datentypen.</p>

**Allgemeine Struktur**

<pre><code class="javascript fragment" data-trim>
function functionName (
  parameterA,
  parameterB,
  parameterC,
  ...
  ) {

  functionBody;
  
  return functionValue;
}
</code></pre>

--

## @head:"Funktionen in JavaScript"
### @subhead:"Grundlagen"

**Erstes Beispiel: Der Steinzeittaschenrechner**

<pre><code class="javascript">
function stoneAgeCalculator(intA, intB, calc) {
  /* This is a very famous StoneAge Calculator. */

  /* check for active values for type */
  if (typeof calc == 'undefined') {
    calc = "+";
  }
  /* check for correct values for calc */
  else if(["+", "-", "*", "/"].indexOf(calc) == -1) {
    return false;
  }

  /* return the stuff */
  if (calc == '+') {return intA + intB;}
  else if (calc == '-') {return intA - intB;}
  else if (calc == '*') {return intA * intB;}
  else if (calc == '/') {return intA / intB;}
  return false;
}
</code></pre>

--

## @head:"Funktionen in JavaScript"
### @subhead:"Grundlagen"

**Erstes Beispiel: Der Steinzeittaschenrechner**

<iframe style="width:900px;height:600px;" src="../demos/console.html"></iframe>

--

## @head:"Funktionen in JavaScript"
### @subhead:"Parameter und Schlüsselwörter"

**Parameter und Schlüsselwörter**

Die Handhabung von Parametern und Schlüsselwörtern ist nicht so leicht in JavaScript wie in Python. Schlüsselwörter gibt eigentlich gar nicht. Das heißt leider auch, dass man keine Standardwerte für bestimmte Parameter annehmen kann, was das Programmieren ein wenig umständlich macht. Um ähnliche Funktionalitäten wie in Python zu erlangen, behilft man sich meist mit Ersatzkonstruktionen.

--

## @head:"Funktionen in JavaScript"
### @subhead:"Parameter und Schlüsselwörter"

**Parameter und Schlüsselwörter**

<pre><code class="javascript">
function wind(country, season) {
  /* Return the typical wind conditions for a country */

  /* carry out type check of season, to set the basic value */
  if (typeof season == "undefined") {
    season = "summer";
  }

  if (country == "Germany" and season == "summer") {
    return "There's strong wind in "+country+".";
  }
  else {
    return "This part hasn't been programmed yet.";
  }
}
</code></pre>

--

## @head:"Funktionen in JavaScript"
### @subhead:"Parameter und Schlüsselwörter"

**Parameter und Schlüsselwörter**

<iframe style="width:900px;height:600px;" src="../demos/console.html"></iframe>

--

## @head:"Funktionen in JavaScript"
### @subhead:"Spezialfälle"

**Prozeduren und Rekursive Funktionen**

Prozeduren und rekursive Funktionen können in JavaScript genauso verwendet werden wie in Python. Tendentiell werden sehr viel mehr Prozeduren in JavaScript verwendet, da das Auslösen von Aktionen mit Hilfe der HTML-Buttons und der "onclick"-Anweisung am leichtesten geregelt werden kann. 

--

## @head:"Funktionen in JavaScript"
### @subhead:"Spezialfälle"

**Globale und lokale Variablen**

JavaScript unterscheidet nicht direkt zwischen globalen und lokalen Variablen: Alles, was auf einer jeweils höheren Ebene definiert wurde, kann auch auf einer niedrigeren Ebene verwendet werden und umgekehrt. Das Schlüsselwort **var** kann jedoch verwendet werden, um zu gewährleisten, dass Variablen nur innerhalb ihrer jeweiligen Ebene Geltung haben. Sicherheitshalber sollte man daher vor jede Variablendeklaration das Schlüsselwort **var** setzen. 

--

## @head:"Funktionen in JavaScript"
### @subhead:"Spezialfälle"

**Globale und lokale Variablen**

<pre><code class="javascript" data-trim>
> s = 'globaler string'
> function f1(){console.log(s)}
> function f2(){s = 'lokaler string'; console.log(s);}
> f1()
'globaler string'
> f2()
'lokaler string'
> function f3() { var s; s = 'lokaler string'; console.log(s);}
> s = 'globaler string';
> f3()
lokaler string
> s 
globaler string
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Funktionen im Allgemeinen"
    * @stroked:"Begriffserklärung"
    * @stroked:"Typen von Funktionen"
* @stroked:"Funktionen in Python"
    * @stroked:"Grundlagen"
    * @stroked:"Parameter und Schlüsselwörter"
    * @stroked:"Spezialfälle"
* @stroked:"Funktionen in JavaScript"
    * @stroked:"Grundlagen"
    * @stroked:"Parameter und Schlüsselwörter"
    * @stroked:"Spezialfälle"

---

@data-background:#000000

<p style="font-size:120px;color:white;font-weight:bold;">
window.close();
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
der dritten Sitzung
</p>



