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

img = Image.open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-7 Iteration\example.jpg")
inverted_img = ImageOps.invert(img.convert("RGB"))  
inverted_img.show()
inverted_img.save("inverted_example.jpg")


for i in range(5):
    print(i)
    i=i+2




A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

def matrix_multiply(A, B):
    
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    
    if cols_A != rows_B:
        raise ValueError("Number of columns in A = number of rows in B")

    
    result = [[0] * cols_B for _ in range(rows_A)]

   
    for i in range(rows_A): 
        for j in range(cols_B):  
            # for k in range(cols_A):  
                result[i][j] += A[i][k] * B[k][j]  
    return result


result = matrix_multiply(A, B)
for row in result:
    print(row)