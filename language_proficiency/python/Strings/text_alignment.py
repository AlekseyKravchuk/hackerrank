""" https://www.hackerrank.com/challenges/text-alignment/problem """

from math import ceil


def print_logo(w):
    for i in range(w):
        print(('H' * (2 * i + 1)).center(2 * w - 1, ' '))

    col = ('H' * w).center(2 * w - 1)
    spaces = ' ' * (3 * w - (w - 1))

    for j in range(w + 1):
        print(col + spaces + col)

    offset = ' ' * int((w - 1) / 2)
    for k in range(ceil(w/2)):
        print(offset + 'H' * (5 * w))

    for j in range(w + 1):
        print(col + spaces + col)

    for i in range(w):
        print(('H' * (2*w - 1 - 2*i)).rjust(6*w - (i+1), ' '))


if __name__ == '__main__':
    print_logo(int(input()))
