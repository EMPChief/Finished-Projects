food = ['Apple', 'Banana', 'Orange', 'Mango']

store = [('Bannana', 3.99),
        ('Apple', 2.19),
        ('Orange', 1.59),
        ('Mango', 0.99),
        ('Dragon Fruit', 9.10)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]*0.95)

store_euros = list(map(to_euros, store))
store_dollers = list(map(to_dollars, store))
for a in store_euros:
    print(f"Store in Euro {a}")
for b in store_dollers:
    print(f"Store in Doller {b}")

