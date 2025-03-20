# Sequences in Python

## 1. Define a sequence. What types of sequences exist in Python?

**Ans.** A sequence is a data structure that contains items arranged in order, and you can access each item using an integer index that represents its position in the sequence. You can always find the length of a sequence.

### Types of sequences in Python:
1. **String (str)**
   - A sequence of characters.
   - Immutable (cannot be changed after creation).
   - **Example**: 
     s = "Hello"  
     print(s[1])  # Output: 'e'

2. **List (list)**
   - A sequence of elements of any data type.
   - Mutable (can be modified).
   - **Example**: 
     lst = [1, 2, 3, "Python"]  
     lst.append(4)  # Modifying the list

3. **Tuple (tuple)**
   - Similar to a list but immutable.
   - **Example**: 
     t = (10, 20, 30)  
     print(t[0])  # Output: 10

4. **Range (range)**
   - Represents an immutable sequence of numbers.
   - Commonly used for loops.
   - **Example**: 
     r = range(1, 10, 2)  # Generates numbers from 1 to 9 with step 2  
     print(list(r))  # Output: [1, 3, 5, 7, 9]

## 2. How are strings, lists, and tuples different from each other?

**Ans.** Differences Between Strings, Lists, and Tuples in Python:

1. **Definition**
   - **String (str)**: A sequence of characters.
   - **List (list)**: A sequence of elements of any type.
   - **Tuple (tuple)**: A sequence of elements of any type.

2. **Mutability**
   - **String**: Immutable (cannot be modified after creation).
   - **List**: Mutable (can be modified).
   - **Tuple**: Immutable (cannot be modified after creation).

3. **Syntax**
   - **String**: "hello" or 'hello'
   - **List**: [1, 2, 3]
   - **Tuple**: (1, 2, 3)

4. **Modification**
   - Strings cannot be changed in place.
   - Lists allow adding, removing, and modifying elements.
   - Tuples do not allow element modifications.

5. **Performance**
   - Strings are faster than lists because they are immutable.
   - Lists are slower due to dynamic resizing.
   - Tuples are faster than lists because they are immutable.

6. **Memory Usage**
   - Strings use memory efficiently.
   - Lists take up more memory due to dynamic resizing.
   - Tuples use less memory than lists.

7. **Use Cases**
   - **Strings**: Storing text, names, messages.
   - **Lists**: Dynamic collections that change over time.
   - **Tuples**: Fixed collections that should remain unchanged.

## 3. Explain how indexing works in Python with an example.

**Ans.** Indexing in Python refers to accessing individual elements of a sequence (like a string, list, or tuple) using their position (index). Python uses zero-based indexing, meaning the first element is at index 0, the second at 1, and so on. Python also supports negative indexing, where -1 refers to the last element, -2 to the second last, and so on.

### Indexing Examples

1. **Indexing in Strings**
   - text = "Python"
   - print(text[0])   # Output: 'P' (First character)
   - print(text[-1])  # Output: 'n' (Last character)

2. **Indexing in Lists**
   - numbers = [10, 20, 30, 40, 50]
   - print(numbers[2])    # Output: 30 (Third element)
   - print(numbers[-2])   # Output: 40 (Second last element)

3. **Indexing in Tuples**
   - data = (5, 10, 15, 20)
   - print(data[1])   # Output: 10 (Second element)
   - print(data[-3])  # Output: 10 (Third element from last)

## 4. What is the result of `len([1, [2, 3], 4])` and why?

**Ans.** The result of `len([1, [2, 3], 4])` is **3**.

### Explanation
The `len()` function returns the number of top-level elements in a list. In the list `[1, [2, 3], 4]`, the elements are:
- 1 (integer)
- [2, 3] (a nested list, but still counted as a single element)
- 4 (integer)

Since there are three top-level elements, `len()` returns 3.

## 5. Explain slicing with a practical example.

**Ans.** Slicing in Python is a technique used to extract a portion of a sequence (string, list, or tuple) using the slice notation:


- **start**: The index where slicing begins (inclusive).
- **stop**: The index where slicing ends (exclusive).
- **step**: The interval between elements (default is 1).

### Practical Example: Slicing a List

**Extracting a Sublist**
- numbers = [10, 20, 30, 40, 50, 60]
- subset = numbers[1:4]  # Extract elements from index 1 to 3 (4 is excluded)
- print(subset)  # Output: [20, 30, 40]

**Using Negative Indexing**
- numbers = [10, 20, 30, 40, 50, 60]
- subset = numbers[-4:-1]  # Extracts elements from index -4 to -2
- print(subset)  # Output: [30, 40, 50]

## 6. How would you reverse a string using slicing?

**Ans.** We can reverse a string using slicing with a step of -1:
- text = "Python"
- reversed_text = text[::-1]  # Slices the string with step -1 (reverse order)
- print(reversed_text)  # Output: "nohtyP"

## 9. Demonstrate list concatenation and repetition with examples.

**Ans.** 

### List Concatenation (+ Operator)
Concatenation means joining two or more lists to create a new list.

- **Example**: 
  - list1 = [1, 2, 3]
  - list2 = [4, 5, 6]
  - concatenated_list = list1 + list2  # Combines both lists
  - print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

### List Repetition (* Operator)
Repetition means duplicating a list multiple times.

- **Example**: 
  - numbers = [10, 20]
  - repeated_list = numbers * 3  # Repeats the list 3 times
  - print(repeated_list)  # Output: [10, 20, 10, 20, 10, 20]

## 11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?

**Ans.** The given code:
- my_tuple = (1, 2, 3)
- print(my_tuple[1:])

**Output**: 
- (2, 3) 

## 12. Explain the difference between `list.append()` and `list.extend()`.

**Ans.** Both `append()` and `extend()` are used to add elements to a list, but they work differently.

1. **`list.append(item)` → Adds a Single Element (or Object)**
   - The `append()` method adds an entire object as a single element at the end of the list.
   - If you append a list, it will be nested inside the original list.
   - **Example**:
     - numbers = [1, 2, 3]
     - numbers.append([4, 5])  # Appends the entire list as a single element
     - print(numbers)  
     - # Output: [1, 2, 3, [4, 5]]
   - **Explanation**: `[4, 5]` is treated as a single element, not individual numbers.

2. **`list.extend(iterable)` → Adds Multiple Elements Individually**
   - The `extend()` method adds elements from an iterable (list, tuple, string, etc.) individually to the list.
   - Unlike `append()`, it does not create a nested list.
   - **Example**:
     - numbers = [1, 2, 3]
     - numbers.extend([4, 5])  # Adds elements individually
     - print(numbers)  
     - # Output: [1, 2, 3, 4, 5]
   - **Explanation**: The elements 4 and 5 are added separately to the list.

## 18. Demonstrate nested list indexing.

**Ans.** 

### Nested List Indexing in Python
A nested list is a list inside another list. You can access elements using multiple indices.

- **Example Code**:
  - nested_list = [
      [10, 20, 30], 
      [40, 50, 60], 
      [70, 80, 90]
    ]

### Accessing elements
- print(nested_list[0][1])  # Output: 20 (First row, second element)
- print(nested_list[2][0])  # Output: 70 (Third row, first element)
- print(nested_list[1][2])  # Output: 60 (Second row, third element)

### Explanation
- `nested_list[0][1]` → Accesses first row ([10, 20, 30]), then the second element (20).
- `nested_list[2][0]` → Accesses third row ([70, 80, 90]), then the first element (70).
- `nested_list[1][2]` → Accesses second row ([40, 50, 60]), then the third element (60).


