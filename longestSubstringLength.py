#Find the length of the longest substring
def long_repeat(line):
    max_length = 0   # Set the longest repeating length to 0
    current_length = 1   # Start counting the length of the current sequence at 1
    if not line:
        return 0     # If the input line is empty, return 0
    for i in range(1, len(line)):   # Loop through the line starting from the second character
        if line[i] == line[i - 1]:
            current_length += 1      # Increase the count of the current repeating sequence
        else:
            if current_length > max_length:   # If the current sequence is longer than the max found, update max_length
                max_length = current_length
            current_length = 1       # Reset current_length for the new character
    if current_length > max_length:
        max_length = current_length     # After the loop, check if the last sequence is the longest
    return max_length       # Return the length of the longest sequence of repeating characters
print(long_repeat('sdsffffse'))   # Output will be 4
print(long_repeat('ddvvrwwwrggg'))  # Output will be 3
