from math import copysign

from ops import launch


def steps(N, plants, greater):
    if N <= 3: return 0
    change_occurred = False
    changes = 0
    for i in range(N):
        if (plants[i] < plants[(i + 1) % N]) != greater:
            if change_occurred:
                return -1
            changes = min(i + 1, N - i - 1)
            change_occurred = True
    return changes


def task(input, output):
    N = int(input.readline())
    plants = [int(x) for x in input.readline().split(' ')]
    assert N == len(plants)
    s = steps(N, plants, True)
    if s == -1:
        s = steps(N, plants, False)
    output.write(str(s) + '\n')


launch(task, 'B-lehky.txt')
