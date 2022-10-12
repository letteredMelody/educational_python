shopping_list = {}

name, purchase, amount = input().split()
shopping_list[name][purchase] = shopping_list.setdefault(name, {}).setdefault(purchase, 0) + int(amount)

name, purchase, amount = input().split()
shopping_list[name][purchase] = shopping_list.setdefault(name, {}).setdefault(purchase, 0) + int(amount)

name, purchase, amount = input().split()
shopping_list[name][purchase] = shopping_list.setdefault(name, {}).setdefault(purchase, 0) + int(amount)

name, purchase, amount = input().split()
shopping_list[name][purchase] = shopping_list.setdefault(name, {}).setdefault(purchase, 0) + int(amount)

customer = input('Customer:')

print(f'{customer}:')
print('\n'.join(str(shopping_list[customer])[1:-1].split(', ')))