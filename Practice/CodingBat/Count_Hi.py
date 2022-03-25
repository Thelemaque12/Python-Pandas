def count_hi(str):
    count = 0
    for i in range(0, len(str)):
        if str[i:i + 2] == 'hi':
            count = count + 1
    return count
