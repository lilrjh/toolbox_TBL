from cryptography.fernet import Fernet
import os

def load_key():
    try:
        with open('fernet_key_folder.key', 'rb') as key_file:
            key = key_file.read()
            return key
    except FileNotFoundError:
        print("La clé Fernet n'a pas été trouvée.")
        return None

key = load_key()
if key is None:
    print("La clé Fernet est nécessaire pour le déchiffrement.")
else:
    fernet = Fernet(key)

    folder_path = r"C:\Users\bjaime\OneDrive - Groupe La Centrale\Bureau\Ecole\Application a la crypto\Test chiffrements"
    files = os.listdir(folder_path)
    print(files)

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as encrypted_file:
                enc_data = encrypted_file.read()

            dec_data = fernet.decrypt(enc_data)

            with open(file_path, 'wb') as decrypted_file:
                decrypted_file.write(dec_data)

            print(f"{file_path} a été déchiffré.")
