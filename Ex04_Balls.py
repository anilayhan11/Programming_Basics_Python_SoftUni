import math

n = int(input())
score = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0

for ball in range(n):
    color = input()

    if color == 'red':
        score += 5
        red_balls += 1
    elif color == 'orange':
        score += 10
        orange_balls += 1
    elif color == 'yellow':
        score += 15
        yellow_balls += 1
    elif color == 'white':
        score += 20
        white_balls += 1
    elif color == 'black':
        score = math.floor(score / 2)
        black_balls += 1
    else:
        other_balls += 1

print(f'Total points: {score}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print(f'Divides from black balls: {black_balls}')


