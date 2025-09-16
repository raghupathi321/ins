from pwn import remote
from Crypto.Cipher import AES
import binascii

# Server details
host = "codefest-ctf.iitbhu.tech"
port = 40451

# Connect to the service
conn = remote(host, port)

# Fetch the initial prompt
welcome_msg = conn.recvline().decode()
print(welcome_msg)

# Fetch the encrypted flag
conn.recvuntil(b"Encrypted Flag: ")
encrypted_flag = conn.recvline().strip().decode()
print(f"Encrypted Flag: {encrypted_flag}")

# Split ciphertext into 16-byte blocks
cipher_blocks = [encrypted_flag[i:i+32] for i in range(0, len(encrypted_flag), 32)]

# Oracle to decrypt using controlled IVs
def decrypt_block(block, iv):
    # Combine IV and ciphertext for submission
    payload = iv + block
    conn.sendline(payload.hex())
    response = conn.recvline().strip()
    return response.decode()

# Reconstruct the plaintext
flag = b""
for block in cipher_blocks:
    iv = b"\x00" * 16  # Controlled IV
    decrypted = decrypt_block(bytes.fromhex(block), iv)
    flag += bytes.fromhex(decrypted)

print(f"Flag: {flag.decode()}")

# Close the connection
conn.close()

