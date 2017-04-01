# Kata 0 - auf Papier
"""
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

def fizzbuzz():
    for i in range(20):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

#fizzbuzz()

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
        #th.start()
        while th.isAlive():
            pass

#fizzbuzz_thrading()

# Kata 4 - mit einer anderen IDE

# Kata 5 - in einer anderen Programmiersprache

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
            #print("sending", i)
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

class App:
    def __init__(self):
        self.i = 0
        root = tkinter.Tk()
        btn = tkinter.Button(root, text="next", command=self.button_click)
        btn.pack()
        self.ent = tkinter.Entry(root)
        self.ent.pack()
        root.mainloop()

    def button_click(self):
        i = self.i
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

#App()



# Kata 8 - Objekt-Orientiert
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

class Numbering:
    def printit(self, i):
        print(i)

class Buzzer2(Numbering):
    def printit(self, i):
        if i & 5 == 0:
            print("buzz")
        else:
            super().printit(i)

class Fizzer2(Buzzer2):
    def printit(self, i):
        if i % 3 == 0:
            print("fizz")
        else:
            super().printit(i)

class FizzerBuzzer2(Fizzer2):
    def printit(self, i):
        if i % 3 == 0 and  i % 5 == 0:
            print("fizzbuzz")
        else:
            super().printit(i)

def fizzbuzz_objektorientiert2():
    for i in range(20):
        fb = FizzerBuzzer2()
        fb.printit(i)

#fizzbuzz_objektorientiert2()

# Kata 10 - funktional
import functools

def by(number):
    """Return a function to prove divisibility by number."""
    return (lambda i: i % number == 0)
def fizzbuzz_func(i):
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

    return bottle.template("""
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
    """, max=number, res=res)

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
"""

# Kata 13 - als installierbares Programm
# s. setup.py

# Kata 14 - als getestetes Programm

import unittest

class FizzBuzzClass:
    def fizzbuzz(self, i):
        """Die ist ein Kommentar,der einen Test enthält:

        Kommentare von Methoden lassen sich auch testen. Der folgende
        Quelltext wird hierfür ausgeführt, sobald das doctext-Modul aufgerufen
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

    Hierfür testet die Klasse mögliche Eingaben und Ausgaben."""

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
    import eamodul.hw
except:
    pass

class FizzBuzzEAModul:
    def __init__(self):
        self.i = 0

        eam = eamodul.hw.EAModul()
        # switching on green only
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
