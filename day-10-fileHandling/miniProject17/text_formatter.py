def format_text(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
        
        formatted_lines = []
        for line in lines:
            formatted_line = line.strip().replace('\t', '    ')  
            formatted_lines.append(formatted_line)
        
        
        with open(output_file, 'w') as outfile:
            outfile.writelines("\n".join(formatted_lines))
        
        print(f" Text formatting completed! Formatted text saved to: {output_file}")
    
    except FileNotFoundError:
        print(f" File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    input_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\raw_text.txt"
    output_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\formatted_text.txt"

    format_text(input_file, output_file)
