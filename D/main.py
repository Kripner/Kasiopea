from ops import launch
#
# def add_distances_left_to_right(buildings, candidates, height, width):
#     tmp = [0] * height
#     for i in range(width):
#


def best_distance(M, N, buildings):
    columnsSums = []
    for i in range(M):
        sum = 0
        for j in range(N):
            sum += buildings[j][i]
        columnsSums.append(sum)
    column, columnError = None, None
    for i in range(M):
        currentColumnError = 0
        for j in range(M):
            currentColumnError += abs(i - j) * columnsSums[j]
        if column is None or currentColumnError < columnError:
            column = i
            columnError = currentColumnError

    rowsSum = []
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += buildings[i][j]
        rowsSum.append(sum)
    row, rowError = None, None
    for i in range(N):
        currentRowError = 0
        for j in range(N):
            currentRowError += abs(i - j) * rowsSum[j]
        if row is None or currentRowError < rowError:
            row = i
            rowError = currentRowError
    # print(row, column)
    return rowError + columnError


def task(input, output):
    N, M = [int(x) for x in input.readline().split(' ')]
    assert N > 0 and M > 0
    buildings = []
    for i in range(N):
        row = [int(x) for x in input.readline().split(' ')]
        assert len(row) == M
        buildings.append(row)
    output.write(str(best_distance(M, N, buildings)) + '\n')


launch(task, 'D-lehky.txt')
# launch(task, None)
