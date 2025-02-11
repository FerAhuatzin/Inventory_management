import tkinter as tk
from tkinter import messagebox
from db import register, check_stock, get_products_by_category, update_stock

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("600x400")

        self.init_ui()

    def init_ui(self):
        # Títulos de campos
        self.label_title = tk.Label(self.root, text="Agregar producto", font=("Helvetica", 12, "bold"))
        self.label_title.grid(row=0, column=0)

        self.label_name = tk.Label(self.root, text="Nombre del producto")
        self.label_name.grid(row=1, column=0)

        self.label_price = tk.Label(self.root, text="Precio")
        self.label_price.grid(row=2, column=0)

        self.label_category = tk.Label(self.root, text="Categoría")
        self.label_category.grid(row=3, column=0)

        self.label_stock = tk.Label(self.root, text="Stock")
        self.label_stock.grid(row=4, column=0)

        self.label_title_2 = tk.Label(self.root, text="Revisar stock", font=("Helvetica", 12, "bold"))
        self.label_title_2.grid(row=5, column=0)

        self.label_id = tk.Label(self.root, text="id")
        self.label_id.grid(row=6, column=0)

        self.label_title_3 = tk.Label(self.root, text="Ver por categoría", font=("Helvetica", 12, "bold"))
        self.label_title_3.grid(row=7, column=0)

        self.label_category_2 = tk.Label(self.root, text="Categoría")
        self.label_category_2.grid(row=8, column=0)

        self.label_title_3 = tk.Label(self.root, text="Cambiar stock", font=("Helvetica", 12, "bold"))
        self.label_title_3.grid(row=9, column=0)

        self.label_category_2 = tk.Label(self.root, text="id")
        self.label_category_2.grid(row=10, column=0)

        self.label_stock_2 = tk.Label(self.root, text="Stock nuevo")
        self.label_stock_2.grid(row=11, column=0)

        # Campos de entrada
        self.name_input = tk.Entry(self.root)
        self.name_input.grid(row=1, column=1)

        self.price_input = tk.Entry(self.root)
        self.price_input.grid(row=2, column=1)

        self.category_input = tk.Entry(self.root)
        self.category_input.grid(row=3, column=1)

        self.stock_input = tk.Entry(self.root)
        self.stock_input.grid(row=4, column=1)

        self.id_input = tk.Entry(self.root)
        self.id_input.grid(row=6, column=1)

        self.category_input_2 = tk.Entry(self.root)
        self.category_input_2.grid(row=8, column=1)

        self.id_input_2 = tk.Entry(self.root)
        self.id_input_2.grid(row=10, column=1)

        self.stock_input_2 = tk.Entry(self.root)
        self.stock_input_2.grid(row=11, column=1)

        # Botones
        self.add_button = tk.Button(self.root, text="Agregar Producto", command=self.agregar_producto)
        self.add_button.grid(row=4, column=2)

        self.search_button = tk.Button(self.root, text="Buscar por ID", command=self.buscar_por_id)
        self.search_button.grid(row=6, column=2)

        self.search_category_button = tk.Button(self.root, text="Buscar por Categoría", command=self.buscar_por_categoria)
        self.search_category_button.grid(row=8, column=2)

        self.update_stock_button = tk.Button(self.root, text="Cambiar Stock", command=self.cambiar_stock)
        self.update_stock_button.grid(row=11, column=2)

        # Tabla para mostrar productos
        self.product_table = tk.Listbox(self.root, width=80, height=10)
        self.product_table.grid(row=12, columnspan=5)

    def agregar_producto(self):
        try:
            name = self.name_input.get()
            price = float(self.price_input.get())
            category = self.category_input.get()
            stock = int(self.stock_input.get())

            register(name, price, category, stock)

            # Limpiar campos después de agregar
            self.name_input.delete(0, tk.END)
            self.price_input.delete(0, tk.END)
            self.category_input.delete(0, tk.END)
            self.stock_input.delete(0, tk.END)

            self.product_table.delete(0, tk.END)
            self.product_table.insert(tk.END, f"Producto agregado de forma correcta")

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos para todos los campos.")

    def buscar_por_id(self):
        try:
            product_id = int(self.id_input.get())
            stock = check_stock(product_id)
            if stock is not None:
                self.product_table.delete(0, tk.END)  # Limpiar la lista antes de cargar nuevos productos
                self.product_table.insert(tk.END, f"ID: {product_id} | Stock: {stock}")
            else:
                messagebox.showerror("Error", f"No se encontró el producto con ID {product_id}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un ID válido.")

    def buscar_por_categoria(self):
        category = self.category_input_2.get()
        productos = get_products_by_category(category)
        if productos:
            self.product_table.delete(0, tk.END)  # Limpiar la lista antes de cargar nuevos productos
            for producto in productos:
                self.product_table.insert(tk.END, f"ID: {producto[0]} | Nombre: {producto[1]} | Precio: {producto[2]} | Stock: {producto[3]}")
        else:
            messagebox.showerror("Error", f"No se encontraron productos en la categoría '{category}'.")

    def cambiar_stock(self):
        try:
            product_id = int(self.id_input_2.get())
            new_stock = int(self.stock_input_2.get())
            update_stock(product_id, new_stock)
            self.product_table.delete(0, tk.END)
            self.product_table.insert(tk.END, f"Stock del producto {product_id}, cambiado de forma correcta")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un ID y un stock válidos.")


if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = Aplicacion(root)  # Crear la aplicación
    root.mainloop()  # Iniciar el ciclo de eventos
