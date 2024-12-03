# 1. Find the number of palindrome words in a given sentence
sentence = input("Enter a sentence: ").split()
palindrome_words = [word for word in sentence if word == word[::-1]]
print(f"Number of palindrome words: {len(palindrome_words)}")

# 2. Find the mean, median, and mode of a list without using statistics module
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Mean calculation
mean = sum(numbers) / len(numbers)

# Median calculation
numbers.sort()
n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

# Mode calculation (using a dictionary to count occurrences)
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
mode = [key for key, value in frequency.items() if value == max(frequency.values())]

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

# 3. Generate a new list with both course code and course name
course_codes = input("Enter course codes separated by space: ").split()
course_names = input("Enter course names separated by space: ").split()

# Create the list of combined course code and name
course_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print(course_list)

# 4. Generate two sets for singers and dancers, then perform set operations
singers = {name for name in input("Enter singers separated by space: ").split()}
dancers = {name for name in input("Enter dancers separated by space: ").split()}

# Set operations
all_artists = singers.union(dancers)
allrounders = singers.intersection(dancers)
dancers_not_singers = dancers.difference(singers)
singers_not_dancers = singers.difference(dancers)
dancers_and_singers = dancers.symmetric_difference(singers)

print(f"All artists: {all_artists}")
print(f"Allrounders: {allrounders}")
print(f"Dancers but not singers: {dancers_not_singers}")
print(f"Singers but not dancers: {singers_not_dancers}")
print(f"Dancers but not singers cum singers but not dancers: {dancers_and_singers}")
