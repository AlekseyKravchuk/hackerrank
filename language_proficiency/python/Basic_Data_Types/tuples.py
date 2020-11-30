""" https://www.hackerrank.com/challenges/python-tuples/problem """


def main():
    N = int(input())
    print(hash(tuple(t for t in map(int, input().split()))))


if __name__ == '__main__':
    main()
