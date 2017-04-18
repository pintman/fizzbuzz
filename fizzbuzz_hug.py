import hug

def fizzbuzz_results(n):
    results = {}
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            results[i] = "fizzbuzz"
        elif i % 3 == 0:
            results[i] = "fizz"
        elif i % 5 == 0:
            results[i] = "buzz"
        else:
            results[i] = i

    return results

@hug.get('/fizzbuzz') # respond to get-requests
def fizzbuzz_get(max_number):
    """Return fizz up to the given number."""
    n = int(max_number)
    return fizzbuzz_results(n)
