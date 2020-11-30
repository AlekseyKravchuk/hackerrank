""" https://www.hackerrank.com/challenges/most-commons/problem """

from collections import Counter


def main():
    cnt_lst = Counter(input()).most_common()
    cnt_lst.sort(key=lambda x: (-x[1], x[0]))
    for elm in cnt_lst[:3]:
        print(*elm)


if __name__ == '__main__':
    main()
