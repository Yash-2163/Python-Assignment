# Easy Assignment

# Rectangle class with area and perimeter methods
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # area is width times height
        return self.width * self.height

    def perimeter(self):
        # perimeter is 2 * (width + height)
        return 2 * (self.width + self.height)

# Testing Rectangle class
print("Rectangle Test Cases:")
rect = Rectangle(5, 10)
print(rect.area())       # Should return 50
print(rect.perimeter())  # Should return 30
print()


# Counter class to increment, decrement, and reset
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        # increase value by 1
        self.value += 1

    def decrement(self):
        # decrease value by 1
        self.value -= 1

    def reset(self):
        # set value back to 0
        self.value = 0

# Testing Counter class
print("Counter Test Cases:")
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Should return 2
counter.decrement()
print(counter.value)  # Should return 1
counter.reset()
print(counter.value)  # Should return 0
print()


# Medium Assignment

# Vehicle base class and Car subclass with extra features
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        # use parent class constructor
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

# Testing Car class
print("Car Inheritance Test Cases:")
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)   # Should return "Toyota"
print(car.doors)  # Should return 4
print()


# BankAccount with private attributes
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private
        self.__balance = balance                # private

    def deposit(self, amount):
        # add money to balance
        self.__balance += amount

    def withdraw(self, amount):
        # remove money from balance
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Testing BankAccount class
print("BankAccount Encapsulation Test Cases:")
account = BankAccount("123456", 1000)
print(account.get_balance())  # Should return 1000
account.deposit(500)
print(account.get_balance())  # Should return 1500
account.withdraw(200)
print(account.get_balance())  # Should return 1300
print(account.get_account_number())  # Should return "123456"

# Trying to change private attribute directly (should not do this)
try:
    account.__balance = 99999  # This won't change real balance
    print(account.__balance)   # Will create new attribute, not modify actual one
    print(account.get_balance())  # Real balance is still 1300
except AttributeError:
    print("Cannot directly access private attribute")
