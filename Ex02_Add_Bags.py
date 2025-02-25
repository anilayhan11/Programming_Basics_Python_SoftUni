excess_baggage_fee = float(input())
baggage_weight = float(input())
days_to_trip = int(input())
bags_count = int(input())

total_price = 0.00

if baggage_weight < 10:
    total_price += excess_baggage_fee * 0.20
elif baggage_weight <= 20:
    total_price += excess_baggage_fee * 0.50
elif baggage_weight > 20:
    total_price += excess_baggage_fee

if days_to_trip > 30:
    total_price *= 1.10
elif days_to_trip >= 7:
    total_price *= 1.15
elif days_to_trip < 7:
    total_price *= 1.40

total_price *= bags_count


print(f'The total price of bags is: {total_price:.2f} lv.')
