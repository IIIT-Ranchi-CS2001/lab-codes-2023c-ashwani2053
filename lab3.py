# Squares of First n Natural Numbers
print("Task 1: Squares of First n Natural Numbers")
n = int(input("Enter the value of n: "))
print("Number\tSquare")
i = 1
while i <= n:
    print(f"{i}\t\t{i**2}")
    i += 1
print("-" * 30)

# Sum of the Digits of a Given Number
print("Task 2: Sum of the Digits of a Given Number")
num = int(input("Enter a number: "))
original_num = num
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(f"The sum of the digits of {original_num} is {digit_sum}.")
print("-" * 30)

# Fibonacci Series
print("Task 3: Fibonacci Series")
n = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
count = 0
print("Fibonacci Series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print("\n" + "-" * 30)

#  Multiplication Table
print("Task 4: Multiplication Table")
num = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter the limit: "))
print(f"Multiplication Table of {num}:")
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")
print("-" * 30)

#  Check for Alphanumeric Characters
print("Task 5: Check for Alphanumeric Characters")
string = input("Enter a string: ")
is_alphanumeric = True
for char in string:
    if not char.isalnum():
        is_alphanumeric = False
        break
print("All characters are alphanumeric:" if is_alphanumeric else "Not all characters are alphanumeric.")
print("-" * 30)

# Count Occurrences of a Character
print("Task 6: Count Occurrences of a Character")
string = input("Enter a string: ")
char_to_find = input("Enter the character to find: ")
count = 0
for char in string:
    if char == char_to_find:
        count += 1
print(f"The character '{char_to_find}' occurs {count} times in the string.")
print("-" * 30)
