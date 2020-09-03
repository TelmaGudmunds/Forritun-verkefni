# Get input from user (int)

# Make an algorithm that calculates the sequence:; 1, 2, 3, 6, 11, 20, 37, ...
# Next number in sequence is the sum of the previous three numbers

# Print the sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line
next_in_sequence = 0
previous_1 = 2
previous_2 = 1
previous_3 = 0

print(previous_2)
print(previous_1)

for i in range(n-2):
    next_in_sequence = previous_1 + previous_2 + previous_3 # Find the next number in sequence
    previous_1, previous_2, previous_3 = next_in_sequence, previous_1, previous_2 # Find the previous three numbers in sequence

    print(next_in_sequence)

