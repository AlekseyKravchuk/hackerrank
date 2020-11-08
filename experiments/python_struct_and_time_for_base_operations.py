# below are Python structs and corresponding time for basic operations (insert, find, get, etc., if available)

from timeit import default_timer as timer
import random


def main():
    rand_lst = [random.randint(0, 1000) for x in range(1, 10 ** 6)]
    rand_set = {s for s in rand_lst}
    # print(rand_lst)
    # print(rand_set)
    start = timer()
    rand_lst.append(987)
    end = timer()
    print(f'Total time to insert value into array (Python list): {(10 ** 6 * (end - start)):.5f} microseconds')

    start = timer()
    rand_set.add(987)
    end = timer()
    print(f'Total time to insert value into set: {(10 ** 6 * (end - start)):.5f} microseconds')

    # print(end - start)


if __name__ == '__main__':
    main()
