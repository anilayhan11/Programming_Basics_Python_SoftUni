city = input()
sales = float(input())
commission_percent = 0.00
valid = True

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission_percent = 5
    elif 500 < sales <= 1000:
        commission_percent = 7
    elif 1000 < sales <= 10000:
        commission_percent = 8
    elif sales > 10000:
        commission_percent = 12
    else:
        valid = False

elif city == 'Varna':
    if 0 <= sales <= 500:
        commission_percent = 4.5
    elif 500 < sales <= 1000:
        commission_percent = 7.5
    elif 1000 < sales <= 10000:
        commission_percent = 10
    elif sales > 10000:
        commission_percent = 13
    else:
        valid = False

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission_percent = 5.5
    elif 500 < sales <= 1000:
        commission_percent = 8
    elif 1000 < sales <= 10000:
        commission_percent = 12
    elif sales > 10000:
        commission_percent = 14.5
    else:
        valid = False

else:
    valid = False

if valid:
    print(f'{sales * commission_percent / 100:.2f}')
else:
    print('error')
