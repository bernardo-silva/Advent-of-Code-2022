def compute_score(file):
    opponent_plays = dict(A="Rock", B="Paper", C="Scissors")
    my_plays = dict(X="Rock", Y="Paper", Z="Scissors")

    plays = [(opponent_plays[l.strip().split()[0]],
              my_plays[l.strip().split()[1]]) for l in file]

    beats = dict(Rock="Scissors", Paper="Rock", Scissors="Paper")
    play_score = dict(Rock=1, Paper=2, Scissors=3)

    score = 0
    for opponent, mine in plays:
        score += play_score[mine]
        if opponent == mine:
            score += 3
            continue
        if beats[opponent] == mine:
            continue
        else:
            score += 6

    return score


def compute_score2(file):
    opponent_plays = dict(A="Rock", B="Paper", C="Scissors")
    beats = dict(Rock="Scissors", Paper="Rock", Scissors="Paper")
    loses = dict(zip(beats.values(), beats.keys()))
    play_score = dict(Rock=1, Paper=2, Scissors=3)

    my_plays = dict(X=beats.get, Y=lambda x: x, Z=loses.get)

    plays = [(opponent_plays[l.strip().split()[0]],
              l.strip().split()[1]) for l in file]

    score = 0
    for opponent, mine in plays:
        play = my_plays[mine](opponent)
        score += play_score[play]
        if opponent == play:
            score += 3
            continue
        if beats[opponent] == play:
            continue
        else:
            score += 6

    return score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        score = compute_score(f)
    with open("input.txt", "r") as f:
        score2 = compute_score2(f)

    # Part 1
    print(score)

    # Part 2
    print(score2)
