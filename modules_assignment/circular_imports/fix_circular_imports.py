def func_a():
    return "Function A"

def call_func_b():
    import module_b  # Import moved inside function
    return module_b.func_b()

print(call_func_b())  # Works fine now


