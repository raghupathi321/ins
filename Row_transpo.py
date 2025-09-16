def row_trans_encrypt(text, key):
    row_len = len(key)
    rows = [text[i:i+row_len].ljust(row_len, 'X') for i in range(0, len(text), row_len)]
    return ''.join(rows[i-1] for i in key)

def row_trans_decrypt(cipher, key):
    row_len = len(key)
    rows = [cipher[i:i+row_len] for i in range(0, len(cipher), row_len)]
    grid = ["" for _ in range(len(rows))]
    for i, k in enumerate(key):
        grid[k-1] = rows[i]
    return ''.join(grid).rstrip('X')


# Example
msg = "HELLOTRANSPOSITION"
key = [3, 1, 4, 2, 5]

enc = row_trans_encrypt(msg, key)
dec = row_trans_decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)
