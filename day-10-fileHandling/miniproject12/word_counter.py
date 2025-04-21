import re
from collections import defaultdict


input_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniproject12\story.txt"
output_file = r"C:\Users\91881\OneDrive\Documents\PYTHON_TRAINING\python-basics-assignment\day-10-fileHandling\miniproject12\frequency.txt"

def count_word_frequency(input_file, output_file):
    word_freq = defaultdict(int)

   
    with open(input_file, 'r') as f:
        for line in f:
            words = re.findall(r'\b\w+\b', line.lower()) 
            for word in words:
                word_freq[word] += 1

    
    sorted_freq = dict(sorted(word_freq.items()))

    
    with open(output_file, 'w') as f:
        for word, count in sorted_freq.items():
            f.write(f"{word}: {count}\n")

    print(f"Word frequency written to: {output_file}")


if __name__ == "__main__":
    count_word_frequency(input_file, output_file)
