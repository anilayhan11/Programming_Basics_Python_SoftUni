destination = input()

while destination != 'End':
    min_budget = float(input())
    money_collected = 0.00

    while money_collected < min_budget:
        saving = float(input())
        money_collected += saving

    print(f'Going to {destination}!')

    destination = input()
