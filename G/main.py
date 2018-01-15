from ops import launch


def count_participants(sessionsCount, sessionCapacity, teams):
    people = sum(teams)
    
    memo = [None] * (sessionCapacity + 1)
    participants = 0
    sessionsDone = 0

    waitingForSession = 0
    while True:
        if memo[waitingForSession] is not None and sessionsDone - memo[waitingForSession][1] <= sessionsCount - sessionsDone:
            cycleAddedPeople = participants - memo[waitingForSession][0]
            cycleDoneSessions = sessionsDone - memo[waitingForSession][1]
            repeats = (sessionsCount - sessionsDone) // cycleDoneSessions

            participants += cycleAddedPeople * repeats
            sessionsDone += cycleDoneSessions * repeats

            if sessionsDone == sessionsCount:
                return participants
        else:
            participantsBefore = participants
            waitingForSessionBefore = waitingForSession
            sessionsDoneBefore = sessionsDone

            for team in teams:
                if waitingForSession + team > sessionCapacity:
                    sessionsDone += 1
                    participants += waitingForSession
                    waitingForSession = 0
                    if sessionsDone == sessionsCount:
                        return participants
                waitingForSession += team
            if sessionsDoneBefore == sessionsDone or waitingForSession == sessionCapacity:
                sessionsDone += 1
                participants += waitingForSession
                waitingForSession = 0
                if sessionsDone == sessionsCount:
                    return participants
            memo[waitingForSessionBefore] = (participantsBefore, sessionsDoneBefore)


def task(input, output):
    R, K, N = [int(x) for x in input.readline().split(' ')]
    assert N > 0 and R > 0 and K > 0
    teams = [int(x) for x in input.readline().split(' ')]
    assert len(teams) == N
    output.write(str(count_participants(R, K, teams)) + '\n')
    print('Done')


launch(task, 'G-lehky.txt')

