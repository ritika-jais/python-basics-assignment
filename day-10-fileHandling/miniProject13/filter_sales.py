import csv

input_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject13\sales.csv"
output_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject13\high_sales.csv"

def filter_high_sales(input_file, output_file, threshold=10000):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()

        print(f"Sales above ₹{threshold}:\n")
        for row in reader:
            try:
                amount = float(row['Amount'])
                if amount > threshold:
                    writer.writerow(row)
                    print(row)
            except ValueError:
                print(f"Skipping invalid row: {row}")

if __name__ == "__main__":
    filter_high_sales(input_file, output_file)
