""" https://www.hackerrank.com/challenges/python-mutations/problem """


def mutate_string(s, i, c):
    return s[:i] + c + s[i+1:]


def main():
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


if __name__ == '__main__':
    main()
