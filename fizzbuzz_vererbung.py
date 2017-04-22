class Game:
    def start_game_loop(self):
        """Starting the gameloop of the game."""
        self.setup()
        while True:
            self.handle_input()
            self.update()
            self.draw()

    def setup():
        """Will be invoked once at the beginning of a game."""
        pass

    def handle_input():
        """Evaluate inputs of the player."""
        pass
    
    def update():
        """Updating all game objects and game values."""
        pass

    def draw():
        """Draw the game world."""
        pass

class FizzBuzzGame(Game): # Subclass(Superclass)
    def __init__(self):
        self.n = 1
        self.answer_correct = False
        self.playerinput = ""

    def setup(self):
        print("Spiel gestartet")

    def handle_input(self):
        self.playerinput = input(str(self.n) + " ? ")

    def update(self):
        # Evaluating player input
        soll = self._fizzbuzz(self.n)
        self.answer_correct = self.playerinput == str(soll)        
        if self.answer_correct:
            self.n += 1

        # Checking winning condition
        if self.n == 6:
            print("Gewonnen!")
            exit()

    def draw(self):
        if self.answer_correct:
            print("Richtig :)")
        else:
            print("Leider Falsch. Probiere es erneut.")
      
    def _fizzbuzz(self, i):
        if i % 3 == 0 and i % 5 == 0:
            return "fizzbuzz"
        elif i % 3 == 0:
            return "fizz"
        elif i % 5 == 0:
            return "buzz"
        else:
            return i

          
fbs = FizzBuzzGame()
fbs.start_game_loop()
