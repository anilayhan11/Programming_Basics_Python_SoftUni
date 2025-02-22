for num1 in range(1, 3 + 1):
    for num2 in range(1, 5 + 1):
        result = num1 * num2
        print(f'{num1} * {num2} = {result}')

        break  # breaks inner loop
    break  # breaks outer loop
