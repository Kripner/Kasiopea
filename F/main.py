from heapq import heappush, heappop

from ops import launch


def calculate_seats(N, M, parties):
    seats = [0] * N
    queue = []
    i = 0
    for party in parties:
        heappush(queue, [-party, 1, i])
        i += 1

    for i in range(M):
        try:
            wonSeat = heappop(queue)
        except IndexError:
            print('wut?')
            break
        seats[wonSeat[2]] += 1
        wonSeat[0] = (wonSeat[0] * wonSeat[1]) / (wonSeat[1] + 1)
        wonSeat[1] += 1
        heappush(queue, wonSeat)
    return seats


def task(input, output):
    N, M = [int(x) for x in input.readline().split(' ')]
    assert N > 0 and M > 0
    votes = [int(x) for x in input.readline().split(' ')]
    assert len(votes) == N
    output.write(' '.join([str(x) for x in calculate_seats(N, M, votes)]) + '\n')


launch(task, 'F-lehky.txt')

