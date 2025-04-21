import csv

def sort_csv(input_file, output_file):
    try:
        
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            products = list(reader)  

       
        sorted_products = sorted(products, key=lambda x: float(x['price']))

        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['id', 'name', 'price', 'quantity']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

           
            writer.writeheader()
            
            writer.writerows(sorted_products)

        print(f"Sorting completed! Sorted products saved to: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\products.csv"
    output_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\products_sorted.csv"

    
    sort_csv(input_file, output_file)
