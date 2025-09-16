def simple_columnar_encrypt(plain_text, key):
    n = len(key)
    rows = (len(plain_text) + n - 1) // n  # Ceiling division
    grid = [['X' for _ in range(n)] for _ in range(rows)]
    
    # Fill the grid row by row
    idx = 0
    for r in range(rows):
        for c in range(n):
            if idx < len(plain_text):
                grid[r][c] = plain_text[idx]
                idx += 1

    # Read columns in key order
    cipher_text = ''
    for col_num in key:
        col_idx = col_num - 1
        for r in range(rows):
            cipher_text += grid[r][col_idx]

    return cipher_text


def simple_columnar_decrypt(cipher_text, key):
    n = len(key)
    rows = (len(cipher_text) + n - 1) // n
    grid = [['' for _ in range(n)] for _ in range(rows)]

    idx = 0
    # Fill the grid column by column in key order
    for col_num in key:
        col_idx = col_num - 1
        for r in range(rows):
            grid[r][col_idx] = cipher_text[idx]
            idx += 1

    # Read grid row by row
    plain_text = ''
    for r in range(rows):
        for c in range(n):
            plain_text += grid[r][c]

    return plain_text.rstrip('X')  # Remove padding


# Example Usage
message = "HELLOCOLUMNARTRANSPOSITION"
key = [3, 1, 4, 2]  # Example key (column permutation)

# First Iteration
encrypted_once = simple_columnar_encrypt(message, key)

# Second Iteration
encrypted_twice = simple_columnar_encrypt(encrypted_once, key)

# Decryption (reverse order)
decrypted_once = simple_columnar_decrypt(encrypted_twice, key)
decrypted_twice = simple_columnar_decrypt(decrypted_once, key)

print(f"Original Message: {message}")
print(f"After 1st Encryption: {encrypted_once}")
print(f"After 2nd Encryption: {encrypted_twice}")
print(f"After 1st Decryption: {decrypted_once}")
print(f"After 2nd Decryption (Recovered): {decrypted_twice}")
