"""Dicts practice Quiz questions 10 through 20"""

# 10.
my_dictionary: dict[str, float] = dict()

# 11.
msg: dict[str, int] = {"Hello": 1, "Yall": 2}

msg["Yall"]

# 12.
msg: dict[str, int] = {"Hello": 1, "Yall": 2}

msg["Yall"] += 3

# 13.
ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}

ids.pop(100)

# 14.
ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}

ids.pop(100)

# 15.
inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}

inventory["markers"] = 15

# 16.
prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}

prices["milk"] = 2.50

# 17.
scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}

scores.keys()

# 18.
scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}


# 19.
fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}

for fruit in fruit_count:
    print(f"{fruit}:{fruit_count[fruit]}")

# 20.
first_dict: dict[str, int] = {"a": 1, "b": 2}
second_dict: dict[str, int] = {"c": 3, "d": 4}
combo_dict: dict[str, int] = {}
