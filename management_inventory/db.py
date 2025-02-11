import mysql.connector
from mysql.connector import Error

# Función para conectar a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="fernando",
        database="inventary"
    )

def register(name: str, price: float, category: str, stock: int):
    try:
        conexion = conectar()
        if conexion.is_connected():
            cursor = conexion.cursor()
            sql = """
            INSERT INTO product (name, price, category, stock)
            VALUES (%s, %s, %s, %s)
            """
            valores = (name, price, category, stock)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Producto '{name}' registrado correctamente con ID {cursor.lastrowid}")
    except Error as e:
        print("Error al registrar el producto:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def update_stock(product_id: int, new_stock: int):
    try:
        conexion = conectar()
        if conexion.is_connected():
            cursor = conexion.cursor()
            sql = "UPDATE product SET stock = %s WHERE id = %s"
            valores = (new_stock, product_id)
            cursor.execute(sql, valores)
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"Stock del producto con ID {product_id} actualizado a {new_stock}")
            else:
                print(f"No se encontró un producto con ID {product_id}")
    except Error as e:
        print("Error al actualizar el stock:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def check_stock(product_id: int):
    try:
        conexion = conectar()
        if conexion.is_connected():
            cursor = conexion.cursor()
            sql = "SELECT stock FROM product WHERE id = %s"
            cursor.execute(sql, (product_id,))
            resultado = cursor.fetchone()
            if resultado:
                print(f"Stock actual del producto con ID {product_id}: {resultado[0]}")
                return resultado[0]
            else:
                print(f"No se encontró un producto con ID {product_id}")
                return None
    except Error as e:
        print("Error al revisar el stock:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

def get_products_by_category(category: str):
    try:
        conexion = conectar()
        if conexion.is_connected():
            cursor = conexion.cursor()
            sql = "SELECT id, name, price, stock FROM product WHERE category = %s"
            cursor.execute(sql, (category,))
            productos = cursor.fetchall()
            if productos:
                print(f"Productos en la categoría '{category}':")
                for p in productos:
                    print(f"ID: {p[0]}, Nombre: {p[1]}, Precio: {p[2]}, Stock: {p[3]}")
                return productos
            else:
                print(f"No se encontraron productos en la categoría '{category}'")
                return []
    except Error as e:
        print("Error al obtener productos por categoría:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()

  
