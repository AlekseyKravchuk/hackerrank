""" https://www.hackerrank.com/challenges/word-order/problem """
from collections import defaultdict


def main():
    words = defaultdict(lambda: [])
    for i in range(int(input())):
        words[input()].append(i + 1)

    print(len(words))
    for key in words:
        print(len(words[key]), end=' ')
    print()


if __name__ == '__main__':
    main()
