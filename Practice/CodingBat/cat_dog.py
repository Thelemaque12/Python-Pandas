def cat_dog(str):
    cat_count  = 0
    dog_count = 0
    for i in range(0, len(str)):
        if str[i:i + 3] == 'cat':
            cat_count += 1
        if str[i :i + 3] == 'dog':
            dog_count += 1
    return cat_count == dog_count
