#Functions Assignments

# Easy Assignment

# This function calculates average of a list
# If the list is empty, it gives 0
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Testing average function
print("calculate_average Test Cases:")
print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))              # Should return 0
print()


# This function greets a user
# If no greeting is given, it uses "Hello"
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Testing greet_user function
print("greet_user Test Cases:")
print(greet_user("Alice"))         # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))     # Should return "Hi, Bob!"
print()


# Medium Assignment

# This function adds all prices
# It can also apply a discount if given
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        total -= (total * discount / 100)
    return total

# Testing calculate_total function
print("calculate_total Test Cases:")
print(calculate_total(10, 20, 30))                   # Should return 60
print(calculate_total(10, 20, 30, discount=10))      # Should return 54
print()


# This function creates a multiplier
# It returns another function to multiply by that number
def create_multiplier(factor):
    def multiplier(n):
        return n * factor
    return multiplier

# Testing create_multiplier function
print("create_multiplier Test Cases:")
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # Should return 10
print(triple(5))  # Should return 15
