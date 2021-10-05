import operator

player_scores = [
  {'id': 5, 'roundscores': [1, 1, 1, 0]},
  {'id': 2, 'roundscores': [-2, -1, -1, -1]},
  {'id': 6, 'roundscores': None},
  {'id': 3, 'roundscores': [0, 0, -2, -1]},
  {'id': 4, 'roundscores': [0, 0, -1, -1]},
  {'id': 1, 'roundscores': [1, 0, -2, -1]},
]


player_names = [
  {'id': 4, 'name': "Bob"},
  {'id': 5, 'name': "Ann"},
  {'id': 1, 'name': "Joe"},
  {'id': 2, 'name': "Sue"},
  {'id': 3, 'name': "Jane"},
  {'id': 6, 'name': "Larry"},
]


def leaderboard(names, scores):
    # Assuming names length == scores length
    names.sort(key=operator.itemgetter('id'))
    scores.sort(key=operator.itemgetter('id'))

    LEN = len(names)
    for i in range(0, LEN):
        if not scores[i]['roundscores']:
            # Remove score and player if no score found
            del scores[i]
            del names[i]
            # Adjust LEN to avoid out of bounds
            LEN -= 1
        else:
            # Add to dictionary
            names[i]['score'] = sum(scores[i]['roundscores'])
            names[i]['winner'] = False

    names.sort(key=operator.itemgetter('score'))
    # Assuming sudden death and no two players will tie
    names[0]['winner'] = True
    return names


def print_leaderboard(l):
    # Attempt at making a table quickly in Python, not optimal, but works for now
    print('ID        Name       Score        Winner      ')
    for n in l:
        print('{:<10}{:<8}{:>6}{:>16}'.format(n['id'], n['name'], n['score'],("False", "True")[n['winner']]))


print_leaderboard(leaderboard(player_names, player_scores))

