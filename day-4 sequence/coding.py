#4 Write code to access the last character of a string.

text = "Python"
last_char = text[-1]
print(last_char)  # Output: 'n'

#5 Create a list of numbers and access the third element.

numbers = [10, 20, 30, 40, 50]
third_element = numbers[2]  # Index 2 corresponds to the third element
print(third_element)  # Output: 30

#10 Write code to count the occurrences of an element in a list.

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
count_of_2 = numbers.count(2)  # Counts occurrences of 2
print(count_of_2)  # Output: 4

#13 Write code to split the sentence: "Learn Python, step by step!" into words.

sentence = "Learn Python, step by step!"
words = sentence.split()  # Splits by spaces (default)
print(words)

#14 Join a list ['Python', 'is', 'fun'] into a single string.

words = ['Python', 'is', 'fun']
sentence = " ".join(words)  # Joins words with a space separator
print(sentence)

#15 Given a list numbers = [1, 2, 2, 3, 4, 2], find the index of the first 2.

numbers = [1, 2, 2, 3, 4, 2]
first_index = numbers.index(2)  # Finds the first occurrence of 2
print(first_index)

#16 Write code to check if a string is a palindrome.

def is_palindrome(s):
    s = s.lower()  # Convert to lowercase to ignore case sensitivity
    return s == s[::-1]  # Compare the string with its reverse

# Example usage
word = "madam"
print(is_palindrome(word))  # Output: True

word = "hello"
print(is_palindrome(word))  # Output: False

#17 Implement a function that returns the length of the longest word in a sentence.

def longest_word_length(sentence):
    words = sentence.split()  # Split sentence into words
    return max(len(word) for word in words)  # Find the longest word length

# Example usage
sentence = "Python programming is amazing"
print(longest_word_length(sentence))  # Output: 11 (programming)

#19 How do you convert a list of characters into a string?

#You can convert a list of characters into a string using the join() method.

char_list = ['H', 'e', 'l', 'l', 'o']
string = "".join(char_list)  # Joins characters without spaces
print(string)

#20 Write code to remove duplicates from a list while preserving order.

#Using a Loop and a Set (Efficient & Simple)

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# Example usage
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)

#Output

[1, 2, 3, 4, 5]
#Explanation
#seen is a set that keeps track of encountered elements.
#The list comprehension ensures each element is added only once while maintaining order.

#21 Write a function that takes a list of tuples and sorts it by the second element of each tuple

def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])  # Sort by second element

# Example usage
tuples_list = [(1, 3), (2, 1), (4, 2), (3, 5)]
sorted_list = sort_by_second_element(tuples_list)
print(sorted_list)

#sorted(lst, key=lambda x: x[1]) sorts the list by the second element (x[1]) of each tuple.
#The default sort order is ascending.

#22 Implement a program to flatten a nested list of arbitrary depth.

def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))  # Recursively flatten sublists
        else:
            flattened.append(item)  # Append non-list items directly
    return flattened

# Example usage
nested_list = [1, [2, [3, 4], 5], [6, [7, [8, 9]]]]
print(flatten_list(nested_list))

#23 Create a function that rotates a list to the right by k steps.

# We can rotate a list to the right by k steps using slicing 

def rotate_right(lst, k):
    k = k % len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]  # Slice and concatenate

# Example usage
numbers = [1, 2, 3, 4, 5]
rotated = rotate_right(numbers, 2)
print(rotated)  # Output: [4, 5, 1, 2, 3]

#lst[-k:] → Gets the last k elements.
#lst[:-k] → Gets the remaining elements.
#Concatenation (+) shifts elements to the right.

#24 Given two strings, write a function that returns True if they are anagrams.

#We can check if two strings are anagrams (i.e., contain the same characters in a different order) using sorting or Counter from collections.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)  # Sort both and compare

# Example usage

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False

#Explanation
#sorted(str1) and sorted(str2) rearrange the letters in ascending order.
#If both sorted strings are identical, they are anagrams.

#25 Create a function to split a list into chunks of a specified size.

def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)] #Uses a list comprehension with range(0, len(lst), size).
                                                                #Slices the list from i to i + size.

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(chunk_list(numbers, 3))

#26 Implement a function that merges two sorted lists into one sorted list.

# Two-Pointer Approach (Efficient - O(n + m))

def merge_sorted_lists(lst1, lst2):
    merged = []
    i, j = 0, 0  # Pointers for both lists

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1

    # Add remaining elements from both lists
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])

    return merged

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_lists(list1, list2))


