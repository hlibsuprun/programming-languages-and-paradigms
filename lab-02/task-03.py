def find_extremes(data):
    largest_number = max(filter(lambda x: isinstance(x, (int, float)), data), default=None)
    longest_string = max(filter(lambda x: isinstance(x, str), data), key=len, default=None)
    largest_tuple = max(filter(lambda x: isinstance(x, tuple), data), key=len, default=None)
    return largest_number, longest_string, largest_tuple


data = [1, "przykładowy tekst", (1, 5, 3), 4.5, "dłuższy tekst", (1, 2)]
result = find_extremes(data)
print(result)
