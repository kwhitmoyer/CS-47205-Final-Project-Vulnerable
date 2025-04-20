from encryptionManager import * 
from userDatabaseManager import * 

def loginExistingUser(existingUsername, existingPassword):
    #Toy example: Encrypting with AES-256
    usernameKey, usernameNonce, usernameCipher, usernameTag = encrypt(existingUsername)
    passwordKey, passwordNonce, passwordCipher, passwordTag = encrypt(existingPassword)

    #Toy example: Decrypting from AES-256
    decryptedUsername = decrypt(usernameKey, usernameNonce, usernameCipher, usernameTag).decode('utf-8')
    decryptedPassword = decrypt(passwordKey, passwordNonce, passwordCipher, passwordTag).decode('utf-8')

    checkPassword(decryptedUsername, decryptedPassword)


def loginExistingUserForInjection(existingUsername, existingPassword):
    #Toy example: Encrypting with AES-256
    usernameKey, usernameNonce, usernameCipher, usernameTag = encrypt(existingUsername)
    passwordKey, passwordNonce, passwordCipher, passwordTag = encrypt(existingPassword)

    #Toy example: Decrypting from AES-256
    decryptedUsername = decrypt(usernameKey, usernameNonce, usernameCipher, usernameTag).decode('utf-8')
    decryptedPassword = decrypt(passwordKey, passwordNonce, passwordCipher, passwordTag).decode('utf-8')

    checkPassword(decryptedUsername, decryptedPassword)


def addNewUser(newUsernameInput, newPasswordInput): 
    newUserUsername = newUsernameInput
    newUserPassword = newPasswordInput

    #Toy example: Encrypting with AES-256
    usernameKey, usernameNonce, usernameCipher, usernameTag = encrypt(newUsernameInput)
    passwordKey, passwordNonce, passwordCipher, passwordTag = encrypt(newPasswordInput)

    #Toy example: Decrypting with AES-256
    decryptedUsername = decrypt(usernameKey, usernameNonce, usernameCipher, usernameTag).decode('utf-8')
    decryptedPassword = decrypt(passwordKey, passwordNonce, passwordCipher, passwordTag).decode('utf-8')

    addUser(decryptedUsername, decryptedPassword)

#No tests as using the UI provides the same functionality 