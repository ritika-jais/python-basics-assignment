# main.py

# Importing the module
import side_effects  # This will automatically print "This runs on import!"

# Calling the function inside the module
side_effects.greet()

#Top-level code in a module runs on import:

#The print("This runs on import!") statement in side_effects.py executes as soon as the module is imported.
#Functions and classes do not execute on import:

#The greet() function does not run unless explicitly called.
#Modules are only executed once per program run:

#If side_effects is imported multiple times in different files, Python caches the module and does not re-execute the print statement unless explicitly reloaded using importlib.reload().