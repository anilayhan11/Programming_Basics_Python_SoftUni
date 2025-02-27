command = input()
sum_prime_nums = 0
sum_non_prime_nums = 0

while command != 'stop':
    num = int(command)

    if num < 0:
        print('Number is negative.')
        command = input()
        continue

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime:
        sum_prime_nums += num
    else:
        sum_non_prime_nums += num

    command = input()

print(f'Sum of all prime numbers is: {sum_prime_nums}')
print(f'Sum of all non prime numbers is: {sum_non_prime_nums}')
