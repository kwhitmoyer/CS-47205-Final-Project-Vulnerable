import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def hashPassword(userPassword):
    passwordBytes = userPassword.encode('utf-8')
    hashedPassword = hashlib.sha256(passwordBytes).digest()
    return hashedPassword

def encrypt(plaintext):
    aes_key = get_random_bytes(32)
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return(aes_key, cipher.nonce, ciphertext, tag)

def decrypt(aes_key, nonce, ciphertext, tag):
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try: 
        cipher.verify(tag)
        return plaintext
    except ValueError:
        print("Message is corrupted.")
            

if __name__ == "__main__":
    print("Testing encryption mangager...")
    password = "testPassword"
    print("The unhashed password is: " + password)
    hashedPassword = hashPassword(password)
    print("The hashed password is: " + hashedPassword.hex())

    aes_key, nonce, ciphertext, tag = encrypt(hashedPassword)
    print("The encrypted text is: " + ciphertext.hex())
    decrypted = decrypt(aes_key, nonce, ciphertext, tag)
    print("The decrypted text is: " + decrypted.hex())

'''
Academic Integrity Notes:
    Techniques for hashing passwords in Python were taken from here: https://www.tutorialspoint.com/how-to-hash-passwords-in-python
    Structure of code for performing AES Encryption with the pycryptdomex library was sourced from:
        https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
        https://pycryptodome.readthedocs.io/en/latest/src/examples.html
    General information on performing AES Encryption is from: 
        https://medium.com/@dheeraj.mickey/how-to-encrypt-and-decrypt-files-in-python-using-aes-a-step-by-step-guide-d0eb6f525e4e
        https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/

    All sources can be found in sources.md in repo
'''