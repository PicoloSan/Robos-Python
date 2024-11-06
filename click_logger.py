# biblioteca para instalar:
# pip install pynput
# Se o botão do mouse é pressionado, a posição do botão é salva no arquivo cliques.txt
# Para executar:
# python click_logger.py
# para interromper:
# fechar o popup

from pynput import mouse
import tkinter as tk
from tkinter import messagebox
import threading
import sys

# Função que será chamada quando um clique ocorrer
def on_click(x, y, button, pressed):
    if pressed:
        with open("cliques.txt", "a") as f:
            f.write(f' Clique em: ({x}, {y}) com {button}\n')
            # print(f' Clique em: ({x}, {y}) com {button}')

# Função para abrir o messagebox
def mostrar_messagebox():
    global running
    running = True
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    messagebox.showinfo("Informação", "Clique em OK para encerrar o script")
    running = False
    root.destroy()  # Fecha a janela oculta

# Função para encerrar o programa quando o messagebox for fechado
def check_running():
    while running:
        pass
    listener.stop()
    sys.exit()

# Monitorando cliques do mouse
listener = mouse.Listener(on_click=on_click)

# Começa o listener do mouse
listener.start()

# Usando threading para mostrar o messagebox e verificar o status
running = False

# Inicia thread para mostrar o messagebox
threading.Thread(target=mostrar_messagebox).start()

# Checa se o messagebox ainda está aberto
check_running()
