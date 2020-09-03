# Get input from user (a int)

# Check if the input is bigger then the previous biggest input
# While input from user is not negative we contine to ask for anther number and check if bigger
# When the input is a negative number stop the loop

# Print maximum positive integer 


num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
