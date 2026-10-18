# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    commands = int(input())

    for _ in range(commands):
        operation = input().split()

        if operation[0] == 'pop':
            s.pop()
        elif operation[0] == 'remove':
            s.remove(int(operation[1]))
        elif operation[0] == 'discard':
            s.discard(int(operation[1]))

    print(sum(s))
