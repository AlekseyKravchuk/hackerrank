""" https://www.hackerrank.com/challenges/defaultdict-tutorial/problem """

from collections import defaultdict
import pathlib


def main_using_files():
    current_path = str(pathlib.Path(__file__).parent.absolute())
    testcase_file = current_path + '/' + 'failed_testcase.txt'
    my_out_file = current_path + '/' + 'my_output.txt'

    with open(testcase_file, 'r') as f:
        n, m = f.readline().strip('\n').split()

        A_words = [f.readline().strip('\n') for _ in range(int(n))]
        B_words = [f.readline().strip('\n') for _ in range(int(m))]
        set_A = set(A_words)
        set_B = set(B_words)
        set_B_minus_A = set_B - set_A  # strings that exist in B, but don't exist in A (for those: -1)

    d = defaultdict(list)
    checked_strings_from_B = set()

    for b_word in B_words:
        if b_word not in checked_strings_from_B:
            if b_word in set_B_minus_A:
                d[b_word].append('-1')
                checked_strings_from_B.add(b_word)
                continue
            for idx, a_word in enumerate(A_words):
                if b_word == a_word:
                    d[b_word].append(idx + 1)
                    checked_strings_from_B.add(b_word)
        else:  # if we come to duplicate string in B
            continue

    with open(my_out_file, 'w') as f:
        for key in B_words:
            print(' '.join([str(x) for x in d[key]]), file=f)


def main():
    d = defaultdict(list)
    checked_strings_from_B = set()  # storage for strings that already have been handled

    n, m = input().split()

    A_words = [input() for _ in range(int(n))]
    B_words = [input() for _ in range(int(m))]

    set_A = set(A_words)
    set_B = set(B_words)
    set_B_minus_A = set_B - set_A  # strings that exist in B, but don't exist in A (for those: append -1)

    for b_word in B_words:
        if b_word not in checked_strings_from_B:
            if b_word in set_B_minus_A:
                d[b_word].append('-1')
                checked_strings_from_B.add(b_word)
                continue
            for idx, a_word in enumerate(A_words):
                if b_word == a_word:
                    d[b_word].append(idx + 1)
                    checked_strings_from_B.add(b_word)
        else:  # if we come to duplicate string in B
            continue

    for key in B_words:
        print(' '.join([str(x) for x in d[key]]))


if __name__ == '__main__':
    # main_using_files()
    main()
