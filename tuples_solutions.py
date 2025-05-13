# Easy Assignment

# This function swaps every two elements in a tuple
# If there's an odd element at the end, it stays as it is
def swap_pairs(t):
    result = []
    i = 0
    while i < len(t):
        if i + 1 < len(t):
            result.extend([t[i + 1], t[i]])
            i += 2
        else:
            result.append(t[i])
            i += 1
    return tuple(result)

# Testing swap_pairs function
print("swap_pairs Test Cases:")
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))     # Should return (2, 1, 3)
print()


# This function returns min, max, sum, and average of a list
def get_stats(numbers):
    if not numbers:
        return (None, None, 0, 0)
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)
    return (minimum, maximum, total, avg)

# Testing get_stats function
print("get_stats Test Cases:")
print(get_stats([1, 2, 3, 4, 5]))  # Should return (1, 5, 15, 3.0)
print()


# Medium Assignment

# This function returns the student with highest average grade
from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def top_student(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades))

# Testing top_student function
print("top_student Test Case:")
alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return Charlie
print()


# This function counts how many times each coordinate appears
def count_coordinate_occurrences(coords):
    count_dict = {}
    for coord in coords:
        if coord in count_dict:
            count_dict[coord] += 1
        else:
            count_dict[coord] = 1
    return count_dict

# Testing count_coordinate_occurrences function
print("count_coordinate_occurrences Test Case:")
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))  # Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}
