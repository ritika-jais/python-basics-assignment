# Understanding Circular Imports in Python

A circular import occurs when two or more modules depend on each other. In this case:

- `module_a.py` imports `module_b.py`
- `module_b.py` imports `module_a.py`

This creates a loop, causing an `ImportError` or `AttributeError`.

### Solution
The simplest way to resolve circular imports is by moving the import inside a function rather than at the module level.

---

## Dynamic Module Loading in Python

Python allows importing modules dynamically using `importlib`, which is useful when the module name is not known in advance. This technique is commonly used in plugin systems, script automation, and interactive applications.

```python
import importlib
module = importlib.import_module(module_name)
function = getattr(module, function_name)
function(arguments)
```

---

## Custom Modules Make Code Reusable

A module like `calculator.py` can be used in multiple programs, avoiding redundant code.

### Exception Handling Prevents Crashes
Using `try-except` blocks ensures that errors like division by zero or invalid input don’t stop execution.

### Always Validate User Input
The `try-except` block in `main.py` ensures only numeric inputs are accepted.

### Importing Modules
Use `import module_name` to access functions from another file.

### Using `except Exception as e` for Unknown Errors
This catches unexpected errors and provides useful feedback.

---

## Dynamic Imports
- **Uses `importlib.import_module(module_name)`.**
- **Function Checking – Uses `hasattr(module, function_name)`.**
- **Graceful Error Handling – Prevents crashes due to missing modules or functions.**
- **Flexible Argument Handling – Converts inputs to numbers when applicable.**

---

## Optimizing Import Time in Python

We can measure the import time for different import methods using the `time` module. This helps us analyze which approach is more efficient.

---

## What is `sys.path`?

`sys.path` is a list of directories that Python searches when importing modules.

### By default, it includes:
- The directory of the script being executed.
- Standard library directories.
- Installed third-party package directories.

### Manually Adding a Custom Import Path
If your module is stored in an unconventional location (not in the standard `site-packages` or script directory), you need to manually add the path using:

```python
import sys
sys.path.append("/custom/path/to/module")
```

---

## Understanding Mocking Modules for Testing in Python

Mocking is a technique used in software testing where we replace real objects or functions with mock objects that simulate the behavior of real dependencies. This helps in isolating the unit of code being tested and ensures that tests run in a controlled environment without external dependencies affecting the results.

Python provides the `unittest.mock` module, which allows us to replace parts of our code with mock objects during testing. One common use case is mocking imported modules or functions.

```python
from unittest import mock
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # Output: 100
```

Normally, `math.sqrt(25)` would return `5`, but because of mocking, it returns `100` instead. This demonstrates how we can control external dependencies during testing.

---

## What are Import Side Effects?

In Python, when a module is imported, all the top-level code in that module runs immediately. This is called an **import side effect**—when importing a module causes actions to take place (such as printing, modifying variables, or executing functions) even before explicitly calling any functions or classes from that module.

---

## What is Import Caching?

When a module is imported in Python, it is loaded **only once** per program execution. The module is then stored in `sys.modules`, a dictionary that keeps track of all imported modules. This prevents redundant imports and improves performance.

Once a module is loaded, subsequent imports do not reload it—instead, Python retrieves it from `sys.modules`. If we want to force a module to reload, we need to use:

```python
import importlib
importlib.reload(module)
