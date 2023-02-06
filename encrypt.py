mode = input("would you like to encrypt or decrypt? (e/d) - ")

key = int(input("which key would you like your cypher to use? (1-9) - "))

message = input("enter a message to decrypt/encrypt - ").lower()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt():
    new = ''
    for i in message:
        if alphabet.index(i)+key > len(alphabet)-1:
            overflow = alphabet.index(i)+key-25
            new = new+alphabet[overflow-1]
        else:
            new = new + alphabet[alphabet.index(i)+key]
    print(new)

def decrypt():
    new = ''
    for i in message:
        new = new + alphabet[alphabet.index(i)-key]
    print(new)
 
if mode == 'e':
    encrypt()
else:
    decrypt()