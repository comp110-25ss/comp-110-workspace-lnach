"""Practice instantiating Pizza class"""

from Lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)

print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())
