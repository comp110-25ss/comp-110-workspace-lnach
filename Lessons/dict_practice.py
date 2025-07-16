"""Practice with dictionaries"""

# Creating a dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

print("Ice cream after adding mint")

# Adding a value to a dictionary
ice_cream["mint"] = 3

print(ice_cream)

print("Ice cream after removing mint")

# Removing a value from a dictionary
ice_cream.pop("mint")

# Accessing a value
print(ice_cream["vanilla"])
print(f"{ice_cream['vanilla']} vanilla orders")

# Updating a value
ice_cream["vanilla"] += 1

# After adding 1 vanilla
print(f"{ice_cream['vanilla']} vanilla orders")

# Check if something is in a dictionary
print("vanilla" in ice_cream)

ice_cream["pecan"]
