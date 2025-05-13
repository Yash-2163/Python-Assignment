# Easy Assignment

# This function returns only even numbers from a list
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Testing filter_even_numbers function
print("filter_even_numbers Test Cases:")
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))           # Should return []
print()


# This function merges two sorted lists and returns a new sorted list
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

# Testing merge_sorted_lists function
print("merge_sorted_lists Test Cases:")
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print()


# Medium Assignment

# This function makes a matrix where each element is i * j
def generate_matrix(n, m):
    return [[i * j for j in range(m)] for i in range(n)]

# Testing generate_matrix function
print("generate_matrix Test Cases:")
print(generate_matrix(3, 3))
# Should return:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]
print()


# This function gives the transpose of a matrix
def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Testing transpose_matrix function
print("transpose_matrix Test Cases:")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Should return:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
