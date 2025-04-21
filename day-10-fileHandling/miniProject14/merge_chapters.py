def merge_chapters(chapter_files, output_file):
    with open(output_file, 'w') as outfile:
        for chapter in chapter_files:
            try:
                with open(chapter, 'r') as infile:
                    content = infile.read()
                    outfile.write(content + "\n\n")  
                    print(f"Merged: {chapter}")
            except FileNotFoundError:
                print(f"File not found: {chapter}")
    
    print(f"\n All available chapters merged into: {output_file}")

if __name__ == "__main__":
    chapter_files = [
         r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject14\chapter1.txt",
        r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject14\chapter2.txt",
        r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniProject14\chapter3.txt"
    ]
    output_file = r"full_book.txt"
    merge_chapters(chapter_files, output_file)
