""" https://www.hackerrank.com/challenges/word-order/problem """

from collections import Counter, OrderedDict


def main():
    # words_cntr = OrderedDict(Counter([input() for i in range(int(input()))]))
    # print(len(words_cntr))
    # for count in words_cntr.values():
    #     print(count, end=' ')
    # print()

    words = Counter([input() for i in range(int(input()))])
    print(len(words))
    for key in words:
        print(words[key], end=' ')
    print()


if __name__ == '__main__':
    main()
