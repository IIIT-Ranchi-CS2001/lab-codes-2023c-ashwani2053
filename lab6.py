# 1. Define a function my_zip() that forms a list of tuples based on customer details and the 'strict' parameter.
def custom_zip(names, ids, points, strict):
    if strict:
        if len(names) == len(ids) == len(points):
            return list(zip(names, ids, points))
        else:
            return "Lengths of the lists are not equal"
    else:
        return list(zip(names, ids, points))

names_list = input("Enter customer names: ").split()
ids_list = list(map(int, input("Enter customer ids: ").split()))
points_list = list(map(int, input("Enter shopping points: ").split()))
is_strict = input("Enter True or False: ").lower() == 'true'

zipped_list = custom_zip(names_list, ids_list, points_list, is_strict)
print(zipped_list)

# 2. Define a function custom_sort() to sort the list of tuples based on the provided key.
def custom_sort(zipped, sort_key):
    if sort_key == 0:
        zipped.sort(key=lambda x: x[0])
    elif sort_key == 1:
        zipped.sort(key=lambda x: x[1])
    elif sort_key == 2:
        zipped.sort(key=lambda x: x[2])

sort_key = int(input("Enter the key for sorting (0 for name, 1 for ID, 2 for points): "))
custom_sort(zipped_list, sort_key)
print(zipped_list)

# 3. Define a function my_max() to find the maximum value in a list, set, or tuple.
def my_max(args):
    m = args[0]
    for i in args[1:]:
        if i > m:
            m = i
    return m

myset = set(map(int, input("Enter numbers for the set: ").split()))
max_number = my_max(myset)
print(max_number)

# 4. Use map, lambda, and filter functions to operate on the user input string.
input_string = input("Enter the string: ")

# To find all letters and convert them to uppercase
letters = list(filter(lambda x: x.isalpha(), input_string))
upper_letters = list(map(lambda x: x.upper(), letters))
print(upper_letters)

# To find all digits and square them
digits = list(filter(lambda x: x.isdigit(), input_string))
squared_digits = list(map(lambda x: int(x) ** 2, digits))
print(squared_digits)

# To display all alphanumeric characters
alphanumeric = list(filter(lambda x: x.isalnum(), input_string))
print(alphanumeric)
