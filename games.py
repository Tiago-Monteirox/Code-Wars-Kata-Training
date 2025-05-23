"""
Our team's match results are recorded in a collection of strings. Each match is represented by a string in the
format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)

We need to write a function that takes this collection and returns the number of points our team (x) got in the
championship by the rules given above.

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


def points(games):
    score = 0
    for i in games:
        j = i.split(':')
        if j[0] > j[1]:
            score += 3
        elif j[0] == j[1]:
            score += 1

    return score

points(['1:2', '2:2'])


# def points(games):
#     result = 0
#     for item in games:
#         result += 3 if item[0] > item[2] else 0
#         result += 1 if item[0] == item[2] else 0
#     return result




