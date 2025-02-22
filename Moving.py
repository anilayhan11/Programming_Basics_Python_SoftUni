width = int(input())
length = int(input())
height = int(input())

available_space = width * length * height
filled_space = 0

command = input()

while command != 'Done':
    boxes_count = int(command)
    filled_space += boxes_count

    if filled_space > available_space:
        break

    command = input()

if command == 'Done':
    print(f'{available_space - filled_space} Cubic meters left.')
elif filled_space > available_space:
    print(f'No more free space! You need {filled_space - available_space} Cubic meters more.')



















