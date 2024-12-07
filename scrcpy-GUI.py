import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def error_message(output): 
    messagebox.showerror("Error", f"Compruebe el cable o conecte el dispositivo via TCP/IP. El Error ha sido: {output}")

def ok_message():
    messagebox.showinfo("Success!!!", "La conexión se estableció correctamente, espere a que se inicie")

def device_disconnect_message():
    messagebox.showinfo("Success!!!", "Los dispositivos inalámbricos se han eliminado correctamente")


def run_scrcpy():
    command = 'scrcpy'
    adb_command = 'adb connect'
    if tcpip.get(): # si casilla selecionada
        if tcpip_value.get() == 'auto': # si casilla seleccionada y auto seleccionado
            command += ' --tcpip -e'        
        else:
            adb_command += f' {tcpip_value.get()}:5555' # Añadir IP personalizada
            process = subprocess.run(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = process.stdout.decode() + process.stderr.decode()
            print(adb_command)
            print(f"ADB Command Output: {output}")
            if 'daemon started successfully' in output.lower():
                ok_message()
            else:
                error_message(output)
                root.destroy()
                return
                
    else:
        command += ' -d'
    if turnscreenoff.get():
        command += ' --turn-screen-off'
    if alwaysontop.get():
        command += ' --always-on-top'
    if stayawake.get():
        command += ' --stay-awake'
    if maxfps.get():
        command += f' --max-fps={fps_value.get()}'

    output = process.stdout.decode() + process.stderr.decode()
    
    if 'error' in output.lower(): # Verificar si hay errores en la salida del terminal
        error_message(output)
        root.destroy()
        return
    else:
        ok_message()
        root.destroy()

    root.withdraw()

    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # Con terminal

    print(command)
    print(f"SCRCPY Command Output: {output}")


def clear_devices():
    process = subprocess.run('adb disconnect', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # Con terminal
    output = process.stdout.decode() + process.stderr.decode()
    if 'disconnected everything' in output:
        device_disconnect_message()
    else:
        error_message(output)

# Crear la ventana principal
root = tk.Tk()
root.title("SCRCPY-GUI v1.2")
root.geometry("320x340")  # ancho x alto // Establecer el tamaño de la ventana

# Establecer el ícono de la ventana 
root.iconbitmap("icon.ico")

# Crear una variable para la casilla de verificación
tcpip = tk.BooleanVar() # --tcpip
turnscreenoff = tk.BooleanVar() # --turn-screen-off
alwaysontop = tk.BooleanVar() # --always-on-top 
stayawake = tk.BooleanVar() # --stay-awake no suspender el móvil
maxfps = tk.BooleanVar() # --max-fps

# Crear y colocar las casillas de verificación y comboboxes para tcpip
tcpip_checkbox = tk.Checkbutton(root, text='Conexión via TCP/IP. Puerto:', variable=tcpip)
tcpip_checkbox.pack(pady=5)

tcpip_options = ["auto", "192.168.1.x", "192.168.x.x"]
tcpip_value = tk.StringVar(value=tcpip_options[0])
tcpip_combobox = ttk.Combobox(root, textvariable=tcpip_value, values=tcpip_options)
tcpip_combobox.pack(pady=5)

# Crear y colocar las casillas de verificación
screenoff_checkbox = tk.Checkbutton(root, text='Apagar pantalla del dispositivo', variable=turnscreenoff)
screenoff_checkbox.pack(pady=5)

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

author_label = tk.Label(root, text="SCRCPY-GUI - Versión 1.2 - Hodei Dz", font=("Arial", 8)) 
author_label.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
