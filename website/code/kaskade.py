# Zunächst definieren wir das Jongliermuster, welches später die einzelnen
# Jonglageschritte darstellen soll. Dabei "malem" wir mit Hilfe von Buchstaben
# und Sonderzeichen ein Feld, indem auf einfache Art und Weise die vier
# entscheidenden Punkte für die Jonglage abgebildet sind, an denen sich die
# Bälle zum Zeitpunkt unserer Snapshots aufhalten könne:
# - RechtsOben (R)
# - LinksOben (L)
# - RechteHand (r)
# - LinkeHand (l)
# Damit wir am Ende auf dem Terminal immer nur ein Bild und nicht mehrere in
# Reihe sehen, fügen wir ganz einfach ganz viele Newline-Zeichen vor dem
# eigentlichen Bild ein (das ist eine sehr dreckige Lösung für so ein Problem).

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

# Nun deklarieren wir die Gegenstände, die jongliert werden sollen. Dies sind
# einfache Strings aus Zahlen, damit man die unterschiedlichen Gegenstände
# besser verfolgen kann.
gegenstand1 = '(1)'
gegenstand2 = '(2)'
gegenstand3 = '(3)'

# Jetzt deklarieren wir die vier Punkte, an denen sich die drei Bälle jeweils
# aufhalten können. Wir tun so, als wäre ein Ball schon in der Luft, um uns das
# Problem des Startens zu ersparen. LinksOben ist zu Beginn leer, weshalb wir
# für LinksOben ein dreifaches Leerzeichen schreiben, da die Bälle ja auch
# immer drei Zeichen groß sind.
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
    
    # Wir deklarieren die Variable SnapShot, welche zu Beginn jeder
    # Schleifenoperation mit Hilfe von print dargestellt wird. Snapshot ist
    # zunächst der gleiche string wie JonglierMuster, aber dieser wird nun
    # verändert, entsprechend der Lage der Bälle an den entsprechenden
    # Positionen. Zum verändern nehmen wir einfache Ersetzungsbefehle, die die
    # Ausgangsstrings durch die von den Variablen belegten strings ersetzen. 
    SnapShot = JonglierMuster
    SnapShot = SnapShot.replace('(R)',RechtsOben)
    SnapShot = SnapShot.replace('(L)',LinksOben)
    SnapShot = SnapShot.replace('(l)',LinkeHand)
    SnapShot = SnapShot.replace('(r)',RechteHand)
    # Wir benutzen nicht print, um das ganze auszugeben, sondern input,
    # weil damit immer gleichzeitig auch eine Pause verbunden ist (erst wenn
    # man Enter drückt geht es weiter).
    input(SnapShot)

    # Jetzt werden die Variablen "jongliert". Das Grundprinzip besteht darin,
    # dass von den vier Orten, an denen sich ein Ball aufhalten kann, immer
    # genau der gefüllt wird, der gerade leer ist. Der füllende Ort ist dabei
    # durch die Kaskadenform festgelegt. Die Reihenfolge ist:
    # LinkeHand => RechtsOben => RechteHand => LinksOben => LinkeHand
    # Das Jonglieren der Bälle wird durch einfaches Übergeben von Werten durch
    # fortlaufende Variablenzuweisung erreicht: Entsprechend der Reihenfolge
    # wird der nichtleere Wert an den leeren Wert übergeben und dieser wiederum
    # geleert.
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



