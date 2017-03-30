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

# Kata 1

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

# Kata 2 - ohne Schleife (rekursiv)

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

# Kata 3 - Nebenläufig
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

# Kata 7 - mit GUI
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
        # TODO löschen
        
        if i % 3 == 0 and i % 5 == 0:
            self.ent.insert(0, "fizzbuzz")
        elif i % 3 == 0:
            self.ent.insert(0, "fizz")
        elif i % 5 == 0:
            self.ent.insert(0, "buzz")
        else:
            self.ent.insert(0, i)
        
App()



# Kata 8 - Objekt-Orientiert.
class Fizz:
    def __init__(self, n):     
        pass
    def print(self):
        print("Fizz")

class Buzz:
    def __init__(self, n):
        pass
    def print(self):
        print("Buzz")

class FizzBuzz:
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
            self.printer = FizzBuzz(i)
        elif i % 3 == 0:
            self.printer = Fizz(i)
        elif i % 5 == 0:
            self.printer = Buzz(i)
        else:
            self.printer = Number(i)
        
    def print(self):
        self.printer.print()
    

for i in range(20):
    f = FizzBuzzNumber(i)
    #f.print()
    
