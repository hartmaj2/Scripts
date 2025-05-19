# Prototype code for generating sequence of labels for google sheets columns

from itertools import product

def generate_excel_column_labels():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Generate single-letter strings
    yield from letters
    
    # Generate two-letter strings and so on
    for length in range(2, 10):  # Adjust the range as needed
        for combination in product(letters, repeat=length):
            yield ''.join(combination)

# Example usage:
sequence = generate_excel_column_labels()

# Print the first 100 elements as an example
for i in range(1000):
    print(f"{i+1} {next(sequence)}")