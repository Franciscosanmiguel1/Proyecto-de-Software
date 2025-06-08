import tkinter as tk
from tkinter import ttk, messagebox

# Clase pedido
class Pedido:
    estados_validos = ["Pendiente", "En preparación", "Entregado", "Cancelado"]

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.estado = "Pendiente"

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in Pedido.estados_validos:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido")

# Clase SistemaPedidos
class SistemaPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, producto, cantidad):
        pedido = Pedido(producto, cantidad)
        self.pedidos.append(pedido)

    def obtener_pedidos(self):
        return self.pedidos

    def resumen_por_estado(self):
        resumen = {}
        for pedido in self.pedidos:
            resumen[pedido.estado] = resumen.get(pedido.estado, 0) + 1
        return resumen

# GUI
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pedidos")
        self.sistema = SistemaPedidos()

        # Entrada de producto
        tk.Label(root, text="Producto:").grid(row=0, column=0)
        self.entry_producto = tk.Entry(root)
        self.entry_producto.grid(row=0, column=1)

        # Entrada de cantidad
        tk.Label(root, text="Cantidad:").grid(row=1, column=0)
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.grid(row=1, column=1)

        # Boton agregar
        self.btn_agregar = tk.Button(root, text="Agregar Pedido", command=self.agregar_pedido)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=5)

        # Tabla de pedidos
        self.tree = ttk.Treeview(root, columns=("Producto", "Cantidad", "Estado"), show="headings")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Estado", text="Estado")
        self.tree.grid(row=3, column=0, columnspan=2)

        # Estado nuevo
        tk.Label(root, text="Nuevo estado:").grid(row=4, column=0)
        self.combo_estado = ttk.Combobox(root, values=Pedido.estados_validos)
        self.combo_estado.grid(row=4, column=1)

        # Boton cambiar estado
        self.btn_cambiar = tk.Button(root, text="Cambiar Estado", command=self.cambiar_estado)
        self.btn_cambiar.grid(row=5, column=0, columnspan=2, pady=5)

        # Boton resumen
        self.btn_resumen = tk.Button(root, text="Resumen por Estado", command=self.mostrar_resumen)
        self.btn_resumen.grid(row=6, column=0, columnspan=2, pady=5)

    def agregar_pedido(self):
        producto = self.entry_producto.get()
        cantidad = self.entry_cantidad.get()
        if not producto or not cantidad.isdigit():
            messagebox.showerror("Error", "Datos inválidos.")
            return
        self.sistema.agregar_pedido(producto, int(cantidad))
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for pedido in self.sistema.obtener_pedidos():
            self.tree.insert("", "end", values=(pedido.producto, pedido.cantidad, pedido.estado))

    def cambiar_estado(self):
        seleccionado = self.tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un pedido.")
            return
        nuevo_estado = self.combo_estado.get()
        index = self.tree.index(seleccionado)
        try:
            self.sistema.pedidos[index].cambiar_estado(nuevo_estado)
            self.actualizar_tabla()
        except ValueError:
            messagebox.showerror("Error", "Estado inválido.")

    def mostrar_resumen(self):
        resumen = self.sistema.resumen_por_estado()
        texto = "\n".join([f"{estado}: {cantidad}" for estado, cantidad in resumen.items()])
        messagebox.showinfo("Resumen por Estado", texto)

# Ejecutar app
root = tk.Tk()
app = App(root)
root.mainloop()
