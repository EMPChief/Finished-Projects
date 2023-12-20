# Open the file in read mode
with open('train_data.csv', 'r') as file:
    # Read and print each line
    for line in file:
        print(line.strip())  # Use strip() to remove leading/trailing whitespaces
