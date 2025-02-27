magic_num = int(input())

for number in range(1111, 9999 + 1):
    number_as_str = str(number)
    divisible_counter = 0

    for idx, digit in enumerate(number_as_str):
        if int(digit) != 0 and magic_num % int(digit) == 0:
            divisible_counter += 1

    if divisible_counter == 4:
        print(f'{number}', end=' ')




