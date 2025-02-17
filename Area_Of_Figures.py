import math

figure = input()
area = 0.00

if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'rectangle':
    side = float(input())
    height = float(input())
    area = side * height
elif figure == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
elif figure == 'triangle':
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f'{area:.3f}')

