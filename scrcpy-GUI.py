import tkinter as tk
from tkinter import ttk
import subprocess

# Función que se ejecuta al presionar el botón
def run_scrcpy():
    command = 'scrcpy'
    if tcpip.get():
        command += ' --tcpip -e'
    else:
        command += ' -d'
    if turnscreenoff.get():
        command += ' --turn-screen-off'
    if windowborderless.get():
        command += ' --window-borderless'
    if alwaysontop.get():
        command += ' --always-on-top'
    if stayawake.get():
        command += ' --stay-awake'
    if maxfps.get():
        command += f' --max-fps={fps_value.get()}'

    root.destroy()
    # subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW) # Sin terminal
    subprocess.run(command, shell=True) # Con terminal
    print(command)

def clear_devices():
    # subprocess.run('adb disconnect', creationflags=subprocess.CREATE_NO_WINDOW) # Sin terminal
    subprocess.run('adb disconnect', shell=True) # Con terminal


# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Gráfica para scrcpy")
root.geometry("320x340")  # ancho x alto // Establecer el tamaño de la ventana

# Establecer el ícono de la ventana 
root.iconbitmap("icon.ico")

# Crear una variable para la casilla de verificación
tcpip = tk.BooleanVar() # --tcpip
turnscreenoff = tk.BooleanVar() # --turn-screen-off
windowborderless = tk.BooleanVar() # --window-border-less
alwaysontop = tk.BooleanVar() # --always-on-top 
stayawake = tk.BooleanVar() # --stay-awake no suspender el movil
maxfps = tk.BooleanVar() # --max-fps


# Crear y colocar la casillas de verificación
tcpip_checkbox = tk.Checkbutton(root, text='Usar TCP/IP (Conexion inalámbrica)', variable=tcpip)
tcpip_checkbox.pack(pady=5)

screenoff_checkbox = tk.Checkbutton(root, text='Apagar pantalla del dispositivo', variable=turnscreenoff)
screenoff_checkbox.pack(pady=5)

windowborderless_checkbox = tk.Checkbutton(root, text='Mostrar ventana sin bordes', variable=windowborderless)
windowborderless_checkbox.pack(pady=5)

alwaysontop_checkbox = tk.Checkbutton(root, text='Mostrar siempre la ventana', variable=alwaysontop)
alwaysontop_checkbox.pack(pady=5)

stayawake_checkbox = tk.Checkbutton(root, text='No suspender el dispositivo', variable=stayawake)
stayawake_checkbox.pack(pady=5)

fps_checkbox = tk.Checkbutton(root, text="Habilitar Limitador de FPS", variable=maxfps)
fps_checkbox.pack(pady=1)

# Crear la lista desplegable
fps_options = ["10", "25", "40", "50"]
fps_value = tk.StringVar(value=fps_options[0])
fps_combobox = ttk.Combobox(root, textvariable=fps_value, values=fps_options)
fps_combobox.pack(pady=5)

# Crear y colocar el botón
run_button = tk.Button(root, text='Iniciar', command=run_scrcpy)
run_button.pack(pady=5)

clear_devices_button = tk.Button(root, text='Borrar conexiones inalámbricas', command=clear_devices)
clear_devices_button.pack(pady=5)

author_label = tk.Label(root, text="Hodei Dz", font=("Arial", 8)) 
author_label.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
