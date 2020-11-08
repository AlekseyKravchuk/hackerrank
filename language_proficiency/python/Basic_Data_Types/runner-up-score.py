""" https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem """


def main():
    n = int(input())
    # numbers = [int(x) for x in input(f'Type in {n} numbers in a row: ').split()]
    numbers = [int(x) for x in input().split()]
    numbers.sort(reverse=True)
    print(numbers)
    for idx, elm in enumerate(numbers):
        if elm == numbers[idx + 1]:
            continue
        print(numbers[idx + 1])
        break


if __name__ == "__main__":
    main()
