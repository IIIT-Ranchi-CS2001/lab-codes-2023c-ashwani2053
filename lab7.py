import random
import math
import matplotlib.pyplot as plt

# Ques 1: Election Seat Share Visualization
mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]
rj_parties = ['INC', 'BJP', 'BSP', 'Others']
rj_seats = [69, 115, 2, 13]

# Calculate percentages for pie chart
mp_percent = [seat / sum(mp_seats) * 100 for seat in mp_seats]
rj_percent = [seat / sum(rj_seats) * 100 for seat in rj_seats]

# Create pie charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].pie(mp_percent, labels=mp_parties, autopct='%1.1f%%', explode=[0.03 if x == max(mp_percent) else 0 for x in mp_percent])
axs[0].set_title('Madhya Pradesh Seat Share')

axs[1].pie(rj_percent, labels=rj_parties, autopct='%1.1f%%', explode=[0.02 if x == max(rj_percent) else 0 for x in rj_percent])
axs[1].set_title('Rajasthan Seat Share')
plt.show()

# Create bar chart for seat distribution
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([i - 0.2 for i in range(len(mp_parties))], mp_seats, width=0.4, label='Madhya Pradesh', color='blue')
ax.bar([i + 0.2 for i in range(len(mp_parties))], rj_seats, width=0.4, label='Rajasthan', color='orange')
ax.set_xticks(range(len(mp_parties)))
ax.set_xticklabels(mp_parties)
ax.set_xlabel('Parties')
ax.set_ylabel('Seats')
ax.set_title('Assembly Elections 2023 Seat Distribution')
ax.legend()
plt.show()

# Ques 2: Prime and Composite Number Classification
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Input
K = int(input("Enter the number of random numbers (K, min 10): "))
N = int(input("Enter the upper limit (N): "))

if K < 10:
    print("K must be at least 10.")
else:
    # Generate random numbers
    numbers = [random.randint(1, N) for _ in range(K)]

    # Classify numbers
    primes = [x for x in numbers if is_prime(x)]
    composites = [x for x in numbers if not is_prime(x) and x > 1]

    # Compute squares and square roots
    prime_squares = [x ** 2 for x in primes]
    composite_roots = [math.sqrt(x) for x in composites]

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Prime numbers vs squares
    axs[0].scatter(primes, prime_squares, color='green', label='Prime Numbers')
    axs[0].set_title('Prime Numbers vs. Squares')
    axs[0].set_xlabel('Prime Numbers')
    axs[0].set_ylabel('Squares')
    axs[0].legend()

    # Composite numbers vs square roots
    axs[1].scatter(composites, composite_roots, color='red', label='Composite Numbers')
    axs[1].set_title('Composite Numbers vs. Square Roots')
    axs[1].set_xlabel('Composite Numbers')
    axs[1].set_ylabel('Square Roots')
    axs[1].legend()

    plt.tight_layout()
    plt.show()
