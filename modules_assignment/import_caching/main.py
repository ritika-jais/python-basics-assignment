# main.py

import sys
import mmymodule  # First import will execute the print statement in mymodule

# Check if mymodule is cached in sys.modules
print(sys.modules['mmymodule'])  # Should print the module object reference

# Call a function from the module
mmymodule.greet()


#First Line: "mymodule has been imported!" → Runs only once because the module is loaded into sys.modules.
#Second Line: The module reference (<module 'mymodule' from '...' >) confirms that sys.modules stores the module.
#Third Line: Hello from mymodule! → Comes from calling greet().