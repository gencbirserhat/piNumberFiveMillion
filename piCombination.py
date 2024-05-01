# Create a list to store all 6-digit number combinations
combinations = []
for i in range(1000000):
    num_str = str(i).zfill(6)
    combinations.append(num_str)
    
print("combinations created")

# Open the file containing pi digits
with open("pi5mn.txt", 'r') as file:
    progress = 100
    # Iterate through each line in the file
    for line in file:
        line = line.strip()
        # Iterate through each character in the line to find combinations
        for i in range(len(line) - 5):
            combination = line[i:i+6]
            # Check progress and print status
            if len(combinations)/10000 == progress:
                progress_percentage = 0
                print("progress status {}".format(progress_percentage))
                progress -= 10
                progress_percentage += 10
                print(progress)
            # Remove combination from the list if found
            if combination in combinations:
                combinations.remove(combination)
                print(len(combinations))
                
# Print completion message
print("scanning process completed")

# Write the remaining combinations to a file
with open("results.txt", 'w') as file:
    if (len(combinations) == 0):
        file.write("all 6 digit number combinations available")
    else:
        for item in combinations:
            file.write(str(item) + '\n')
            
# Print completion message
print("result saved")
