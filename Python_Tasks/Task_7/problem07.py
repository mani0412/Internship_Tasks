# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    # your code goes here
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        middle = alphabet[size - i - 1:size]
        row = list(left + middle)
        row = "-".join(row)
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
