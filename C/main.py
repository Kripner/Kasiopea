from ops import launch


def dist(planes, a, b):
    return abs(planes[a] - planes[b]) * 20


def find_letter(N, planes):
    if N <= 2: raise Exception()
    letter = None
    letter_save = None
    for i in range(1, N - 1):
        distance_saved = (dist(planes, i - 1, i) + dist(planes, i, i + 1)) - dist(planes, i - 1, i + 1)
        if letter is None or distance_saved > letter_save:
            letter = i
            letter_save = distance_saved
    return letter


def task(input, output):
    N = int(input.readline())
    planes = [int(x) for x in input.readline().split(' ')]
    assert N == len(planes)
    output.write(str(find_letter(N, planes)) + '\n')


launch(task, 'C-lehky.txt')
# launch(task, None)
