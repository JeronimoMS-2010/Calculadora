import tkinter as tk

window = tk.Tk()
window.geometry("300x400")
window.title("Calculadora")

# Pantalla
Pantalla = tk.Entry(window, font=("Arial", 16), justify="right", state="readonly")
Pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Función para escribir en pantalla
def presionar(valor):
    if valor == "C":
        Pantalla.config(state="normal")
        Pantalla.delete(0, "end")
        Pantalla.config(state="readonly")

    elif valor == "=":
        operacion = Pantalla.get()
        resultado = eval(operacion)
        Pantalla.config(state="normal")
        Pantalla.delete(0, "end")
        resultado_UI = str(resultado)
        Pantalla.insert("end", resultado_UI)
        Pantalla.config(state="readonly")

        
        
        

    else:
        Pantalla.config(state="normal")
        Pantalla.insert("end", valor)
        Pantalla.config(state="readonly")


# Botones
botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

fila = 1
col = 0

for boton in botones:
    tk.Button(
        window,
        text=boton,
        command=lambda v=boton: presionar(v)
    ).grid(row=fila, column=col, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        fila += 1

# Expandir columnas y filas
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

for i in range(fila + 1):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()
