player = input()
best_player = ''
best_score = 0
hat_trick = False

while player != 'END':
    goals = int(input())

    if goals > best_score:
        best_score = goals
        best_player = player

    if goals >= 3:
        hat_trick = True

    if goals >= 10:
        break

    player = input()


print(f'{best_player} is the best player!')

if best_score >= 3:
    print(f'He has scored {best_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_score} goals.')
