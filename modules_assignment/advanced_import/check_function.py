import importlib

def execute_function(module_name, function_name, *args):

    try:
        # Step 1: Dynamically import the module
        module = importlib.import_module(module_name)

        # Step 2: Check if the function exists in the module
        if not hasattr(module, function_name):
            print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
            return

        # Step 3: Retrieve and execute the function
        func = getattr(module, function_name)
        result = func(*args)  # Execute function with provided arguments
        print("Output:", result)

    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except TypeError:
        print("Error: Invalid number of arguments for the function.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Example usage
module_name = input("Enter module name: ").strip()
function_name = input("Enter function name: ").strip()
args = input("Enter arguments (comma-separated): ").split(",")

# Convert numeric arguments if possible
processed_args = []
for arg in args:
    arg = arg.strip()
    try:
        processed_args.append(float(arg) if '.' in arg else int(arg))  # Convert to number if possible
    except ValueError:
        processed_args.append(arg)  # Keep as string if conversion fails

execute_function(module_name, function_name, *processed_args)
