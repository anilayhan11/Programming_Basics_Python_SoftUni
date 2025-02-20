tournaments_count = int(input())
initial_score = int(input())
final_score = initial_score
counter_won = 0

for i in range(tournaments_count):
    tournament_result = input()

    if tournament_result == 'W':
        final_score += 2000
        counter_won += 1
    elif tournament_result == 'F':
        final_score += 1200
    elif tournament_result == 'SF':
        final_score += 720

average_score = (final_score - initial_score) // tournaments_count
wins_percent = counter_won / tournaments_count * 100

print(f'Final points: {final_score}')
print(f'Average points: {average_score}')
print(f'{wins_percent:.2f}%')

