chicken_menus = int(input())
fish_menus = int(input())
veggy_menus = int(input())

total_price = chicken_menus * 10.35 + fish_menus * 12.40 + veggy_menus * 8.15

dessert_price = total_price * 0.20

total_price += dessert_price + 2.50

print(total_price)