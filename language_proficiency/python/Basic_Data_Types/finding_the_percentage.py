""" https://www.hackerrank.com/challenges/finding-the-percentage """


def my_average(scores: list):
    scores_sum = 0
    for score in scores:
        scores_sum += score
    return float(scores_sum)/len(scores)


def main():
    marks = {}
    n = int(input(''))
    for _ in range(n):
        name, *line = input().split()
        # scores = list(map(float, line))
        scores = [float(elm) for elm in line]
        marks[name] = (scores, my_average(scores))
    # for pair in marks.items():
    #     print(pair)
    query_name = input()
    print(f'{marks[query_name][1]:.2f}')


if __name__ == '__main__':
    main()
