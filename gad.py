def strings_to_lengths(string_list):
    return {string: len(string) for string in string_list}

strings = ["apple", "banana", "cherry"]
lengths = strings_to_lengths(strings)
print(lengths) 