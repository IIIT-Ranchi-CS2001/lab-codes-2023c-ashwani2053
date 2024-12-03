import math
from collections import Counter

# Euclidean Distance
def calculate_euclidean_distance():
    p1 = tuple(map(float, input("Enter point 1 (x, y, z): ").split(',')))
    p2 = tuple(map(float, input("Enter point 2 (x, y, z): ").split(',')))
    distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
    print("Euclidean Distance:", distance)

# Equation of a Straight Line
def calculate_straight_line_equation():
    x1, y1 = map(float, input("Enter point 1 (x1, y1): ").split(','))
    x2, y2 = map(float, input("Enter point 2 (x2, y2): ").split(','))
    if y1 == y2:
        print(f"The line is horizontal: y = {y1}")
    else:
        slope = (x2 - x1) / (y2 - y1)
        print(f"Equation of the line: (x - {x1}) = {slope} * (y - {y1})")

# Character Count in String
def count_characters_in_string():
    user_input = input("Enter a string: ")
    char_counts = Counter(user_input)
    print("Character counts:", dict(char_counts))

# List Comprehension with and without zip()
def list_comprehension_example():
    customers = [
        (input(f"Name {i+1}: "), input(f"ID {i+1}: "), int(input(f"Points {i+1}: ")))
        for i in range(3)
    ]
    customers_with_zip = list(zip(*[list(t) for t in zip(*customers)]))
    customers_without_zip = [(customers[i][0], customers[i][1], customers[i][2]) for i in range(3)]

    print("\nWith zip():", customers_with_zip)
    print("Without zip():", customers_without_zip)

# Sort Customers by Points
def sort_customers():
    customers = [
        (input(f"Name {i+1}: "), input(f"ID {i+1}: "), int(input(f"Points {i+1}: ")))
        for i in range(3)
    ]
    sorted_customers = sorted(customers, key=lambda x: x[2])
    print("\nSorted customers:", sorted_customers)

# Execution
while True:
    print("\n--- Choose an Option ---")
    print("1. Calculate Euclidean Distance")
    print("2. Find Equation of a Straight Line")
    print("3. Count Characters in a String")
    print("4. List Comprehension Example")
    print("5. Sort Customers by Shopping Points")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        calculate_euclidean_distance()
    elif choice == "2":
        calculate_straight_line_equation()
    elif choice == "3":
        count_characters_in_string()
    elif choice == "4":
        list_comprehension_example()
    elif choice == "5":
        sort_customers()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
