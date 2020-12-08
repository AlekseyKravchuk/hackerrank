""" https://www.hackerrank.com/challenges/python-string-formatting/problem """


def print_formatted(n):
    width = len(f'{n:b}')

    types = {'d': 'decimal',
             'o': 'octal',
             'X': 'hexadecimal',
             'b': 'binary'}
    for i in range(1, n + 1, 1):
        for _type in types:
            print(f'{i: >{width}{_type}}', end=' ')
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
