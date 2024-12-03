import math

# 1. String Manipulations
S1 = "Maha Bharat"
print(S1[:1].lower() + S1[1:4].upper() + " " + S1[5:6].lower() + S1[6:].upper())  # a
print(S1[5:])  # b
print(S1[5:] * 3)  # c
print("Mera " + S1[5:])  # d
print("Mera " + S1[5:] + " Mahan")  # e

# 2. String Analysis
S = "Ba Ba Black Sheep"
print(len(S))  # a
print(S.find('e'))  # b
print(S.count('a'))  # c
print(S.replace('B', 'T'))  # d

# 3. Palindrome Check
inp = input("Enter a string: ").lower().replace(" ", "")
print("Palindrome" if inp == inp[::-1] else "Not a palindrome")

# 4. Student Details
def grade(m):
    return (10, "OUTSTANDING") if m >= 90 else \
           (9, "VERY GOOD") if m >= 80 else \
           (8, "GOOD") if m >= 70 else \
           (7, "AVERAGE") if m >= 60 else \
           (6, "PASS") if m >= 50 else (0, "FAIL")

n = input("Name: ")
r = input("Roll: ")
m = int(input("Marks: "))
g, rem = grade(m)
print(f"\nName: {n}\nRoll: {r}\nMarks: {m}\nGrade: {g}\nRemark: {rem}")

# 5. Quadratic Equation Roots
def roots(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        return (r1, r2)
    return (-b / (2 * a), math.sqrt(-d) / (2 * a))

a, b, c = map(int, input("Enter coefficients a, b, c: ").split())
r1, r2 = roots(a, b, c)
if isinstance(r2, float):
    print(f"Roots: {r1:.2f}, {r2:.2f}")
else:
    print(f"Roots: {r1:.2f} ± {r2:.2f}i")
