def end_other(a, b):
    a = a.lower()
    b = b.lower()

    large_str = a # a is the largest string
    short_str = b # b is the shortest string

    if len(b) > len(a):
        large_str = b
        short_str = a
    if short_str == large_str[len(large_str) - len(short_str): len(large_str)]:
        return True
    return False
