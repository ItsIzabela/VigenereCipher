import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Szyfr Vigenère")
root.geometry("500x400")

def vigenere_encrypt(plain_text, key):
    cipher_text = []
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            key_char = key[key_index % key_len]
            key_char_value = ord(key_char) - 65
            encrypted_char = chr((ord(char) - offset + key_char_value) % 26 + offset)
            cipher_text.append(encrypted_char)
            key_index += 1
        else:
            cipher_text.append(char)

    return ''.join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    plain_text = []
    key = key.upper()
    key_len = len(key)
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            key_char = key[key_index % key_len]
            key_char_value = ord(key_char) - 65
            decrypted_char = chr((ord(char) - offset - key_char_value) % 26 + offset)
            plain_text.append(decrypted_char)
            key_index += 1
        else:
            plain_text.append(char) 

    return ''.join(plain_text)

def encrypt_action():
    plain_text = input_text.get("1.0", "end-1c")
    key = key_entry.get()

    if not plain_text or not key:
        messagebox.showerror("Error", "Musisz wpisac klucz i tekst!")
        return

    encrypted_text = vigenere_encrypt(plain_text, key)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt_action():
    cipher_text = input_text.get("1.0", "end-1c")
    key = key_entry.get()

    if not cipher_text or not key:
        messagebox.showerror("Error", "Musisz wpisac klucz i tekst!")
        return

    decrypted_text = vigenere_decrypt(cipher_text, key)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)


key_label = tk.Label(root, text="Wprowadz klucz:")
key_label.pack(pady=5)
key_entry = tk.Entry(root, width=30)
key_entry.pack(pady=5)


input_label = tk.Label(root, text="Wprowadz tekst (do zaszyfrowanie lub do odszyfrowania):")
input_label.pack(pady=5)
input_text = tk.Text(root, height=5, width=60)
input_text.pack(pady=5)


output_label = tk.Label(root, text="Wynik:")
output_label.pack(pady=5)
output_text = tk.Text(root, height=5, width=60)
output_text.pack(pady=5)

encrypt_button = tk.Button(root, text="Zaszyfruj", command=encrypt_action)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Odszyfruj", command=decrypt_action)
decrypt_button.pack(pady=5)

root.mainloop()