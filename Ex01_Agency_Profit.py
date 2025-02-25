aviation_company = input()
tickets_count_adults = int(input())
tickets_count_children = int(input())
ticket_price_adult = float(input())
ticket_price_child = ticket_price_adult * 0.30
service_fee = float(input())

all_tickets_price = tickets_count_adults * ticket_price_adult \
                    + tickets_count_children * ticket_price_child \
                    + tickets_count_adults * service_fee \
                    + tickets_count_children * service_fee

profit = all_tickets_price * 0.20

print(f'The profit of your agency from {aviation_company} tickets is {profit:.2f} lv.')


