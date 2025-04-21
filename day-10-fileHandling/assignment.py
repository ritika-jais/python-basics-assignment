#Beginner-Level Questions (Concept + Code)

#1 Open and Read File
#Write a Python program to read a file notes.txt and print its contents line-by-line.

try:
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\notes.txt", "r") as file:

        
        for line in file:
            print(line.strip())  
except FileNotFoundError:
    print("The file 'notes.txt' was not found.")

#2 Count Lines in a File
#Count how many lines exist in a file poem.txt. begginer level progra

line_count = 0


try:
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\poem.txt", "r") as file:
        
        for line in file:
            line_count += 1

    print("Total number of lines:", line_count)

except FileNotFoundError:
    print("The file 'poem.txt' was not found.")

#3 Write to a File
#Create a new file reminder.txt and write 5 tasks to it, one per line    

with open("reminder.txt", "w") as file:
    print("Enter 5 tasks:")
    for i in range(1, 6):
        task = input(f"Task {i}: ")
        file.write(task + "\n")  

print("All tasks saved to 'reminder.txt'.")

#4 Append to a File
#Add a new task to reminder.txt without deleting existing ones.

with open("reminder.txt", "a") as file:
    task = input("Enter a new task to add: ")
    file.write(task + "\n")  

print(" all Task added to 'reminder.txt'.")

#5 Check File Exists
#Use os.path.exists() to check if data.txt exists before opening.

import os

if os.path.exists("data.txt"):
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\data.txt") as file:
        print("File contents:")
        print(file.read())
else:
    print(" file 'data.txt' does not exist.")


#Intermediate-Level Questions

#6 Remove Blank Lines
#Write a program that reads input.txt and creates cleaned.txt with no empty lines.    

try:
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\input1.txt") as infile, open("cleaned.txt", "w") as outfile:
        for line in infile:
            if line.strip():  
                outfile.write(line)

    print("Blank lines removed. Output saved in 'cleaned.txt'.")

except FileNotFoundError:
    print("The file 'input1.txt' does not exist.")

#7 Find and Replace
#Search and replace the word “Python” with “PYTHON” in article.txt.    

try:
    
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\article.txt") as file:
        content = file.read()

    updated_content = content.replace("Python", "PYTHON")

    with open("article.txt", "w") as file:
        file.write(updated_content)

    print(" 'Python' replaced with 'PYTHON'.")

except FileNotFoundError:
    print("The file 'article.txt' does not exist.")

#8 Uppercase Writer
#Read a file and write its contents in all uppercase to output.txt.    

try:
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\input.txt") as infile:
        content = infile.read()

    upper_content = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(upper_content)

    print(" 'output.txt' converted in uppercase.")

except FileNotFoundError:
    print("The file 'input.txt' does not exist.")

#9 Student Report Generator
#Read students.txt containing Name,Marks, calculate and save the pass/fail status in report.txt (Pass if Marks ≥ 50).

try:
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\students.txt") as infile, open("report.txt", "w") as outfile:
        for line in infile:
            line = line.strip()
            if line:  
                name, marks = line.split(",")
                marks = int(marks.strip())
                status = "Pass" if marks >= 50 else "Fail"
                outfile.write(f"{name} - {status}\n")

    print("Student report in 'report.txt'.")

except FileNotFoundError:
    print("The file 'students.txt' does not exist.")

#10 Reverse File Lines
#Reverse the order of lines in quotes.txt and write to reversed_quotes.txt.

try:
    with open(r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\quotes.txt") as infile:
        lines = infile.readlines()

    lines.reverse()

    with open("reversed_quotes.txt", "w") as outfile:
        outfile.writelines(lines)

    print("reversed and written to 'reversed_quotes.txt'.")

except FileNotFoundError:
    print("The file 'quotes.txt' does not exist.")

