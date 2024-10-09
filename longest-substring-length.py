def long_repeat(line):
    max_length = 0
    current_length = 1
    if not line:
        return 0
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
    if current_length > max_length:
        max_length = current_length
    return max_length
print(long_repeat('sdsffffse'))
print(long_repeat('ddvvrwwwrggg'))
