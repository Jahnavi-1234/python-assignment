# It prints max and min elements
def find_max_min(lst):
    if not lst:   # If the input line is empty, return None
        return None
    max_num = lst[0]  # Assuming first element is Max
    min_num = lst[0]  # Assuming first element is Min
    for num in lst:   # Looping over the elements
        if num > max_num:
            max_num = num  # If the number is greater than the initial number then update the max_num
        if num < min_num:
            min_num = num  # If the number is less than the initial number then update the min_num
    return max_num, min_num # It returns the max_num and min_num
lst = [93, 994, 62, 334, 603, 381, 116, 840, 841, 111, 994]
max_value, min_value = find_max_min(lst)
print("Max:", max_value)    # Max: 994
print("Min:", min_value)    # Min: 62














