from cryptography.fernet import Fernet
import os

def generateKey():
    key = Fernet.generate_key()
    with open('fernet_key_folder.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    try:
        with open('fernet_key_folder.key', 'rb') as key_file:
            key = key_file.read()
            return key
    except FileNotFoundError:
        print("La clé Fernet n'a pas été trouvée. Genération de la clé !")
        return None

key = load_key()
if key is None:
    key = generateKey()

fernet = Fernet(key)

folder_path = r"C:\Users\bjaime\OneDrive - Groupe La Centrale\Bureau\Ecole\Application a la crypto\Test chiffrements"

files = os.listdir(folder_path)
print(files)

for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            original = file.read()
        
        encrypted = fernet.encrypt(original)
        
        with open(file_path, 'wb') as enc_file:
            enc_file.write(encrypted)
        
        print(f"{file_path} a été chiffré.")