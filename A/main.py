def can_drive(N, path):
        assert len(path) == N
        for j in range(N - 1):
            if path[j + 1] - path[j] > 3:
                return False
        return True


T = int(input())
for i in range(T):
    N = int(input())
    path = [int(x) for x in input().split(' ')]
    print('ano' if can_drive(N, path) else 'ne')
