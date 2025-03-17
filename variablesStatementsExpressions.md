# Variables, Statements, and Expressions: A Learning Task

## 2.1. Introduction

### 2.1.1. Learning Goals

By the end of this task, students should be able to:

- Understand the basics of variables, expressions, and statements in Python.
- Differentiate between data types and apply type conversions.
- Properly name variables following Python conventions.
- Grasp the flow of execution through function calls and expressions.
- Update and reassign variables effectively.

### 2.1.2. Objectives

- Identify values and their data types.
- Perform operations using different operators.
- Understand function calls and their role in expressions.
- Explore Python's order of operations.
- Practice variable reassignment and updating.

---

## 2.2. Values and Data Types

1. **Definition:**
   - A value is a piece of data that Python can manipulate.
   - Data types include integers (`int`), floating points (`float`), strings (`str`), and booleans (`bool`).
2. **Example Code:**
   ```python
   x = 42
   y = 3.14
   z = 'Hello'
   print(type(x), type(y), type(z))
   ```

---

## 2.3. Operators and Operands

1. **Definition:**
   - Operators perform operations on values (operands).
   - Types: arithmetic (`+`, `-`, `*`, `/`), comparison (`>`, `<`), logical (`and`, `or`).
2. **Example Code:**
   ```python
   print(5 + 3, 10 - 2, 4 * 2, 9 / 3)
   print(10 > 5, 4 < 2, True and False, True or False)
   ```

---

## 2.4. Function Calls

1. **Definition:**
   - A function call executes a block of reusable code.
2. **Example Code:**
   ```python
   numbers = [5, 3, 8, 1]
   print(max(numbers) - min(numbers))
   ```

---

## 2.6. Type Conversion Functions

1. **Definition:**
   - Convert data types using `int()`, `float()`, `str()`.
2. **Example Code:**
   ```python
   num = '123'
   converted_num = int(num)
   print(converted_num, type(converted_num))
   ```

---

## 2.7. Variables

1. **Definition:**
   - A variable stores a value in memory.
2. **Example Code:**
   ```python
   count = 10
   print(count)
   count = 20
   print(count)
   ```

---

## 2.10. Statements and Expressions

1. **Definition:**
   - An expression produces a value, while a statement performs an action.
2. **Example Code:**
   ```python
   x = 5 + 3
   print(x)
   ```

---

## 2.11. Order of Operations

1. **Definition:**
   - Python follows **PEMDAS** (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).
2. **Example Code:**
   ```python
   result = 2 + 3 * 4 ** 2 / 8
   print(result)
   ```

---

## 2.13. Updating Variables

1. **Definition:**
   - Modify variables using `+=`, `-=`.
2. **Example Code:**
   ```python
   score = 100
   score += 10
   print(score)
   score -= 5
   print(score)
   ```

