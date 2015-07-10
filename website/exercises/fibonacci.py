# author: Johann-Mattis List
# date: 12.05.2011
# file: fibonacci.py



def fibonacci(number):
    """
    Dies ist die klassische Lösung, die sich fast überall im Internet finden
    lässt. Dummerweise habe ich vergessen, die Quelle zu dokumentieren und bin
    jetzt zu faul, das zu tun.
    """
    # Dies ist die Bedingung für das Terminieren der Funktion. Wenn der Wert 1
    # oder der Wert 0 eingegeben wird, wird der gleiche Wert zurückgegeben und
    # die Rekursion gestoppt.
    if number == 0 or number == 1:
        return number
    # Dies ist die Rekursion. Da die Fibonaccizahlen immer aus den zwei
    # Vorgängerzahlen errechnet werden, welche wiederum aus ihren zwei
    # vorgängerzahlen errechnet werden, muss die Funktion zwei mal aufgerufen
    # werden.
    else:
        return fibonacci(number-1) + fibonacci(number-2)

