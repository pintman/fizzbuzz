import sys
import os

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n

# determine parameter for fizzbuzz: environment variable, commandline,
# or default value.
if "FIZZBUZZ" in os.environ:
    print("[using environment variable as parameter]")
    n = os.environ["FIZZBUZZ"]
    n = int(n)    
elif len(sys.argv) > 1:
    print("[using command line parameter]")
    n = int(sys.argv[1])
else:
    print("[using default value as parameter]")
    n = 20   

for i in range(n):
    print(fizzbuzz(i))
