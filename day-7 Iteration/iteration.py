#1 For Loop Basics: Write a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)

#2 String Iteration: Write a program that counts vowels in a string.

vowels = "a", "e", "i","o","u", "A", "E","I","O","U"
str = " I saw an elephant today"
count = 0
for i in str:
    if i in vowels:
        count+=1

print("No .of vowels=" ,count)        

#3 Accumulator Pattern: Calculate the sum of squares from 1 to 100.

acc=0
for i in range(1,101):
    acc+=i**2

print(acc)    

#4 Nested Loops: Create a multiplication table up to 10x10.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4}",end = " ")
    print()

#5 Image Processing: Use PIL to invert the colors of an image.

from PIL import Image, ImageOps

# Open the image
img = Image.open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-7 Iteration\example.jpg")


# Invert the image colors
inverted_img = ImageOps.invert(img.convert("RGB"))  # Ensure it's in RGB mode before inverting

# Show the inverted image
inverted_img.show()

# Save the inverted image
inverted_img.save("inverted_example.jpg")


