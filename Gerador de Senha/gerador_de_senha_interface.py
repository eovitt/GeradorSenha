import tkinter as tk
from tkinter import ttk
import random
import pyperclip

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&"

def generate_password(n):
    password = ""
    for _ in range(n):
        password += random.choice(characters)
    return password

def generate_and_display_password():
    password_length = int(entry.get())
    password = generate_password(password_length)
    result_label.config(text=f"Senha gerada: {password}")
    pyperclip.copy(password)  # Copiar a senha para a área de transferência

# Criar janela
window = tk.Tk()
window.title("Gerador de Senha")

# Adicionar estilo ao tema do tkinter
style = ttk.Style()
style.theme_use("clam")  # Pode experimentar com outros temas disponíveis

# Elementos da interface
label = ttk.Label(window, text="Comprimento da senha:")
label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

entry = ttk.Entry(window)
entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

generate_button = ttk.Button(window, text="Gerar Senha", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=20)

result_label = ttk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

copy_button = ttk.Button(window, text="Copiar Senha", command=lambda: pyperclip.copy(result_label.cget("text")[14:]))
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar loop de interface gráfica
window.mainloop()