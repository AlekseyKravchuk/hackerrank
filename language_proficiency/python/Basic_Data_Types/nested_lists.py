""" https://www.hackerrank.com/challenges/nested-list/problem """

import sys


def get_first_second_scored_item_idx(lst: list) -> int:
    for i in range(len(lst) - 1):
        if lst[i][1] == lst[i+1][1]:
            continue
        return i+1
    raise Exception('You have typed wrong values: there are will always be one or more students having the second lowest grade!')


def main():
    entries = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        entries.append([name, score])

    entries.sort(key=lambda x: (x[1], x[0]))  # sort items in entries first by SCORE, than by NAME, both in ASC order

    try:
        first_second_scored_item_idx = get_first_second_scored_item_idx(entries)
    except Exception as e:
        print(e)
        sys.exit(-1)

    names = [entries[first_second_scored_item_idx][0]]
    for i in range(first_second_scored_item_idx, len(entries) - 1):
        if entries[i][1] == entries[i + 1][1]:
            names.append(entries[i + 1][0])
        else:
            break
    for name in names:
        print(name)


if __name__ == '__main__':
    main()
