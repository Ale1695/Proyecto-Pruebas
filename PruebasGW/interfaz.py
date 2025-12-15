import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # ✅ importa ttk para usar Combobox
from reservas import buscar_vuelos, crear_reserva, cancelar_reserva, obtener_reservas

def buscar():
    origen = combo_origen.get().upper()
    destino = combo_destino.get().upper()
    resultados = buscar_vuelos(origen, destino)
    listbox.delete(0, tk.END)
    if resultados:
        for v in resultados:
            listbox.insert(tk.END, f"ID:{v['id']} {v['origen']}→{v['destino']} | ${v['precio']} | {v['asientos']} asientos")
    else:
        messagebox.showinfo("Sin resultados", "No hay vuelos disponibles")

def reservar():
    try:
        nombre = entry_nombre.get()
        vuelo_id = int(entry_id.get())
        asientos = int(entry_asientos.get())
        reservas = crear_reserva(nombre, vuelo_id, asientos)
        messagebox.showinfo("Éxito", f"Reserva creada para {nombre}.\nTotal: ${reservas['total']}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def cancelar():
    try:
        nombre = entry_nombre.get()
        cancelar_reserva(nombre)
        messagebox.showinfo("Cancelado", f"Reserva de {nombre} eliminada.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def ver_reservas():
    lista = obtener_reservas()
    if not lista:
        messagebox.showinfo("Reservas", "No hay reservas registradas.")
    else:
        texto = "\n".join([f"{r['cliente']} → vuelo {r['vuelo']} ({r['asientos']} asientos)" for r in lista])
        messagebox.showinfo("Reservas activas", texto)

# --- Interfaz ---

ventana = tk.Tk()
ventana.title("Sistema de Reservas Green Airways")
ventana.geometry("500x420")

# --- Dropdown Origen ---
tk.Label(ventana, text="Origen:").pack()
combo_origen = ttk.Combobox(ventana, values=["SJO", "Liberia", "Cobano"], state="readonly")
combo_origen.pack()

# --- Dropdown Destino ---
tk.Label(ventana, text="Destino:").pack()
combo_destino = ttk.Combobox(ventana, values=["SJO", "Liberia", "Cobano"], state="readonly")
combo_destino.pack()

# --- Botón buscar vuelos ---
tk.Button(ventana, text="Buscar vuelos", command=buscar).pack()
listbox = tk.Listbox(ventana, width=60); listbox.pack()

# --- Datos de reserva ---
tk.Label(ventana, text="Nombre del cliente:").pack()
entry_nombre = tk.Entry(ventana); entry_nombre.pack()

tk.Label(ventana, text="ID del vuelo:").pack()
entry_id = tk.Entry(ventana); entry_id.pack()

tk.Label(ventana, text="Asientos:").pack()
entry_asientos = tk.Entry(ventana); entry_asientos.pack()

# --- Botones ---
tk.Button(ventana, text="Reservar", command=reservar).pack()
tk.Button(ventana, text="Cancelar reserva", command=cancelar).pack()
tk.Button(ventana, text="Ver reservas", command=ver_reservas).pack()

ventana.mainloop()
