#1 Data Pipeline Validator

#Task: Identify the longest pipeline and return pipelines taking more than a given threshold time.
pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]

threshold = 40
# Finding the longest pipeline
longest_pipeline = max(pipelines, key=lambda x: x[1])[0]

# Finding pipelines exceeding the threshold
exceeding_pipelines = [name for name, time in pipelines if time > threshold]

# Output
print("Longest Pipeline:", longest_pipeline)
print("Pipelines exceeding threshold:", exceeding_pipelines)

#2 Log File Parser

#Task: Extract unique error codes from a log file.
import re

logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""

# Extracting error codes using regex
error_codes = set(re.findall(r'ERROR (\d+)', logs)) #(re.findall): Extracts all error codes appearing after ERROR.,(set()): Ensures uniqueness.

# Converting set to sorted list
unique_error_codes = sorted(error_codes) #(sorted()): Provides a structured output.

# Output
print("Unique Error Codes:", unique_error_codes)

#3 Config File Reader

#Task: Parse key-value pairs from a configuration string.

config = "host=127.0.0.1;port=8080;mode=debug"

# Splitting by ';' to get key-value pairs
pairs = [tuple(pair.split("=")) for pair in config.split(";")]

# Output
print(pairs)

#4 Social Media Data Cleaner

#Task: Extract unique hashtags from a social media post.

import re

post = "Loving the new #Python course! #Coding #Python #Learning"

# Using regex to find all hashtags
hashtags = re.findall(r"#\w+", post) # regex (#\w+): Finds all words starting with #.

# Removing duplicates while preserving order
unique_hashtags = list(dict.fromkeys(hashtags))  # dict.fromkeys() to maintain order.
 
# Output
print(unique_hashtags)

# 5 Secret Code Decoder

#Task: Extract every third character from a string.

# Secret Code Decoder
# Task: Extract every third character from a string in order.

# Input secret message
secret_message = "hweoll rorlwd"

# Extract every third character using slicing
decoded_message = secret_message[::3]

# Output the decoded message
print(decoded_message)  # Expected Output: 'hello world'

#6 Inventory Tracker

#Task: Find the product with the highest quantity.

# Inventory list with product names and their respective quantities
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]

# Finding the product with the highest quantity using max() and lambda function
highest_quantity_product = max(inventory, key=lambda item: item[1])[0]

# Output the result
print(highest_quantity_product)  # Expected Output: 'Oranges'

#7 Survey Data Analyzer

#Task: Extract scores from a survey string and find min/max.

# Given survey data as a string
survey_data = "5,3,4,1,2"

# Convert string to a list of integers
scores = list(map(int, survey_data.split(',')))

# Find the maximum and minimum scores
max_score = max(scores)
min_score = min(scores)

# Output the results
print(f"Max Score: {max_score}, Min Score: {min_score}")

#8 Access Control Manager

#Task: Manage user access levels using lists and tuples.

# Given users and roles
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")

# Assign roles to users using zip
for user, role in zip(users, roles): # zip -makes pair 
    print(f"{user}: {role}")

#9 Customer Support Ticket System

#Task: Categorize tickets based on message length.

#Categories are determined by message length:
#Short: 0–20 characters
#Medium: 21–50 characters
#Long: More than 50 characters

def categorize_ticket(message):
    length = len(message)
    
    if length <= 20:
        category = "Short"
    elif 21 <= length <= 50:
        category = "Medium"
    else:
        category = "Long"
    
    return f"Category: {category}"

# Example Input
message = "My account is locked, please help!"
print(categorize_ticket(message))

#10 Product Catalog Manager

#Task: Find the product with the longest name.

def find_longest_product(products):
    return max(products, key=len)

# Example Input
products = ["Laptop", "Smartphone", "Wireless Headphones"]
print(find_longest_product(products))

#11 Sensor Data Analyzer
#Task: Extract the last 10 sensor readings and calculate the average.

def analyze_sensor_data(sensor_readings):
    last_10_readings = sensor_readings[-10:]  # Extract last 10 readings
    average = sum(last_10_readings) / len(last_10_readings)  # Calculate average
    return round(average)  # Round to nearest whole number

# Example Input
sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
print("Average:", analyze_sensor_data(sensor_readings))

#12 Transaction Reverser
#Task: Reverse the list of transactions.

def reverse_transactions(transactions):
    return transactions[::-1]  # Reverse the list

# Example Input
transactions = [100, -50, 200, -150, 50]
print(reverse_transactions(transactions))

#13 Log Formatter
#Task: Format logs with timestamps.

def format_logs(logs, timestamp):
    return [f"{timestamp} - {log}" for log in logs]  #he formatted log messages are returned as a new list.

# Example Input
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"

# Function Call
formatted_logs = format_logs(logs, timestamp)

# Output
for log in formatted_logs:
    print(log)

#14 Pattern Generator
#Task: Generate patterns with repetition.

def generate_pattern(symbol, count):
    """
    Generates a pattern by repeating the given symbol a specified number of times.
    
    Parameters:
    symbol (str): The character to be repeated.
    count (int): The number of times the symbol should be repeated.
    
    Returns:
    str: The generated pattern.
    """
    return " ".join([symbol] * count)

# Example Usage
symbol = "*"
count = 5

# Generate and print the pattern
pattern = generate_pattern(symbol, count)
print(pattern)

#15 Customer Feedback Analyzer
#Task: Count keyword occurrences.

feedback = "The product is excellent, absolutely excellent!"

# Remove punctuation manually
clean_feedback = feedback.replace(",", "").replace("!", "")

# Split into words
words = clean_feedback.split()

# Count occurrences
word_count = words.count("excellent")

print(f"'excellent' count: {word_count}")

#16 Sentence Index Finder
#Task: Find the index of the first occurrence of "error".

log = "INFO: All systems go.ERROR: Failed to start service."

# Convert to lowercase to handle case-insensitivity
index = log.lower().find("error")

print(f"Index: {index}")

#17 CSV Parser
#Task: Parse CSV data into lists.

csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"

# Splitting rows by newline ('\n')
rows = csv_data.split("\n")

# Splitting each row by comma (',') to get individual values
parsed_data = [row.split(",") for row in rows]

print(parsed_data)

#18 Username Generator
#Task: Generate usernames from full names.

names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]

# Generating usernames by taking the first letter of the first name and appending the last name
usernames = [name.split()[0][0] + name.split()[1] for name in names]

print(usernames)

#19 Chat Log Analyzer
#Task: Count messages per user from chat logs.

from collections import defaultdict

chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]

# Dictionary to store message counts
message_count = defaultdict(int)

# Counting messages per user
for log in chat_logs:
    user, _ = log.split(": ", 1)  # Splitting by ': ' to get the username
    message_count[user] += 1

# Displaying output
for user, count in message_count.items():
    print(f"{user}: {count} messages")

#20 Data Compressor
#Task: Compress recurring substrings.

def compress_data(data):
    n = len(data)
    
    # Try to find the smallest repeating substring
    for i in range(1, n // 2 + 1):  # Check for repeating patterns of length i
        substring = data[:i]  # Take first i characters
        if data == substring * (n // i):  # Check if it repeats to form the full string
            return f"'{substring}' repeated {n // i} times"
    
    return "No repeating pattern found"

# Example input
data = "abababababab"
output = compress_data(data)
print(output)








