"""Bei FizzBuzz handelt es sich um ein Zählspiel, bei dem die Zahlen bis 100
aufgezählt werden. Ist die Zahl durch 3 teilbar, wird "fizz" gesagt. Ist sie
durch 5 teilbar, wird "buzz" gesagt. Ist sie durch 3 und 5 teilbar, wird
"fizzbuzz" gesagt. Ansonsten wird die Zahl selbst gesagt.

Wir versuchen uns auf dem Blatt mit einer Aufwärmübung (Kata).

# Kata 0 - auf Papier
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19

"""


# Kata 1 - mit einer Methode

def fizzbuzz_methode(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

def fizzbuzz_methode2(n):
    for i in range(n):
        if i % 3 == 0:
            s = "fizz"
        if i % 5 == 0:
            s += "buzz"
        if len(s) == 0:
            s = i
        print(s)

#fizzbuzz_methode(20)
#fizzbuzz_methode2(20)


# Kata 2 - ohne Verwendung einer Schleife (rekursiv)

def fizzbuzz_rekursiv(i):
    if i == 0:
        return
    else:
        fizzbuzz_rekursiv(i-1)

        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


#fizzbuzz_rekursiv(20)


# Kata 3 - mit Hilfe von nebenläufigen Threads
import threading

def fizzbuzz_thread(i):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

def fizzbuzz_threading():
    for i in range(20):
        th = threading.Thread(target=fizzbuzz_thread, args=(i,))
        th.start()
        # Wait for thread to finish
        while th.isAlive():
            pass

#fizzbuzz_threading()


# Kata 4 - mit einer anderen IDE
"""
Mögliche Kandiaten wären:

- IDLE
- PyCharm
- Emacs
- vim
- Atom

"""


# Kata 5 - in einer anderen Programmiersprache
"""
Mögliche Sprachen wären:

- Java
- Javascript
- C#
- C
- C++
- Bash

"""


# Kata 6 - als Client-Server Anwendung
import socketserver
import socket

class FizzBuzzHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # received bytes from request and take the first one
        i = self.request.recv(1)[0]
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

class FizzBuzzClient:
    def __init__(self, ip, port):
        self.socket = (ip, port)

    def send(self, i):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.socket)
            sock.sendall(bytes([i]))

def fizzbuzz_client_server():
    # Starting the server in a separate thread
    server_socket = ("127.0.0.1", 8081)
    server = socketserver.TCPServer(server_socket, FizzBuzzHandler)
    th = threading.Thread(target=server.serve_forever)
    th.start()
    # starting the client
    cl = FizzBuzzClient(*server_socket)
    for i in range(20):
        cl.send(i)

#fizzbuzz_client_server()


# Kata 7 - mit einer grafischen Oberfläche (GUI)
import tkinter

class GUI:
    def __init__(self):
        self.i = 0

        root = tkinter.Tk()
        btn = tkinter.Button(root, text="next", command=self.button_click)
        btn.pack()
        self.ent = tkinter.Entry(root)
        self.ent.pack()
        # entering main event loop
        root.mainloop()

    def button_click(self):
        i = self.i
        # clear the entry field
        self.ent.delete(0, tkinter.END)

        if i % 3 == 0 and i % 5 == 0:
            self.ent.insert(0, "fizzbuzz")
        elif i % 3 == 0:
            self.ent.insert(0, "fizz")
        elif i % 5 == 0:
            self.ent.insert(0, "buzz")
        else:
            self.ent.insert(0, i)

        self.i += 1

def fizzbuzz_gui():
    GUI()


#fizzbuzz_gui()


# Kata 8 - Objekt-Orientiert: Klassen und Objekte verwenden
class Fizzer:
    def __init__(self, n):
        pass
    def print(self):
        print("Fizz")

class Buzzer:
    def __init__(self, n):
        pass
    def print(self):
        print("Buzz")

class FizzBuzzer:
    def __init__(self, n):
        pass
    def print(self):
        print("FizzBuzz")

class Number:
    def __init__(self, n):
        self.n = n
    def print(self):
        print(self.n)

class FizzBuzzNumber:
    def __init__(self, i):
        if i % 3 == 0 and i % 5 == 0:
            self.printer = FizzBuzzer(i)
        elif i % 3 == 0:
            self.printer = Fizzer(i)
        elif i % 5 == 0:
            self.printer = Buzzer(i)
        else:
            self.printer = Number(i)

    def print(self):
        self.printer.print()

def fizzbuzz_objektorientiert():
    for i in range(20):
        f = FizzBuzzNumber(i)
        f.print()

#fizzbuzz_objektorientiert()


# Kata 9 - objekt-orientiert mit Vererbung
class Numberer:
    def printit(self, i):
        print(i)

class BuzzingNumberer(Numberer):
    def printit(self, i):
        if i % 5 == 0:
            print("buzz")
        else:
            super().printit(i)

class FizzingBuzzingNumberer(BuzzingNumberer):
    def printit(self, i):
        if i % 3 == 0:
            print("fizz")
        else:
            super().printit(i)

class FizzBuzzingFizzingBuzzingNumberer(FizzingBuzzingNumberer):
    def printit(self, i):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:
            super().printit(i)

def fizzbuzz_objektorientiert2():
    for i in range(20):
        fb = FizzBuzzingFizzingBuzzingNumberer()
        fb.printit(i)

#fizzbuzz_objektorientiert2()


# Kata 10 - funktional mit map, reduce und lambda-Ausdrücken
import functools

def by(number):
    """Return a function to prove divisibility by number."""
    return (lambda i: i % number == 0)

def fizzbuzz_func(i):
    # create two functions to test for divisibility
    by5 = by(5)
    by3 = by(3)

    if by5(i) and by3(i):
        return "fizzbuzz"
    elif by3(i):
        return "fizz"
    elif by5(i):
        return "buzz"
    else:
        return i

def fizzbuzz_funktional():
    # apply fizzbuzz_func to numbers
    res = map(fizzbuzz_func, range(20))

    # reduce the result into a string
    s = functools.reduce(
        lambda acc, i: acc + str(i) + "\n", # updating function
        res, # values to be reduced
        "") # initial value

    print(s)

#fizzbuzz_funktional()


# Kata 11 - als Webanwendung (mit bottle)
import bottle

@bottle.route("/fizzbuzz/<number:int>")
def fizzbuzz_web_route(number):    
    res = []
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            res.append("fizzbuzz")
        elif i % 3 == 0:
            res.append("fizz")
        elif i % 5 == 0:
            res.append("buzz")
        else:
            res.append(i)

    html = """
        <!DOCTYPE html>
        <html>
          <body>
            <h1>FizzBuzz Numbers up to {{max}}</h1>
            <table>
            % for r in res:
              <tr><td> {{r}} </td></tr>
            %end
            </table>
          </body>
        </html>
        """

    return bottle.template(html, max=number, res=res)

def fizzbuzz_web():
    bottle.run(host="127.0.0.1", port=8081)

#fizzbuzz_web()


# Kata 12 - in git-repo einchecken
"""
$ cd fizzbuzz

# Repo initialisieren
$ git init

# Dateien für commit vormerken
$ git add fizzbuzz.py

# Dateien in Repo einchecken
$ git commit -a

# Logfile anschauen
$ git log
"""


# Kata 13 - als installierbares Programm
# s. setup.py


# Kata 14 - als getestetes Programm (mit unittest und doctests)
import unittest

class FizzBuzzClass:
    def fizzbuzz(self, i):
        """Die ist ein Kommentar,der einen Test enthält. Unter Python nennt man dies
        einen doctest.

        Kommentare von Methoden lassen sich auch testen. Der folgende
        Quelltext wird hierfür ausgeführt, sobald das doctest-Modul aufgerufen
        wird:

        $ python3 -m doctest fizzbuzz.py

        Hier kommt der Test:

        >>> fbc = FizzBuzzClass()
        >>> fbc.fizzbuzz(3)
        'fizz'
        >>> fbc.fizzbuzz(5)
        'buzz'
        >>> fbc.fizzbuzz(10)
        'buzz'
        >>> fbc.fizzbuzz(11)
        11

        """
        if i % 3 == 0 and i % 5 == 0:
            return "fizzbuzz"
        elif i % 3 == 0:
            return "fizz"
        elif i % 5 == 0:
            return "buzz"
        else:
            return i

class FizzBuzzClassTest(unittest.TestCase):
    """Diese Unit-Test-Klasse testet die Klasse FizzBuzzClass. 

    Hierfür testet sie mögliche Eingaben und Ausgaben."""

    def test_fizzbuzz(self):
        fb = FizzBuzzClass()

        self.assertEqual(fb.fizzbuzz(3), "fizz")
        self.assertEqual(fb.fizzbuzz(15), "fizzbuzz")
        self.assertEqual(fb.fizzbuzz(9), "fizz")
        self.assertEqual(fb.fizzbuzz(10), "buzz")


def fizzbuzz_getestet():
    # Alle Tests ausführen.
    unittest.main()

#fizzbuzz_getestet()


# Kata 15 - mit einem EA-Modul ansteuern
# https://github.com/pintman/ea_rpi_modul
try:
    # Um die Bibliothek zu installieren: pip install eapi
    import eamodul.hw 
except:
    pass

class FizzBuzzEAModul:
    def __init__(self):
        self.i = 0

        eam = eamodul.hw.EAModul()
        # switching on green LED only
        eam.schalte_leds(False, False, True)
        # register for events when button0 pressed
        eam.taster_event_registrieren(0, self.taster0_gedrueckt)

        # wait for taster event
        while True:
            pass

    def taster0_gedrueckt(self, pin):
        if self.i % 3 == 0 and self.i % 5 == 0:
            print("fizzbuzz")
        elif self.i % 3 == 0:
            print("fizz")
        elif self.i % 5 == 0:
            print("buzz")
        else:
            print(self.i)

        self.i += 1

def fizzbuzz_eamodul():
    FizzBuzzEAModul()


#fizzbuzz_eamodul()


# Kata 16 - mit Anbindung an eine Datenbank
import sqlite3

def fizzbuzz_insert_into_db():
    conn = sqlite3.connect("fizzbuzz.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS fizzbuzz(nr int, ergebnis text)")

    for i in range(20):
        erg = ""
        if i % 3 == 0 and i % 5 == 0:
            erg = "fizzbuzz"
        elif i % 3 == 0:
            erg = "fizz"
        elif i % 5 == 0:
            erg = "buzz"
        else:
            erg = i

        c.execute("INSERT INTO fizzbuzz VALUES(?,?)", (i,erg))

    conn.commit()
    conn.close()

def fizzbuzz_select_from_db():
    conn = sqlite3.connect("fizzbuzz.db")
    c = conn.cursor()
    rows = c.execute("SELECT nr, ergebnis FROM fizzbuzz")

    print("Nr.\tErgebnis")
    for i,erg in rows:
        print(i, "\t", erg)

    conn.close()

def fizzbuzz_db():
    fizzbuzz_insert_into_db()
    fizzbuzz_select_from_db()
    

#fizzbuzz_db()


# Kata 17 - mit docstring Dokumentation

def fizzbuzz_dokumentiert(n):
    """Diese Methode durchläuft die Zahlen 1 bis n. Sie gibt 'fizz' aus,
    wenn die Zahl durch 3 ist, 'buzz', wenn sie durch 5 teilbar ist
    und 'fizzbuzz', wenn sie durch 3 und 5 teilbar ist."""

    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# Der Kommentar einer Methode oder Klasse steht immer als erster
# String in der Deklaration.
#
# Er kann im Python-Interpreter mit help() abgerufen werden:
#
# >>> help(fizzbuzz_dokumentiert)
#
# Außerdem gibt es das Modul pydoc, mit dem eine Dokumentation auf der
# Kommandozeile oder über einen Webserver zur Verfügung steht.
#
# $ pydoc fizzbuzz.fizzbuzz_dokumentiert
# $ python -m pydoc fizzbuzz.fizzbuzz_dokumentiert
#
# Webserver starten auf Port 8080 mit Dokumentation unter
# http://localhost:8080
#
# $ pydoc -p 8080
# $ python -m pydoc -p 8080


# Kata 18 - als Chatbot (z.B. mit sopel https://sopel.chat/)
# und https://github.com/sopel-irc/sopel/wiki

"""
Installation: 
$ sudo pip3 install sopel

Konfiguration (in ~/.sopel) erstellen: 
$ sopel

Eigenen Bot in ~/.sopel/modules/fizzbuzz.py erstellen

Sopel starten
$ sopel
"""

from sopel import module

@module.commands('fizzbuzz')
def echo(bot, trigger):
    # to everybody:   bot.say("...")
    # to querstioner: bot.reply("...")

    # take and convert argument
    i = int(trigger.group(2))

    if i % 3 == 0 and i % 5 == 0:
        bot.reply("fizzbuzz")
    elif i % 3 == 0:
        bot.reply("fizz")
    elif i % 5 == 0:
        bot.reply("buzz")
    else:
        bot.reply(i)
           
"""
Eine mögliche Chat-Konversation (Sopel-Befehle beginnen mit einem
Punkt):

* FizzBuzzBot has joined
<fizzbuzz_owner> .fizzbuzz 1
<FizzBuzzBot>    fizzbuzz_owner: 1
<fizzbuzz_owner> .fizzbuzz 2
<FizzBuzzBot>    fizzbuzz_owner: 2
<fizzbuzz_owner> .fizzbuzz 3
<FizzBuzzBot>    fizzbuzz_owner: fizz
<fizzbuzz_owner> .fizzbuzz 5
<FizzBuzzBot>    fizzbuzz_owner: buzz
<fizzbuzz_owner> .fizzbuzz 14
<FizzBuzzBot>    fizzbuzz_owner: 14
<fizzbuzz_owner> .fizzbuzz 15
<FizzBuzzBot>    fizzbuzz_owner: fizzbuzz

"""


# Kata 19 - auf einem Cluster (mit GNU parallel)

"""Hierfür bedienen wir uns des Programmes GNU parallel.

Zuerst muss das Programm 'fizzbuzz.py' auf jeden Rechner übertragen
werden und der ssh-login gemäß der Beschreibung in 'man parallel'
eingerichtet worden sein. Dies wird im Abschnitt "EXAMPLE: Using
remote computers" der man-page beschrieben.

Nun folgt der Aufruf:

$ seq 20 | parallel --sshlogin server1,server2,server3 python3 fizzbuzz.py

seq 20 generiert die Zahlen 1 bis 20 und sendet sie über eine Pipe (|)
an den Befehl 'parallel'. Dieser verteilt die Aufrufe

 'python3 fizzbuzz.py 1',
 'python3 fizzbuzz.py 2',
 'python3 fizzbuzz.py 3',
 'python3 fizzbuzz.py 4', ...

auf die Server server1, server2 und server3.

"""

def fizzbuzz_cluster():
    import sys
    i = int (sys.argv[1])

    if i % 3 == 0 and i % 5 == 0:
        print(i, "fizzbuzz")
    elif i % 3 == 0:
        print(i, "fizz")
    elif i % 5 == 0:
        print(i, "buzz")
    else:
        print(i, i)

#fizzbuzz_cluster()
