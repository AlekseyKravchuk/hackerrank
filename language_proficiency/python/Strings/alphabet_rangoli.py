""" https://www.hackerrank.com/challenges/alphabet-rangoli/problem """

import string
from collections import deque


def print_rangoli(n):
    assert n < 27
    letters = list(string.ascii_lowercase)[:n]
    bottom = []
    for i in range(1, n+1):
        pad = '-' * (2*n - 2*i)
        center = deque(letters[n-i])
        for k in range(i-1, 0, -1):
            center.appendleft(letters[n-k])
            center.append(letters[n-k])
        s = pad + '-'.join(center) + pad
        print(s)
        if i != n:
            bottom.append(s)
    for line in bottom[::-1]:
        print(line)


def main():
    n = int(input())
    print_rangoli(n)


if __name__ == '__main__':
    main()
