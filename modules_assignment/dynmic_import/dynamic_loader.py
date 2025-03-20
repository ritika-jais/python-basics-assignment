#Enter module name: math
#Enter function name: factorial
#Enter argument: 5
#Output: 120

import importlib  # Importing importlib for dynamic module loading

def dynamic_import_and_execute():
    """
    Dynamically imports a module, retrieves a function, and executes it with user input.
    """
    try:
        # Step 1: Get the module name from the user
        module_name = input("Enter module name: ").strip()

        # Step 2: Dynamically import the module
        module = importlib.import_module(module_name)

        # Step 3: Get the function name from the user
        function_name = input("Enter function name: ").strip()

        # Step 4: Check if the function exists in the module
        if not hasattr(module, function_name):
            print(f"Error: Function '{function_name}' not found in module '{module_name}'.")
            return

        # Step 5: Retrieve the function from the module
        func = getattr(module, function_name)  

        # Step 6: Get the argument from the user
        arg = input("Enter argument: ").strip()

        # Step 7: Convert the argument to an integer (since factorial requires an int)
        try:
            arg = int(arg)  # Convert to integer
        except ValueError:
            print("Error: Please enter a valid integer argument.")
            return

        # Step 8: Execute the function and display the result
        result = func(arg)
        print("Output:", result)

    except ModuleNotFoundError:
        print("Error: Module not found. Please enter a valid module.")
    except TypeError:
        print("Error: Invalid number of arguments for the function.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

# Run the function
dynamic_import_and_execute()
