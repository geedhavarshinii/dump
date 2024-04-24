def apply_table(inp, table):
    res = ""
    for i in table:
        res += inp[i-1]
    return res

def left_shift(data):
    return data[1:]+data[0]

if __name__ == "__main__":
    key = input("Enter 10 bit key: ")
    msg = input("Enter 8 bit msg: ")
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

    temp = apply_table(key, p10)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = apply_table(left+right, p8)
    print(f"key 1 is {key1}")
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = apply_table(left+right, p8)
    print(f"key 2 is {key2}")
    
