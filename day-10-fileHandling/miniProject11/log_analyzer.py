def analyze_log(input_log_file, error_log_file):
    error_count = 0
    error_lines = []

   
    with open(input_log_file, 'r') as infile:
        for line in infile:
            if "ERROR" in line:
                error_count += 1
                error_lines.append(line)

    
    with open(error_log_file, 'w') as outfile:
        outfile.writelines(error_lines)

    print(f"Total 'ERROR' entries found: {error_count}")
    print(f"All 'ERROR' lines written to: {error_log_file}")


if __name__ == "__main__":
    
    input_log_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject11\server.log"
    error_log_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject11\errors_only.log"

    analyze_log(input_log_file, error_log_file)
