#   Q1-  Write a function that takes a list of tuples, each containing (department, employee, salary), and returns a dictionary with departments as keys and a list of (employee, salary) sorted by salary descending.

from collections import defaultdict

def group_by_department(data):
    result = defaultdict(list)
    for dept, emp, salary in data:
        result[dept].append((emp, salary))
    
    
    for dept in result:
        result[dept].sort(key=lambda x: x[1], reverse=True)
    
    return dict(result)

data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]
print(group_by_department(data))


# Q2- **Inverted Index**

#Create a dictionary from a list of sentences that maps each word to the indices of the sentences it appears in

from collections import defaultdict

def inverted_index(sentences):
    index = defaultdict(set)
    
    for i, sentence in enumerate(sentences):
        for word in sentence.split():
            index[word].add(i)
    
    return {word: sorted(list(indices)) for word, indices in index.items()}


sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
print(inverted_index(sentences))

# Q3. **Deep Copy Trap**
#Demonstrate a scenario where using `dict.copy()` fails due to nested structures. Show how `deepcopy` fixes it.

import copy

original = {'a': [1, 2], 'b': [3, 4]}

# Shallow copy
shallow_copy = original.copy()
shallow_copy['a'].append(999)

print("Original after shallow copy change:", original)

# Deep copy
original = {'a': [1, 2], 'b': [3, 4]}
deep_copy = copy.deepcopy(original)
deep_copy['a'].append(999)

print("Original after deep copy change:", original)

# **Q4. Accumulate Word Lengths**
# Write a program that takes a list of words and creates a dictionary where the key is the length of the word, and the value is a list of words of that length.

from collections import defaultdict

def group_words(words):
    result = defaultdict(list)
    for word in words:
        result[len(word)].append(word)
    return dict(result)


words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
print(group_words(words))

# **Q5. Dictionary Merge with Conflict Resolution**
# Given two dictionaries, merge them such that:

#- If keys are unique, include both.
#- If keys conflict, take the larger value.

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] = max(result[key], value)
        else:
            result[key] = value
    return result

d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}
print(merge_dicts(d1, d2))



