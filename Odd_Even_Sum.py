n = int(input())
sum_even = 0
sum_odd = 0

for idx in range(n):
    num = int(input())

    if idx % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_even}')

else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')
