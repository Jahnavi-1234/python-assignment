def find_max_min(lst):
    if not lst:
        return None
    max_num = lst[0]
    min_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num
lst = [93, 994, 62, 334, 603, 381, 116, 840, 841, 111, 994]
max_value, min_value = find_max_min(lst)
print("Max:", max_value)
print("Min:", min_value)














