days = int(input())
nights = days - 1
accommodation = input()
rating = input()
price = 0.00

if accommodation == 'room for one person':
    price = 18.00 * nights
elif accommodation == 'apartment':
    if days < 10:
        price = 25.00 * nights * 0.70
    elif 10 <= days <= 15:
        price = 25.00 * nights * 0.65
    elif days > 15:
        price = 25.00 * nights * 0.50
elif accommodation == 'president apartment':
    if days < 10:
        price = 35.00 * nights * 0.90
    elif 10 <= days <= 15:
        price = 35.00 * nights * 0.85
    elif days > 15:
        price = 35.00 * nights * 0.80

if rating == 'positive':
    price *= 1.25
elif rating == 'negative':
    price *= 0.90

print(f'{price:.2f}')