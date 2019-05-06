""" This program shows a quick use of python's dict """
pizzas = {
    "cheese": 9,
    "pepperoni": 10,
    "vegetable": 11,
    "buffallo chicken": 12
}

pizzas["bacon"] = 14

for pizza in pizzas:
    print(pizza)

for pizza, price in pizzas.items():
    print("A whole {} pizza costs ${}".format(pizza, price))

print()
for pizza, price in pizzas.items():
    print("A whole "+ pizza +" pizza costs $"+ str(price))
