import sys


def launch(task, path):
    if path is None:
        input = sys.stdin
        output = sys.stdout
    else:
        input = open(path, 'r')
        output = open(path + '_output.txt', 'w')

    T = int(input.readline())
    for i in range(T):
        task(input, output)
