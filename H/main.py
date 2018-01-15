from ops import launch


def shifts_to_swaps(shifts):
    print(shifts)
    changed = True
    swaps = []
    while changed:
        changed = False
        for i in range(len(shifts)):
            nextIndex = (i + 1) % len(shifts)
            if shifts[i] > shifts[nextIndex]:
                swaps.append((i, nextIndex))
                shifts[i], shifts[nextIndex] = shifts[nextIndex], shifts[i]
                shifts[i] += 1
                shifts[nextIndex] -= 1
                changed = True
    return swaps


def calculate_exchanges(satellites):
    L = len(satellites)
    requiredShifts = [satellites[i] - i for i in range(L)]
    while True:
        # measured to be fast
        minIndex, maxIndex = requiredShifts.index((min(requiredShifts))), requiredShifts.index((max(requiredShifts)))
        if requiredShifts[maxIndex] - requiredShifts[minIndex] <= L:
            break
        # this doesn't make the solution invalid & provides a better solution
        requiredShifts[minIndex] += L
        requiredShifts[maxIndex] -= L
    return shifts_to_swaps(requiredShifts)


def task(input, output):
    N = int(input.readline())
    assert N > 0
    satellites = [int(x) - 1 for x in input.readline().split(' ')]
    assert len(satellites) == N
    exchanges = calculate_exchanges(satellites)
    output.write(str(len(exchanges)) + '\n')
    for swap in exchanges:
        output.write(str(swap[0] + 1) + ' ' + str(swap[1] + 1) + '\n')
    # print(f'Done {len(exchanges)}')


# launch(task, 'H-tezky.txt')
launch(task, None)
