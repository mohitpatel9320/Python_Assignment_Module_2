# Program to update a value at a particular key in a dictionary

# Sample dictionary
sample_dict = {
    'name': 'mohit',
    'age': 22,
    'city': 'Ahmedabad'
}

# Key to update
key_to_update = 'age'
# New value
new_value = 30

# Update the dictionary
if key_to_update in sample_dict:
    sample_dict[key_to_update] = new_value
    print(f"Updated dictionary: {sample_dict}")
else:
    print(f"Key '{key_to_update}' not found in the dictionary.")