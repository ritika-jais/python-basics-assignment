import csv
import json

def convert_to_json(input_file, output_file): 
        
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)  
            students = list(reader) 
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(students, outfile, indent=4)  

        print(f" Conversion completed! Data saved to: {output_file}")

    
if __name__ == "__main__":
   
    input_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\students.txt"
    output_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\students.json"
    
    
    convert_to_json(input_file, output_file)
