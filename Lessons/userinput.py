"""Practice user input, elif, and local variables"""

forecast: str = input("What is the weather? ")


if forecast == "rainy":
    print("Bring a jacket!")
elif forecast == "sunny":
    print("Bring sunglasses")
else:
    print("I don't have any advice for you")

age: int = 10
age = age + 1
print(age)
