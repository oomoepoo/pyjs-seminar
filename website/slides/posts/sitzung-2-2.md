# Sitzung 2: Operatoren und Kontrollstrukturen

@data-background:#ffffff
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 2 (Tag 2)

----

#### 21.07.2015

----

### &quot;Operatoren und Kontrollstrukturen&quot;

---

## @head:"Agenda 2015"

* @unstroked:"Operatoren"
    - @unstroked:"Allgemeines"
    - @unstroked:"... in Python"
    - @unstroked:"... in JavaScript"
* @unstroked:"Kontrollstrukturen"
    - @unstroked:"Allgemeines"
    - @unstroked:"... in Python"
    - @unstroked:"... in JavaScript"

---

## @head:"Operatoren"
### @subhead:"Allgemeines"

**[Wikipedia zu Operatoren in der Mathematik](:wiki:Operator_(Mathematik))**
<blockquote class="fragment" style="line-height:40px">
Ein Operator ist eine mathematische Vorschrift (ein Kalkül), durch die man
aus mathematischen Objekten neue Objekte bilden kann. Er kann eine
standardisierte Funktion oder eine Vorschrift über Funktionen sein.
Anwendung finden die Operatoren bei Rechenoperationen, also bei manuellen
oder bei maschinellen Berechnungen.
</blockquote>

--

## @head:"Operatoren"
### @subhead:"Allgemeines"

**[Wikipedia zu Operatoren in der Logik](:wiki:Operator_(Logik))**

<blockquote class="fragment" style="line-height:40px">
Ein Logischer Operator ist eine Funktion, die einen Wahrheitswert liefert. Bei
der zweiwertigen, booleschen Logik liefert er also wahr oder falsch, bei einer
mehrwertigen Logik können auch entsprechend andere Werte geliefert werden.
</blockquote>

--

## @head:"Operatoren"
### @subhead:"Allgemeines"

**Vereinfachte Begriffserklärung**

* :fragment: Wenn wir uns den Operator als einen Verfertiger von Objekten vorstellen, dann heißt das, dass ein Operator *irgendetwas* mit *irgendetwas* anstellt. Entscheidend sind hierbei die Fragen, *was* der Operator tut, und *womit* der Operator etwas tut. ::
* :fragment: Ein Operator wandelt also eines oder mehrere Objekte in neue Objekte um. ::
* :fragment: Das, was umgewandelt wird, nennen wir die *Operanden* eines Operators. ::
* :fragment: Das, was der Operator mit den Operanden tut, nennen wir die *Operation*. ::
* :fragment: Der Plus-Operator wandelt bspw. zwei Zahlen in eine Zahl um, indem er die Operation *Addition* ausführt. ::

--

## @head:"Operatoren"
### @subhead:"Allgemeines"

**Klassifikation von Operatoren**

:fragment: Operatoren können nach verschiedenen Kriterien klassifiziert werden. Die grundlegendste Unterscheidung besteht in der Anzahl der Operanden, auf die ein Operator die Operation anwendet. Hierbei unterscheiden wir zwischen *unären* und *binären* Operatoren ::
    
- :fragment: *Unäre* Operatoren haben nur einen Operanden. ::
- :fragment: *Binäre* Operatoren haben zwei Operanden. ::

--

## @head:"Operatoren"
### @subhead:"Allgemeines"

**Klassifikation von Operatoren**

:fragment: Ferner kann zwischen *arithmetischen*, *logischen* und *relationalen* Operatoren unterschieden werden. ::

* :fragment: *Arithmentische* Operatoren führen arithmetische Operationen aus (Addition, Division, etc.). ::
* :fragment: *Logische* Operatoren liefern Aussagen über Wahrheitswerte (wahr oder falsch). ::
* :fragment: *Relationale* Operatoren liefern Aussagen über die Beziehungen zwischen Objekten (Identität, Zugehörigkeit). ::

--

## @head:"Operatoren"
### @subhead:"Allgemeines"

**Überladen von Operatoren**

* :fragment: Normalerweise werden Operatoren immer nur für spezifische Datentypen definiert. ::
* :fragment: Der Operator $+$ nimmt als Operanden bspw. gewöhnlich nur Zahlen. ::
* :fragment: In vielen Programmiersprachen ist es jedoch üblich, Operatoren, je nach Datentyp, auf den sie angewendet werden, unterschiedliche Operationen zuzuschreiben. ::
* :fragment: Diesen Vorgang nennt man das *Überladen* von Operatoren. ::
* :fragment: Wird der Additionsoperator $+$ bswp. auf den Datentyp *string* angewendet, so bewirkt er eine Verkettung von Strings (Konkatenation). ::
* :fragment: Das Überladen von Operatoren ermöglicht es, sehr kompakt und flexibel zu programmieren. ::

---

## @head:"Operatoren"
### @subhead:"... in Python"

**Allgemeines**

* :fragment: Die Operatoren in Python ähneln denen vieler Programmiersprachen. ::
* :fragment: Neben den durch mathematische Zeichen dargestellten Operatoren ($+$, $-$, $\*$) sind einige Operatoren auch als *Namen* (**is**, **in**) definiert. ::
* :fragment: Die Überladung von Operatoren ist ein entscheidender Wesenszug der Sprache. Viele Operatoren sind auf viele Datentypen anwendbar. ::

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Arithmetische Operatoren**

[<img src="img/operatoren.svg" alt="operatoren" style="width:600px;" />](img/operatoren.svg)

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Arithmetische Operatoren**

<pre><code class="python fragment" data-trim>
>>> x,y = 5,2
>>> +x
5
>>> -x
-5
>>> x + y
7
>>> x - y
3
>>> x * y
10
>>> x / y
2.5
>>> x // y
2
>>> x % y
1
>>> x ** y
25
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Logische Operatoren**

* :fragment: Die logischen Operatoren dienen dem Verarbeiten von Wahrheitswerten. ::
* :fragment: Jeder Wert bekommt in Python automatisch einen Wahrheitswert zugewiesen (**True** oder **False**). ::
* :fragment: Die Wahrheitswerte werden dem Datentyp *bool* zugeschrieben. ::
* :fragment: Negative Zahlen einschließlich der Zahl $0$ besitzen den Wahrheitswert **False**. ::
* :fragment: Alle "leeren" Werte (der leere String <code>""</code> oder die leere Liste <code>[]</code>) besitzen ebenfalls den Wahrheitswert **False**. ::
* :fragment: Die logischen Operatoren prüfen den Wahrheitswert von Werten und liefern als Ergebnis einen Wahrheitswert zurück. ::

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Logische Operatoren**

[<img src="img/logische_operatoren.svg" style="width:800px">](img/logische_operatoren.svg)

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Logische Operatoren**

[<img src="img/truth_table.svg" style="width:600px">](img/truth_table.svg)

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Logische Operatoren**

Wenn andere Werte als der Datentyp *bool* mit den Operatoren **and** und
**or** verknüpft werden, so wird immer einer der beiden Operanden
zurückgegeben, wobei die Bedingungen für die Rückgabe wie folgt sind:
    
* :fragment: [**and**] ::
    * :fragment: Wenn der erste Operand falsch ist, wird dieser zurückgegeben. ::
    * :fragment: Wenn der erste Operand wahr ist, wird der zweite Operand zurückgegeben. ::
* :fragment: [**or**] ::
    * :fragment: Wenn der erste Operand wahr ist, wird dieser zurückgegeben. ::
    * :fragment: Wenn der erste Operand falsch ist, wird der zweite Operand zurückgegeben. ::

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Logische Operatoren**

<pre><code class="python" data-trim>
>>> x,y = True,False
>>> not x
False
>>> not y
True
>>> x and y
False
>>> x or y
True
>>> x,y = False,False
>>> not x and not y
True
>>> x and y
False
>>> x or y
False
>>> x,y = 'harry','potter'
>>> x and y
'potter'
>>> x or y
'harry'
>>> x = False
>>> x and y
False
>>> x or y
'potter'
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Relationale Operatoren**

* :fragment: Relationale Operatoren liefern immer einen Wahrheitswert in Bezug auf die Relation zurück, die überprüft werden soll. ::
* :fragment: Bei den relationalen Operatoren kann zwischen Vergleichs-, Element- und Identitätsoperatoren unterschieden werden. ::
    * :fragment: Vergleichsoperatoren dienen dem Vergleich von Operanden hinsichtlich ihrer Werte. ::
    * :fragment: Zugehörigkeitsoperatoren dienen der Ermittlung der Zugehörigkeit eines Operanden zu anderen Operanden. ::
    * :fragment: Identitätsoperatoren dienen der Ermittlung von Identitätsverhältnissen, wobei Identität von Gleichheit ähnlich abgegrenzt wird wie dies im Deutschen mit Hilfe der Wörter *dasselbe* vs. *das gleiche* getan wird. ::

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Relationale Operatoren**

[<img src="img/relationale_operatoren.svg" style="width:700px">](img/relationale_operatoren.svg)

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Relationale Operatoren: Vergleichsoperatoren**

<pre><code class="python" data-trim>
>>> x,y = 5,10
>>> x > y
False
>>> x < y
True
>>> x == y
False
>>> x != y
True
>>> x <= y
True
>>> x >= y
False
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Relationale Operatoren: Zugehörigkeitsoperatoren**

<pre><code class="python" data-trim>
>>> x,y = 'doculect','cul'
>>> x in y
False
>>> y in x
True
>>> x not in y
True
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in Python"

**Relationale Operatoren: Identitätsoperatoren**

<pre><code class="python" data-trim>
>>> x = 1,2
>>> y = x
>>> x is y
True
>>> y = 1,2
>>> x is y
False
</code></pre>

---

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Arithmetische Operatoren**

Die arithmetischen Operatoren in JavaScript sind im Großen und Ganzen identisch mit denen in Python. Lediglich der Potenz-Operator <code>\*\*</code> existiert nicht. 

--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Arithmetische Operatoren**

<pre><code class="javascript" data-trim>
> var x = 5; var y = 2;
> +x;
5
> -x;
-5
> x + y;
7
> x - y;
3
> x * y;
10
> x / y;
2.5
> x // y;
2
> x % y;
1
> Math.pow(x,y); // x ** y in Python
25
</code></pre>
--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Logische Operatoren**

Funktionell sind die logischen Operatoren in JavaScript identisch mit denen in Python, jedoch werden an Stelle der Schlüsselwörter **and**, **or** und **not** in JavaScript die Zeichen **\&\&**, **||** und **!** verwendet. Ferner werden die beiden Werte des Datentyps **bool** klein geschrieben (**true** und **false** anstelle von **True** und **False**).

--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Logische Operatoren**

<pre><code class="javascript" data-trim>
> var x = true; var y = false
> !x; // not x in Python
false
> !y // not y in Python
true
> x && y // x and y in Python
false
> x || y // x or y in Python
true
> var x = false; var y = false;
> ! x && ! y // not x and not y in Python
true
> x && y
false
> x || y
false
> var x = 'harry'; var y = 'potter';
> x && y
'potter'
> x || y
'harry'
> var x = False
> var x && y
false
>>> x || y
'potter'
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Relationale Operatoren**

Auch die relationalen Operatoren in JavaScript sind denen in Python sehr ähnlich. Es fehlen jedoch die Operatoren **in** und **not in**. Anstelle der Schlüsselwörter **is** und **is not** werden die Symbole **===** und **!==** verwendet.

--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Relationale Operatoren: Vergleichsoperatoren**

<pre><code class="javascript">
> var x = 5; var y = 10;
> x > y
false
> x < y
true
> x == y
false
> x != y
true
> x <= y
true
> x >= y
false
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Relationale Operatoren: Vergleichsoperatoren**

<pre><code class="javascript">
> var x = 'doculect'; var y = 'cul';
> y.indexOf(x) != -1 // x in y in Python
false
> x.indexOf(y) != -1 // y in x in Python
true
> y.indexOf(x) == -1 // x not in y in Python
true
</code></pre>

--

## @head:"Operatoren"
### @subhead:"... in JavaScript"

**Relationale Operatoren: Vergleichsoperatoren**

<pre><code class="javascript">
> var x = [1, 2] // x = [1,2] in Python
> var y = x
> x === y // x is y in Python
true
> y = [1, 2] 
> x === y // x is y in Python
false
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Operatoren"
    - @stroked:"Allgemeines"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @unstroked:"Kontrollstrukturen"
    - @unstroked:"Allgemeines"
    - @unstroked:"... in Python"
    - @unstroked:"... in JavaScript"

---

## @head:"Kontrollstrukturen"
### @subhead:"Allgemeines"

**[Gängige Begriffserklärung aus Wikipedia](:wiki:Kontrollstruktur)**

<blockquote class="fragment">
Kontrollstrukturen (Steuerkonstrukte) werden in imperativen
Programmiersprachen verwendet, um den Ablauf eines Computerprogramms zu
steuern. Eine Kontrollstruktur gehört entweder zur Gruppe der Verzweigungen
oder der Schleifen. Meist wird ihre Ausführung über logische Ausdrücke der
booleschen Algebra beeinflusst.
</blockquote>

--

## @head:"Kontrollstrukturen"
### @subhead:"Allgemeines"

**Begriffserklärung in [Weigend (2008:127)](:bib:Weigend2008)**

<blockquote class="fragment">
Kontrollstrukturen legen fest, in welcher Reihenfolge und unter welchen
Bedingungen die Anweisungen eines Programms abgearbeitet werden.
</blockquote>

--

## @head:"Kontrollstrukturen"
### @subhead:"Allgemeines"

**Typen von Kontrollstrukturen**

* :fragment: **Verzweigungen** kontrollieren den Fluss eines Programms, indem sie dieses, abhängig von bestimmten Gegebenheiten, in unterschiedliche Bahnen lenken ::
* :fragment: **Schleifen** kontrollieren den Fluss eines Programms, indem sie Operationen wiederholt auf Objekte anwenden ::

--

## @head:"Kontrollstrukturen"
### @subhead:"Allgemeines"

**Typen von Kontrollstrukturen**

[<img src="img/kontrollstrukturen.svg" alt="ks" style="width:800px" />](img/kontrollstrukturen.svg)

--


## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Allgemeines**

* :fragment: Python kennt insgesamt vier verschiedene Kontrollstrukturen: zwei Verzweigungsstrukturen (**if**, **try**) und zwei Schleifenstrukturen (**for**, **while**). ::
* :fragment: Das besondere an den Kontrollstrukturen in Python ist deren enge Anbindung an logische Ausdrücke, welche einen sehr kompakten, sehr leicht verständlichen Kode erlauben. ::

--
## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Verzweigungen: if, elif, und else**

* :fragment: Bei der **if**-Verzweigung wird ein Programmabschnitt unter einer bestimmten Bedingung ausgeführt. ::
* :fragment: Dabei wird eine Bedingung auf ihren Wahrheitswert getestet. Trifft sie zu, wird das Programm entsprechend weitergeführt. Trifft sie nicht zu, unterbleibt der Abschnitt. ::
* :fragment: Es können auch mehrere Bedingungen auf ihren Wahrheitswert überprüft und entsprechend mehrere verschiedene Programmabschnitte aktiviert werden. ::
* :fragment: Es gibt in Python auch die Möglichkeit, *nichts* zu tun, wenn eine Bedingung zutrifft. Dies muss durch das Schlüsselwort **pass** festgelegt werden. ::

--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Verzweigungen: if, elif, und else**

<pre><code class="python" data-trim>
>>> x, y, yes, no = 10, 0, "yes", "no"
>>> if x: print(yes)
yes
>>> if y: print(yes)
>>> if not x: print(yes)
    elif not y: print no
no
>>> if 1 > 10: print("Eins ist groesser als zehn.")
    elif 1 < 10: print("Eins ist kleiner als zehn.")
Eins ist kleiner als zehn.
>>> if x or y: print("Einer von beiden Werten ist wahr.")
    else: print("Keiner von beiden Werten ist wahr.")
Einer von beiden Werten ist wahr.
>>> if x == 10: pass
    else: print("Danke, Herr Jauch!")
</code></pre>

--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Verzweigungen: try und except**

* :fragment: Eine sehr wichtige und nützliche Verzweigunsstruktur bietet Python mit **try** und **except**. ::
* :fragment: Hierbei wird nicht eine Bedingung auf ihren Wahrheitswert überprüft, sondern getestet, ob ein Statement eine Fehlermeldung hervorruft. ::
* :fragment: Auf diese Weise kann man gezielt auf mögliche Fehler reagieren. ::
* :fragment: Fehler können dabei gezielt entsprechend ihrer Klasse eingeordnet werden. ::
* :fragment: Auf diese Weise können gezielt bestimmte Fehler angesprochen werden, die vom Programm ignoriert werden sollen. ::
        
--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Verzweigungen: try und except**

<pre><code class="python" data-trim>
>>> try: x = int(input())
    except: print("Der Wert, den Sie eingegeben haben, ist kein Integer!")
2
>>> try: x = int(input())
    except ValueError: print("Der Wert, den Sie eingegeben haben, ist kein Integer!")
2.0
Der Wert, den Sie eingegeben haben, ist kein Integer!"
>>> x = input()
10
>>> x, y = 10, 0 
>>> try: x / y
    except ZeroDivisionError: print("Durch Null kann man nicht teilen!")
Durch Null kann man nicht teilen.
>>> try: x = int(input())
    except ValueError: print("Falscher Wert für Integer!")
10.0
Falscher Wert für Integer!
</code></pre>

--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Schleifen: while**

* :fragment: Mit Hilfe von Schleifenkonstruktionen werden Blöcke von Anweisungen in Programmen wiederholt ausgeführt, bis eine Abbruchsbedingung eintritt, bzw. so lange eine Bedingung zutrifft. ::
* :fragment: Wie für Verzweigunsstrukturen werden auch die Bedingungen in Schleifen auf Grundlage der Auswertung von Wahrheitswerten errechnet. ::
* :fragment: Der Abbruch einer Schleife kann in Python bewusst durch das Schlüsselwort **break** gesteuert werden. ::

--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Schleifen: while**

<pre><code class="python">
>>> a = 10
>>> while a > 0: 
        print(a," ist groesser als 0.")
        a -= 1 # wir lassen der Wert gegen 0 laufen

10 ist groesser als 0
9 ist groesser als 0
8 ist groesser als 0
7 ist groesser als 0
6 ist groesser als 0
5 ist groesser als 0
4 ist groesser als 0
3 ist groesser als 0
2 ist groesser als 0
1 ist groesser als 0
>>> while True:
        b = input("Sag was: ")
        print b
        if not b:
            print("Aaaaaabbbbbrrrrruuuuccccccch!")
            break
Sag was: bla
bla
Sag was: bloed
bloed
Aaaaaabbbbbrrrrruuuuccccccch!
</code></pre>
--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Schleifen: for**
    
* :fragment: Während bei der **while**-Schleife die Abbruchsbedingung immer explizit genannt werden muss, gilt dies nicht für die **for**-Schleife. :: 
* :fragment: Hier wird explizit und im Voraus festgelegt, wie oft, bzw. in Bezug auf welche Objekte eine bestimmte Operation ausgeführt werden soll, weshalb sich die **for**-Schleife anbietet, wenn man die Anzahl der Operationen kennt, die man durchführen will. ::
* :fragment: Der Bereich, in dem in Python eine Operation mit Hilfe der **for**-Schleife ausgeführt wird, wird zumeist mit Hilfe der Funktion **range()** angegeben, welche automatisch eine Liste von Integern erzeugt, über die dann iteriert wird. ::

--

## @head:"Kontrollstrukturen"
### @subhead:"... in Python"

**Schleifen: for**

<pre><code class="python" data-trim>
>>> a = range(5)
>>> a
range(0,5)
>>> list(a)
[0, 1, 2, 3, 4]
>>> for i in range(5): print(i)
0
1
2
3
4
>>> einkaufsliste = ['mehl','butter','zitronen','bier']
>>> for element in einkaufsliste: print element
mehl
butter
zitronen
bier
>>> namen = ['peter','frank','karl','jan']
>>> for name in namen: print(name)
peter
frank
karl
jan
>>> woerter = ['haus','kaffee','getraenk','wasser','flasche']
>>> for wort in woerter: print(wort)
haus
kaffee
getraenk
wasser
flasche
</code></pre>

---

## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Verzweigungen: if, else if und else**

Die if-else-Verzweigung in JavaScript unterscheidet sich in ihrer Syntax von Python, nicht jedoch in der grundlegenden Konzeption, auf der sie aufbaut. Auch in JavaScript wird der Wahrheitswert einer Datenstruktur getestet und entsprechend reagiert. Anstelle von "elif" wird dabei in javaScript "else if" geschrieben. Ferner werden hässliche Klammern verwendet anstelle der schönen Einrückungen, die in Python verwendet werden.

--
## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Verzweigungen: if, else if und else**

<pre><code class="javascript" data-trim>
> var x = 10; var y = 0; var yes = 'yes'; var no = 'no';
> if (x) {console.log(yes);} // if x: print(yes) in Python
yes
> if (y) {console.log(yes);} // if y: print(yes) in Python 
>>> if (!x) {console.log(yes);}
    else if(!y) { console.log(no);}
no
>>> if (1 > 10) {console.log("Eins ist groesser als zehn.");}
    else if (1 < 10) {console.log("Eins ist kleiner als zehn.");}
Eins ist kleiner als zehn.
>>> if (x || y) {console.log("Einer von beiden Werten ist wahr.");} // if x or y in Python
    else {console.log("Keiner von beiden Werten ist wahr.");}
Einer von beiden Werten ist wahr.
>>> if (x == 10) {}
    else {console.log("Danke, Herr Jauch!");}
</code></pre>

--

## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Verzweigungen: try und catch**

Anstelle von **try** und **except** bietet JavaScript die Verzweigung **try** und **catch** an. Die Syntax ist auch hier wieder anders als in Python, die grundlegende Struktur ist jedoch sehr ähnlich. Allerdings sollte man diese Verzweigung nach Möglichkeit nur spärlich anwenden, da eine Vielzahl von Fehlern in JavaScript nicht als solche definiert werden. So führt eine Division durch 0 beispielsweise nicht zu einem ZeroDivisionError, sondern zum Wert *Infinity*. Ferner führt der Befehl <code>parseInt('m')</code> nicht zu einem ValueError, sondern zum Wert *NaN*. Aus diesem Grund werden **try** und **catch** hier nicht weiter behandelt. 

--

## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Schleifen: while**

Abgesehen von der Verwendung der hässlichen Klammerstrukturen funktioniert die **while**-Schleife in JavaScript im Prinzip genauso wie die **while**-Schleife in Python. Auch das Schlüsselwort **break** kann verwendet werden.

--

## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Schleifen: while**

<pre><code class="javascript" data-trim>
> var a = 10
> while (a > 0) { console.log(a+" ist groesser als 0."); a -= 1;}
10 ist groesser als 0
9 ist groesser als 0
8 ist groesser als 0
7 ist groesser als 0
6 ist groesser als 0
5 ist groesser als 0
4 ist groesser als 0
3 ist groesser als 0
2 ist groesser als 0
1 ist groesser als 0
> var a = 10;
> while(true){a -= 1; console.log(a+' ist groesser als 0'); if(a == 0){break;}}
9 ist groesser als 0 
8 ist groesser als 0 
7 ist groesser als 0 
6 ist groesser als 0 
5 ist groesser als 0 
4 ist groesser als 0 
3 ist groesser als 0 
2 ist groesser als 0 
1 ist groesser als 0 
0 ist groesser als 0 
</code></pre>

--

## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Schleifen: for**

In Bezug auf die **for**-Schleife unterscheiden sich Python und JavaScript ein wenig mehr als in Bezug auf die anderen Kontrollstrukturen. Während die **for**-Schleife in Python generell auf der Datenstruktur von iterierbaren Elementen (vorrangig Listen) aufbaut, wird in JavaScript eine explizite Zählerstruktur benötigt. Zwar gibt es auch ein **for value in iterable**-Konstrukt in JavaScript, jedoch gibt dies nur die Schlüsselwerte von Objekten (**dictionaries** in Python) aus und sollte nie zusammen mit Arrays verwendet werden. 

--

## @head:"Kontrollstrukturen"
### @subhead:"... in JavaScript"

**Schleifen: for**

<pre><code class="javascript" data-trim>
> var liste = ["a", "b", "c", "d"];
> for (var i=0; i < liste.length; i++) {console.log(i, liste[i]);}
0 'a'
1 'b'
2 'c'
3 'd'
> for (var i=0,elm; elm=liste[i]; i++) {console.log(i, elm);}
0 'a'
1 'b'
2 'c'
3 'd'
> var myobj = {"a":1, "b":2, "c":3, "d":4};
> for (key in myobj) {console.log(key, myobj[key]);}
a 1
b 2
c 3
d 4
</code></pre>

---

## @head:"Agenda 2015"

* @stroked:"Operatoren"
    - @stroked:"Allgemeines"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
* @stroked:"Kontrollstrukturen"
    - @stroked:"Allgemeines"
    - @stroked:"... in Python"
    - @stroked:"... in JavaScript"
---

@data-background:#000000

<p style="font-size:200px;color:white;font-weight:bold;">
sys.exit()
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
der zweiten Sitzung
</p>
<p><code style="font-size:160px">88</code></p>



