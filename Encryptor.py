from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

print('This is an encryption and decryption software.')
print('To encrypt, enter plaintext. To decrypt, enter the encoded ciphertext.')
print('To exit, type "exit".')

# Use a fixed key for testing (replace with secure key management in production)
key = b'\x01' * 16  # Example fixed 16-byte key

while True:
    mode = input('Enter "e" to encrypt or "d" to decrypt (or "exit" to quit): ').strip().lower()
    if mode == 'exit':
        print('Bye Bye! Thank you for using the software.')
        break

    if mode == 'e':  # Encryption mode
        data = input('Enter plaintext to encrypt: ').encode()
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        nonce = cipher.nonce

        # Combine nonce, tag, and ciphertext into a single encoded string
        combined = base64.b64encode(nonce + tag + ciphertext).decode()
        print(f"Encoded Ciphertext: {combined}")

    elif mode == 'd':  # Decryption mode
        try:
            encoded = input('Enter encoded ciphertext: ')
            combined = base64.b64decode(encoded)

            # Extract nonce, tag, and ciphertext
            nonce = combined[:16]
            tag = combined[16:32]
            ciphertext = combined[32:]

            cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            print(f"Decrypted Data: {plaintext.decode()}")
        except (ValueError, KeyError, base64.binascii.Error):
            print("Decryption failed: Invalid input.")
    else:
        print('Invalid option. Please enter "e" or "d".')