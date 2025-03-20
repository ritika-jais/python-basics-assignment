#for SINGLE IMPORT

import time

start = time.time()
import math  # Importing only one module
end = time.time()

print(f"Single Import Time: {end - start:.6f} seconds")

#for IMPORTING MULTIPLE MODULES AT ONCE

start = time.time()
import math, os, sys, random, datetime  # Importing multiple modules at once
end = time.time()

print(f"Multiple Import Time: {end - start:.6f} seconds")

#IMPORTING EVERYTHING

start = time.time()
from math import *  # Importing all functions from math
end = time.time()

print(f"Wildcard Import Time: {end - start:.6f} seconds")

