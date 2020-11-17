""" https://www.hackerrank.com/challenges/py-collections-deque/problem """

from collections import deque
import sys


def main():
    q = deque()
    for i in range(int(input())):
        line = [x for x in input().split()]
        if len(line) == 2:
            exec(f'q.{line[0]}({line[1]})')
        elif len(line) == 1:
            exec(f'q.{line[0]}()')
        else:
            sys.exit('Wrong number of arguments')
    for elm in q:
        print(elm, end=' ')


if __name__ == '__main__':
    main()
