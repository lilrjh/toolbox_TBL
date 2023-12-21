from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_key)
    
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_key)

def load_key_pair():
    try:
        with open("private_key.pem", "rb") as private_file:
            private_key = RSA.import_key(private_file.read())
        with open("public_key.pem", "rb") as public_file:
            public_key = RSA.import_key(public_file.read())
    except FileNotFoundError:
        generate_key_pair()
        return load_key_pair()

    return private_key, public_key

def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode())
    return ciphertext

def decrypt_message(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    message = cipher.decrypt(ciphertext).decode()
    return message

def main():
    choice = input("Voulez-vous chiffrer ou déchiffrer? (c/d): ")

    if choice.lower() == 'c':
        message = input("Entrez le message à chiffrer : ")
        _, public_key = load_key_pair()
        ciphertext = encrypt_message(message, public_key)
        hex_ciphertext = binascii.hexlify(ciphertext).decode('utf-8')
        print(f"Message chiffré (hex) : {hex_ciphertext}")
    elif choice.lower() == 'd':
        hex_ciphertext = input("Entrez le message chiffré (hex) : ")
        ciphertext = binascii.unhexlify(hex_ciphertext)
        private_key, _ = load_key_pair()
        message = decrypt_message(ciphertext, private_key)
        print(f"Message déchiffré : {message}")
    else:
        print("Choix non valide. Veuillez entrer 'c' pour chiffrer ou 'd' pour déchiffrer.")

if __name__ == "__main__":
    main()