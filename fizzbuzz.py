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
    
for i in range(20):
    th = threading.Thread(target=fizzbuzz_thread, args=(i,))
    #th.start()
    while th.isAlive():
        pass
    

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

fizzbuzz_objektorientiert2()
