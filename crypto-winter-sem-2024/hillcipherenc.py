def text_to_numbers(text):
    return [ord(char.upper()) - 65 for char in text if char.isalpha]

def numbers_to_text(numbers):
    return ''.join(chr(num % 26 + 65) for num in numbers)

def key_to_matrix(key, size):
    key_numbers = text_to_numbers(key)
    matrix = []
    index = 0
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(key_numbers[index%len(key_numbers)])
            index+=1
        matrix.append(row)
    return matrix

def matrix_multiply(pt_mat, key_mat):
    result = []
    for row in key_mat:
        value = sum(row[i]*pt_mat[i] for i in range(len(row)))
        result.append(value%26)
    return result

def encrypt(pt, key):
    pt_mat = text_to_numbers(pt)
    key_mat = key_to_matrix(key, len(pt_mat))
    encrypted_nums = matrix_multiply(pt_mat, key_mat)
    return numbers_to_text(encrypted_nums)

plaintext = input("Enter the pt: ")
key = input("Enter the key: ")
encrypted_text = encrypt(plaintext, key)
print(f"Encrypted text is {encrypted_text}")
