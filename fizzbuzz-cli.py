import sys

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
    print("Evaluating command line:", sys.argv)

    num_arg = sys.argv[1]
    number = int(num_arg)

    fizzbuzz(number)
