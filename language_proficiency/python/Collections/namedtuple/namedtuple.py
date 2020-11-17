""" https://www.hackerrank.com/challenges/py-collections-namedtuple/problem """

from collections import namedtuple


def main():
    n = int(input())
    sum = 0
    Columns = namedtuple('Columns', input().strip().split())

    for i in range(n):
        line = input().strip().split()
        entry = Columns(*line)
        sum += int(entry.MARKS)
    print(f'{float(sum) / n: .2f}')


def main_improved():
    n = int(input())  # the total number of students
    Header = namedtuple('Header', input().split())
    print(f'{sum([float(Header(*input().split()).MARKS) for i in range(n)]) / n: .2f}')


if __name__ == '__main__':
    main()
