""" https://www.hackerrank.com/challenges/the-minion-game/problem """

import string


def minion_game(word):
    length = len(word)
    score = {'Kevin': 0,
             'Stuart': 0}
    vowels = {'A', 'E', 'I', 'O', 'U'}                   # for Kevin
    consonants = set(string.ascii_uppercase) - (vowels)  # for Stuart

    for pos, letter in enumerate(word):
        points = (length - pos)
        if letter in vowels:
            score['Kevin'] += points
        if letter in consonants:
            score['Stuart'] += points
    if score['Kevin'] != score['Stuart']:
        print(*max(score.items(), key=lambda x: x[1]))
    else:
        print('Draw')


def main():
    s = input()
    minion_game(s)


if __name__ == '__main__':
    main()
