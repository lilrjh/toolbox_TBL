import customtkinter 
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from cryptography.fernet import Fernet
import json
import os
from tkinter import filedialog



def show_frame(frame):
    frame.tkraise()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()




def update_options():
    print("La valeur de 'var' a changé en", var.get())



def signup():
    username = entry1.get()
    password = entry2.get()
    confirmation = entry3.get()
    print("| Username : ", username,"| ", " | Password : ", password, " | Confirmation : ", confirmation)

    if password == confirmation:
        with open("output.txt", "a") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n\n")
    else:
        messagebox.showerror("Erreur", "Le mot de passe et la confirmation ne correspondent pas.")

    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')



def login():
    username = entry4.get()
    password = entry5.get()

    if checkbox.get():
        encrypt_credentials(username, password)
    else:
        if os.path.exists(CREDENTIALS_FILE):
            os.remove(CREDENTIALS_FILE)


    button3.configure(state="disabled")

    with open("output.txt", "r") as file:
        lines = file.readlines()
        credentials = {}
        i = 0
        while i < len(lines):
            if len(lines[i].strip().split(": ")) > 1:
                stored_username = lines[i].strip().split(": ")[1]
                if i+1 < len(lines) and len(lines[i+1].strip().split(": ")) > 1:
                    stored_password = lines[i+1].strip().split(": ")[1]
                    credentials[stored_username] = stored_password
                    i += 2  
                else:
                    i += 1  
            else:
                i += 1  

    if username in credentials and credentials[username] == password:
        print("Login successful!")
        button3.configure(state="normal")
        show_frame(utility_frame)  
    else:
        messagebox.showerror("Erreur", "Identifiant ou Mot de passe incorrect.")
        button3.configure(state="normal")

    entry4.delete(0, 'end')
    entry5.delete(0, 'end')



def update_options(*args):
    global optionmenu_2
    if optionmenu_2 is not None:
        optionmenu_2.pack_forget()  
    if var.get() == "Symétrique":
        optionmenu_2 = customtkinter.CTkOptionMenu(master=utility_frame, values=["AES", "DES"])
    elif var.get() == "Asymétrique":
        optionmenu_2 = customtkinter.CTkOptionMenu(master=utility_frame, values=["RSA", "RH"])
    if optionmenu_2 is not None:
        optionmenu_2.pack(pady = 5, side=tk.TOP)



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
    


CREDENTIALS_FILE = "credentials.json"



key = load_key()
if key is None:
    key = generateKey()

fernet = Fernet(key)



def encrypt_credentials(username, password):
    credentials = {"username": username, "password": password}
    credentials_json = json.dumps(credentials)
    encrypted = fernet.encrypt(credentials_json.encode())
    with open(CREDENTIALS_FILE, "wb") as file:
        file.write(encrypted)



def decrypt_credentials():
    try:
        with open(CREDENTIALS_FILE, "rb") as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        credentials = json.loads(decrypted.decode())
        return credentials
    except FileNotFoundError:
        print("Le fichier d'informations d'identification n'a pas été trouvé.")
        return None



def load_credentials():
    credentials = decrypt_credentials()
    if credentials is not None:
        entry4.insert(0, credentials["username"])
        entry5.insert(0, credentials["password"])

def chiffrement():
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
        print("La clé Fernet est nécessaire pour le chiffrement.")
    else:
        fernet = Fernet(key)

        root = tk.Tk()
        root.withdraw()  

        folder_path = filedialog.askdirectory()  

        if folder_path:
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
        else:
            print("Aucun dossier n'a été sélectionné.")

def dechiffrement():
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

        root = tk.Tk()
        root.withdraw()  

        folder_path = filedialog.askdirectory()  

        if folder_path:
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
        else:
            print("Aucun dossier n'a été sélectionné.")




initial_frame = customtkinter.CTkFrame(master=root)
initial_frame.grid(row=0, column=0, sticky='news')

login_button = customtkinter.CTkButton(master=initial_frame, text="Se connecter", command=lambda: show_frame(login_frame))
login_button.pack(pady=12, padx=10, side=tk.LEFT)

signup_button = customtkinter.CTkButton(master=initial_frame, text="S'inscrire", command=lambda: show_frame(signup_frame))
signup_button.pack(pady=12, padx=10, side=tk.LEFT)







login_frame = customtkinter.CTkFrame(master=root)
login_frame.grid(row=0, column=0, sticky='news')











label = customtkinter.CTkLabel(master=login_frame, text="Login", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Username")
entry4.pack(pady=12, padx=10)

entry5 = customtkinter.CTkEntry(master=login_frame, placeholder_text="Password", show="*")
entry5.pack(pady=12, padx=10)

load_button = customtkinter.CTkButton(master=login_frame, text="Charger", command=load_credentials)
load_button.pack(pady=12, padx=10)

button3 = customtkinter.CTkButton(master=login_frame, text="Connexion", command=login)
button3.pack(pady=12, padx=10)

entry4.bind('<Return>', lambda event: login())
entry5.bind('<Return>', lambda event: login())
button3.bind('<Return>', lambda event: login())

checkbox = customtkinter.CTkCheckBox(master=login_frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

back_button = customtkinter.CTkButton(master=login_frame, text="Retour", command=lambda: show_frame(initial_frame))
back_button.pack(pady=12, padx=10)







signup_frame = customtkinter.CTkFrame(master=root)
signup_frame.grid(row=0, column=0, sticky='news')






label = customtkinter.CTkLabel(master=signup_frame, text="Sign up", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=signup_frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=signup_frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=signup_frame, placeholder_text="Confirmation", show="*")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=signup_frame, text="Création", command=signup)
button.pack(pady=12, padx=10)

entry1.bind('<Return>', lambda event: signup())
entry2.bind('<Return>', lambda event: signup())
entry3.bind('<Return>', lambda event: signup())
button.bind('<Return>', lambda event: signup())


back_button2 = customtkinter.CTkButton(master=signup_frame, text="Retour", command=lambda: show_frame(initial_frame))
back_button2.pack(pady=12, padx=10)







utility_frame = customtkinter.CTkFrame(master=root)
utility_frame.grid(row=0, column=0, sticky='news')


var = tk.StringVar(master=utility_frame)
var.trace('w', update_options)

optionmenu_1 = customtkinter.CTkOptionMenu(master=utility_frame, values=["Symétrique","Asymétrique"], variable=var)
optionmenu_1.pack(pady=12, padx=10, side=tk.TOP)

optionmenu_2 = None
update_options()

deco_button = customtkinter.CTkButton(master=utility_frame, text="Se déconnecter", command=lambda: show_frame(initial_frame))
deco_button.pack(pady=30, padx=20, side=tk.BOTTOM)

button1 = customtkinter.CTkButton(master=utility_frame, text="Chiffrer", command=chiffrement)
button1.pack(pady=5, padx=20, side=tk.BOTTOM)

button2 = customtkinter.CTkButton(master=utility_frame, text="Déchiffrer", command=dechiffrement)
button2.pack(pady=30, padx=10, side=tk.BOTTOM)





show_frame(initial_frame)

root.mainloop()