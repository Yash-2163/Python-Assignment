# Easy Assignment

# This function switches keys and values in a dictionary
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# Testing invert_dictionary
print("invert_dictionary Test Cases:")
print(invert_dictionary({"a": 1, "b": 2, "c": 3}))  # Should return {1: "a", 2: "b", 3: "c"}
print()


# This function merges two dictionaries
# If same key in both, second one's value is used
def merge_dictionaries(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

# Testing merge_dictionaries
print("merge_dictionaries Test Case:")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}
print()


# Medium Assignment

# This function counts how many times each word comes in a string
def word_frequencies(text):
    words = text.split()
    return {word: words.count(word) for word in words}

# Testing word_frequencies
print("word_frequencies Test Case:")
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
print()


# This function adds or updates a contact in a dictionary
def add_contact(contacts, name, **info):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(info)

# Testing add_contact
print("add_contact Test Case:")
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")
print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }
