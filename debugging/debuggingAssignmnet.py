# Advanced Debugging Assignment Solutions

# 1. Error Classification
# a) Syntax Error: Missing colon
for i in range(5):  # Fixed: Added colon
    print(i)

# b) Runtime Error: Division by zero
try:
    x = 10 / 0  # Fixed: Wrapped in try-except
except ZeroDivisionError:
    x = "Error: Division by zero"
    print(x)

# c) Logic Error: Incorrect formula for area
# Fixed: Changed formula to calculate area correctly
def calculate_area(radius):
    return 3.14 * radius ** 2  # Corrected formula

# 2. Debugging Complex Functions

def process_data(data):
    total = 0
    count = 0
    for item in data:
        try:
            total += int(item)  # Convert item to integer
            count += 1  # Only count valid numbers
        except ValueError:
            print(f"Skipping invalid data: {item}")
    return total / count if count > 0 else "Error: No valid data to process"

print(process_data(['10', '20', 'abc', '30']))

# 3. Advanced Debugging Challenge
import random

def unreliable_function():
    number = random.choice([1, 2])  # Fixed: Removed 0 to prevent division by zero
    return 10 / number

for i in range(10):
    print(unreliable_function())

# 4. Writing Debug-Friendly Code
def calculate_discount(price, discount):
    try:
        discount = float(discount)  # Convert discount to float
        return price - (price * discount / 100)
    except ValueError:
        return "Error: Invalid discount format"

print(calculate_discount(100, '10'))  # Fixed input format

# 5. Rubber Duck Debugging
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("Product:", result)  # Explains step-by-step multiplication

# 6. Debugging a Multi-threaded Program
import threading

counter = 0
lock = threading.Lock()  # Added lock to prevent race conditions

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Now correctly outputs 200000

# 7. Activity: Debug with Breakpoints

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

a = 10
b = 0
print(divide(a, b))

# 8. Memory Leaks and Performance Debugging
import time

def efficient_function():
    return [i * 2 for i in range(100000)]  # Used list comprehension for efficiency

print(len(efficient_function()))

# 9. Unexpected None
def add(a, b):
    result = a + b
    return result  # Fixed: Added return statement

print(add(3, 4))

# 10. Silent Failures
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Handled division by zero error")  # Explicitly handle errors

print("No error detected!")
