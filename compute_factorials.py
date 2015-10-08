import sys
from tasks import compute_factorial


def compute_from_files(filenames):
    numbers = []
    for filename in filenames:
        with open(filename) as f:
            numbers.append(int(f.readline().rstrip('\n')))
    results = [compute_factorial(n) for n in numbers]

    return dict(zip(numbers, results))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compute_factorials.py filename1, filename2, ... ")
        sys.exit()
    filenames = sys.argv[1:]
    results = compute_from_files(filenames)

    fact_sum = 0
    for number, factorial in results.items():
        print("{}! = {}".format(number, factorial))
        fact_sum += factorial
    print("Sum of factorials = ", fact_sum)
