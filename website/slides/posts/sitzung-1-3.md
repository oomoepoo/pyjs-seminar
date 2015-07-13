# Sitzung 3: Erste Schritte in JavaScript

@data-background:LightYellow
@data-transition:concave
@style:text-align:justify;
@style:font-size:85%;

---

@style:text-align:center;font-size:100%;

## Computergestützter Sprachvergleich mit Python und JavaScript

----

### Sitzung 3 (Tag 1)

----

#### 20.07.2015

----

### &quot;Erste Schritte in JavaScript&quot;

---

## @head:"Agenda 2015"

* @unstroke:"Allgemeines zu JavaScript"
    - @unstroke:"Herkunft"
    - @unstroke:"Charakteristik"
    - @unstroke:"Installation"
* @unstroke:"Bibliotheken und Entwickertools"
    - @unstroke:"Webbrowser"
    - @unstroke:"Bibliotheken"
    - @unstroke:"Entwicklertools"
* @unstroke:"Ein erstes Programmierbeispiel"
    - @unstroke:"HTML und CSS"
    - @unstroke:"Die Kölner Phonetik in JavaScript"
    - @unstroke:"Interaktives Beispiel"

---

## @head:"Allgemeines zu JavaScript"
### @subhead:"Herkunft"

[JavaScript](:wiki:JavaScript)

* @fragment:"ist eine Skriptsprache, die speziell für dynamisches HTML in Webbrowsern entwickelt wurde"
* @fragment:"verändert Inhalte von Webseiten, reagiert auf Benutzereingaben, und erweitert die Möglichkeiten von HTML und CSS"
* @fragment:"ist ein abtrünniges Kind von C, was die hässliche Syntax angeht und hat mit Java selbst sehr wenig zu tun (obwohl die Syntax von Java auch sehr hässlich ist)"
* @fragment:"wurde ursprünglich von Netscape entwickelt und im Jahre 1996 in der Version 1.1 veröffentlicht"

--

## @head:"Allgemeines zu JavaScript"
### @subhead:"Charakteristik"

[JavaScript](:wiki:JavaScript)

* @fragment:"hat eine sehr hässliche Syntax"
* @fragment:"ist prinzipiell nicht sehr schwer zu erlernen, sieht aber hässlich aus"
* @fragment:"erlaubt es den Benutzern, sehr, sehr hässlichen Kode zu schreibne"
* @fragment:"ist am Anfang sehr gewöhungsbedürftig, bis man begriffen hat, wie die Interaktion zwischen HTML, CSS, und JavaScript abläuft"
* @fragment:"ist generell &quot;innen pfui, außen hui&quot;"
* @fragment:"macht des dem Benutzer sehr schwer, modularen Kode zu schreiben"

--

## @head:"Allgemeines zu JavaScript"
### @subhead:"Installation"

<span class="fragment">
JavaScript ist fester Bestandteil gängiger Webbrowser, wie [Firefox](:wiki:Mozilla_Firefox), [Chrome](:wiki:Google_Chrome), oder [Safari](:wiki:Apple_Safari). Im [Internet-Explorer](:wiki:Internet_Explorer) ist JavaScript angeblich auch vorinstalliert, jedoch laufe viele Apps sehr viel schlechter als gewünscht, weil Microsoft sich mal wieder qualitativ von den anderen Anbietern abgrenzen muss.
</span>

---

## @head:"Agenda 2015"

* @stroked:"Allgemeines zu JavaScript"
    - @stroked:"Herkunft"
    - @stroked:"Charakteristik"
    - @stroked:"Installation"
* @unstroke:"Bibliotheken und Entwickertools"
    - @unstroke:"Webbrowser"
    - @unstroke:"Bibliotheken"
    - @unstroke:"Entwicklertools"
* @unstroke:"Ein erstes Programmierbeispiel"
    - @unstroke:"HTML und CSS"
    - @unstroke:"Die Kölner Phonetik in JavaScript"
    - @unstroke:"Interaktives Beispiel"

---

## @head:"Bibliotheken und Entwicklertools"
### @subhead:"Webbrowser"

<span class="fragment">
Ich empfehle, beim Entwickeln von JavaScript-Applikationen grundsätzlich auf einen der gängigen Unix-Browser ([Firefox](:wiki:Mozilla_Firefox), [Chrome](:wiki:Google_Chrome), oder [Safari](:wiki:Apple_Safari)) zurückzugreifen. 
Firefox und Chrome, welche ich beide regelmäßig verwende, unterscheiden sich in den Funktionen, die sie bieten. Firefox erlaubt bestimmte Dateizugriffe, ohne die Applikation über einen Server laufen zu lassen, was die Entwicklung von Applikationen erleichtert. Chrome hat Vorteile im Layout und im Debugging. Grundsätzlich sollten alle Applikationen mindestens auf Firefox und Chrome getestet werden, da es hier mitunter zu bestimmten Unterschieden kommen kann. Auch unerwartete Fehler können in einem Webbrowser auftauchen, im anderen aber nicht.
</span>

--

## @head:"Bibliotheken und Entwicklertools"
### @subhead:"Bibliotheken"

**Empfohlene Frameworks:**

* <span class="fragment">[jQuery](http://jquery.com): eine der am weitesten verbreiteten JavaScript-Bibliotheken, die viele Erweiterungen und Erleichterungen bietet und als Grundlage zahlreicher Plugins dient. Aufgrund der Größe von jQuery sollte man sich jedoch für jedes Projekt überlegen, ob man die Bibliothek auch wirklich braucht, denn auch JavaScript allein bietet viele Möglichkeiten, kurzen und knackigen Kode zu schreiben.</span>
* <span class="fragment">[d3](http://d3js.org): Eine wunderbare Bibliothek zur Datenvisualisierung, ein bisschen gewöhnungsbedürftig in der Anwendung, aber unheimlich schön in den Ergebnissen. Entwickelt wurde die Bibliothek vorrangig von Mike Bostock, der für die New York Times arbeitet, die seine Pionierarbeit der interaktiven Visualisierung sponsort.</span>

--

## @head:"Bibliotheken und Entwicklertools"
### @subhead:"Entwicklertools"

<p class="fragment" style="font-size:75%">
Man kann JavaScript auch in der Konsole ausführen (die selbst in JavaScript geschrieben wurde): 
</p>

<iframe scrolling="no" style="width:880px;height:300px;overflow:hidden;margin-left:40px;" src="../demos/console.html"></iframe>

<span class="fragment" style="font-size:75%">
Zum Testen bietet sich [node.js](http://nodejs.org) an: Dieses Paket erlaubt es, JavaScript Kode in Skripten auszuführen und bietet auch eine interaktive Konsole. Der Vorteil von node.js ist, dass man Skripte testen kann, ohne den ansonsten erforderlichen HTML/CSS-Überbau zugrunde legen zu müssen.
</span>

---

## @head:"Agenda 2015"

* @stroked:"Allgemeines zu JavaScript"
    - @stroked:"Herkunft"
    - @stroked:"Charakteristik"
    - @stroked:"Installation"
* @stroked:"Bibliotheken und Entwickertools"
    - @stroked:"Webbrowser"
    - @stroked:"Bibliotheken"
    - @stroked:"Entwicklertools"
* @unstroke:"Ein erstes Programmierbeispiel"
    - @unstroke:"Die Kölner Phonetik in JavaScript"
    - @unstroke:"Ausführung im Terminal"
    - @unstroke:"Interaktives Beispiel"

---

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

<span class="fragment">
Es existiert natürlich bereits eine Implementierung der Kölner Phonetik für JavaScript, implementiert von J. Tillmann: [https://github.com/jtillmann/colophoneticjs](https://github.com/jtillmann/colophoneticjs). Diese Version wurde für die Zwecke unseres Seminars leicht umgeschrieben, so dass wir sie in ähnlicher Weise, wie die Python-Version der Kölner Phonetik verwenden können. Der resultierende Source Code, ein Skript mit Namen [kph.js](https://github.com/LinguList/pyjs-seminar/blob/master/website/code/kph.js) befindet sich auf der Projektwebseite und kann dort heruntergeladen werden. Er wurde ebenfalls bereits in die Terminal-Applikation integriert.
</span>

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

**Kölner Phonetik mit Hilfe des [Web-Terminals](../demos/console.html):**

<pre><code class="fragment js" data-trim>
js> kph.encode('Mayer');
67
</code></pre>

<span class="fragment">
<iframe scrolling="no" style="width:880px;height:200px;overflow:hidden;margin-left:40px;" src="../demos/console.html"></iframe>
</span>

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

**Kölner Phonetik mit node.js:**

<span class="fragment">Einbinden von kph.js:</span>

<pre class="fragment"><code class="js" data-trim>
> kph = require('./js/kph.js') /* Im Order demos/ */
{ encode: [Function] }
</code></pre>

<span class="fragment">Anwenden:</span>

<pre class="fragment"><code class="js" data-trim>
> kph.encode('Müller-Lüdenscheidt');
'65752682'
> kph.encode('Muller-Ludenscheidt Sebastian Bach')
65752682 81826 14
</code></pre>

--

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

Die Verwendung in der Konsole ist aber noch nicht alles! Viel interessanter wird es ja, wenn man den Kode gleich auf einer Webseite einsetzen kann, zum Beispiel als interaktive Applikation. 

Dafür brauchen wir zunächst eine HTML-Eingabe und Ausgabe, die wir in einer HTML-Seite (mit Standard-Head-Body Struktur) wie folgt unterbringen können:

<pre class="fragment"><code data-trim>
<input type="text" style="width:200px" id="ipt" />
<input type="button" onclick="showKPH();">OK</>
<output id="opt" />
</code></pre>

<span class="fragment">Die Ausgabe sieht dann auf der Webseite wie folgt aus:</span>

<div class="fragment">
<input type="text" style="width:200px" id="ipt"></input>
<button type="button" onclick="showKPH();">OK</button>
<div id="opt"></div>
</div>

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

Um eine bestimmte JavaScript-Bibliothek ausführen zu können, müssen wir sie im Header der HTML-Datei (oder an einer beliebigen anderen Stelle) einbinden, was wie folgt aussieht:

<pre class="fragment"><code data-trim class="html">
&lt;html>
  &lt;head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <script src="js/kph.js"></script>
  &lt;/head>
  &lt;body>
    <input type="text" style="width:300px" id="ipt"></input>
    <button type="button" onclick="showKPH();">GIB MIR DIE KPH!</button>
    <output id="opt"></output>
  &lt;/body>
&lt;/html>
</code></pre>

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

Dann brauchen wir noch eine JavaScript Funktion, die mit HTML kommuniziert:
<pre class="fragment"><code class="js" data-trim>
// Funktion greift auf die HTML-Datei zu und Berechnet
// die Werte für die Kölner Phonetik
function showKPH() {
  /\* get the input button element \*/
  var ipt = document.getElementById('ipt');
  /\* get the input value \*/
  var ipt_val = ipt.value;
  /\* convert to Kölner Phonetik \*/
  var converted_values = kph.encode(ipt_val);
  /\* write to html page \*/
  var opt = document.getElementById('opt');
  opt.innerHTML = converted_values;
}
</code></pre>

<span class="fragment" style="font-size:75%;line-height:15px;">Beachten Sie, dass es zwei Arten in JS gibt, um Kommentare einzufügen, den Doppelslash (//), der den Rest einer Zeile auskommentiert, und die Kombination von Slash mit Asterisk (/\* und \*/), mit denen man auch über Zeilen hinaus auskommentieren kann. </span>

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

Diese Datei können wir entweder als separates Skript abspeichern und in HTML einbinden,

<pre class="fragment"><code class="html" data-trim>
&lt;html>
  ...
    <output id="opt"></output>
    <script src="communication.js"></script>
  &lt;/body>
</code></pre>
 
<p class="fragment">
oder wir können sie direkt zwischen die Skript-Tags schreiben</p>

<pre class="fragment"><code class="js html" data-trim>
&lt;html>
  ...
    <output id="opt"></output>
    <script>
function showKPH() {
  var ipt = document.getElementById('ipt');
  var ipt_val = ipt.value;
  var converted_values = kph.encode(ipt_val);
  var opt = document.getElementById('opt');
  opt.innerHTML = converted_values;
}
    </script>
  &lt;/body>
</code></pre>

--

@data-transition:none

## @head:"Ein erstes Programmierbeispiel"
### @subhead:"Die Kölner Phonetik in JavaScript"

Und so sieht das Ganze dann in Aktion aus:

<iframe scrolling="no" style="width:880px;height:200px;overflow:hidden;margin-left:40px;" src="../demos/kph-demo.html"></iframe>

---

## @head:"Agenda 2015"

* @stroked:"Allgemeines zu JavaScript"
    - @stroked:"Herkunft"
    - @stroked:"Charakteristik"
    - @stroked:"Installation"
* @stroked:"Bibliotheken und Entwickertools"
    - @stroked:"Webbrowser"
    - @stroked:"Bibliotheken"
    - @stroked:"Entwicklertools"
* @stroked:"Ein erstes Programmierbeispiel"
    - @stroked:"Die Kölner Phonetik in JavaScript"
    - @stroked:"Ausführung im Terminal"
    - @stroked:"Interaktives Beispiel"

---


@data-background:#000000

<p style="font-size:200px;color:white;font-weight:bold;">
062
</p>
<p style="font-size:80%;color:white;font-weight:bold;text-align:right;">
der dritten Sitzung
</p>
<p><code style="font-size:160px">:wq!</code></p>



