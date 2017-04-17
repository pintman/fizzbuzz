import argparse

def fizzbuzz(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    
if __name__ == "__main__":
    # Using class ArgumentParser to help handling parameters
    parser = argparse.ArgumentParser(description="FizzBuzz Spiel")
    parser.add_argument("--max_wert", type=int, default=20,
                        help="Bis zu diesem Wert wird gezählt")
    args = parser.parse_args()
    fizzbuzz(args.max_wert)
    
