joinery_count = int(input())
joinery_type = input()
delivery_type = input()

final_price = 0.00

if joinery_type == '90X130':
    final_price = 110 * joinery_count

    if joinery_count > 60:
        final_price *= 0.92
    elif joinery_count > 30:
        final_price *= 0.95


elif joinery_type == '100X150':
    final_price = 140 * joinery_count

    if joinery_count > 80:
        final_price *= 0.90
    elif joinery_count > 40:
        final_price *= 0.94

elif joinery_type == '130X180':
    final_price = 190 * joinery_count

    if joinery_count > 50:
        final_price *= 0.88
    elif joinery_count > 20:
        final_price *= 0.93


elif joinery_type == '200X300':
    final_price = 250 * joinery_count

    if joinery_count > 50:
        final_price *= 0.86
    elif joinery_count > 25:
        final_price *= 0.91

if delivery_type == 'With delivery':
    final_price += 60

if joinery_count > 99:
    final_price *= 0.96

if joinery_count < 10:
    print('Invalid order')
else:
    print(f'{final_price:.2f} BGN')


