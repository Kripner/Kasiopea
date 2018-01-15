from ops import launch


def distance(diff):
    dist = 0
    for i in range(1, len(diff)):
        flip = diff[i - 1] != diff[i]
        if i + 1 == len(diff):
            flip = flip and (not diff[i])
        else:
            flip = flip and diff[i] != diff[i + 1]
        if flip:
            diff[i] = not diff[i]
            dist += 1
    blocks = 1
    for i in range(1, len(diff)):
        if diff[i] != diff[i - 1]:
            blocks += 1
    dist += blocks
    if diff[len(diff) - 1]:
        dist -= 1
    return dist


def task(input, output):
    N = int(input.readline())
    assert N > 0
    firstString = list(input.readline()[:-1])
    secondString = list(input.readline()[:-1])
    # assert len(firstString) == len(secondString) == N

    diff = [firstString[i] == secondString[i] for i in range(len(firstString))]
    output.write(str(distance(diff)) + '\n')


launch(task, 'E-lehky.txt')

