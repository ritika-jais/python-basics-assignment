import os

def list_files_in_directory(directory_path):
    try:
        
        files = os.listdir(directory_path)
        
       
        filtered_files = [file for file in files if file.endswith(('.txt', '.csv'))]

        if filtered_files:
            print(f"Found .txt and .csv files in '{directory_path}':\n")
            for file in filtered_files:
                print(file)
        else:
            print(f"No .txt or .csv files found in '{directory_path}'.")
    except FileNotFoundError:
        print(f" Directory not found: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    directory_path = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling"
    
   
    list_files_in_directory(directory_path)
