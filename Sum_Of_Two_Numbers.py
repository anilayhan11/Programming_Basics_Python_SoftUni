interval_start = int(input())
interval_end = int(input())
magic_num = int(input())

combo_count = 0
is_found = False

for num1 in range(interval_start, interval_end + 1):
    for num2 in range(interval_start, interval_end + 1):
        combo_count += 1

        if num1 + num2 == magic_num:
            is_found = True
            break
    if is_found:
        break


if is_found:
    print(f'Combination N:{combo_count} ({num1} + {num2} = {magic_num})')
else:
    print(f'{combo_count} combinations - neither equals {magic_num}')



