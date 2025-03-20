import sys  # Import the sys module to modify the Python import path

# Add the custom directory to sys.path
custom_path = "C:\\Users\\91881\\custom_modules"
sys.path.append(custom_path)  # Append the path to sys.path

# Now, we can import the module stored in the custom directory
try:
    import mymodule  # Import a module from the newly added path
    print("Module imported successfully!")
except ModuleNotFoundError:
    print(f"Error: Could not find 'mymodule' in {custom_path}")

# Print the sys.path to verify the added path
print("\nCurrent sys.path:")
for p in sys.path:
    print(p)
