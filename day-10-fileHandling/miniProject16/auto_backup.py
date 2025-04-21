import os
from datetime import datetime

def backup_data(source_file, backup_folder):
    
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    current_date = datetime.now().strftime("%Y%m%d")

    backup_file = os.path.join(backup_folder, f"data_backup_{current_date}.csv")

    try:
       
        with open(source_file, 'r') as src:
            data = src.read()

        with open(backup_file, 'w') as dest:
            dest.write(data)

        print(f"Backup successful to: {backup_file}")
    
    except FileNotFoundError:
        print(f"⚠️ File not found: {source_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\data.csv"
    backup_folder = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\backup"
    
    backup_data(source_file, backup_folder)
