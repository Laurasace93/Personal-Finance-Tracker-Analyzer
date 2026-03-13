import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def inicializar_base_de_datos():
    """Crea el archivo .db y la tabla si no existen todavía."""
    conexion = sqlite3.connect("finanzas.db")
    cursor = conexion.cursor()
    # Esta instrucción crea la tabla solo si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            descripcion TEXT,
            categoria TEXT,
            monto REAL
        )
    ''')
    conexion.commit()
    conexion.close()

def conectar():
    return sqlite3.connect("finanzas.db")

def insertar_gasto(fecha, descripcion, categoria, monto):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO gastos (fecha, descripcion, categoria, monto) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (fecha, descripcion, categoria, monto))
    conexion.commit()
    conexion.close()
    print("\n✅ ¡Gasto guardado!")


def borrar_gasto():
    # Primero mostramos los gastos para que el usuario vea qué ID quiere borrar
    ver_gastos() 
    
    id_borrar = input("\n🆔 Introduce el ID del gasto que deseas eliminar: ")
    
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Ejecutamos la eliminación
    cursor.execute("DELETE FROM gastos WHERE id = ?", (id_borrar,))
    
    conexion.commit()
    
    # Comprobamos si realmente se borró algo
    if cursor.rowcount > 0:
        print(f"🗑️ Gasto con ID {id_borrar} eliminado con éxito.")
    else:
        print("⚠️ No se encontró ningún gasto con ese ID.")
        
    conexion.close()    

def ver_gastos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM gastos")
    filas = cursor.fetchall()
    
    print("\n--- LISTA DE GASTOS ---")
    print(f"{'ID':<5} | {'Fecha':<12} | {'Descripción':<20} | {'Categoría':<15} | {'Monto':<10}")
    print("-" * 75)
    for fila in filas:
        print(f"{fila[0]:<5} | {fila[1]:<12} | {fila[2]:<20} | {fila[3]:<15} | ${fila[4]:<10.2f}")
    conexion.close()

def generar_reporte():
    conexion = conectar()
    # Cargamos los datos de SQL a un DataFrame de Pandas
    df = pd.read_sql_query("SELECT * FROM gastos", conexion)
    conexion.close()

    if df.empty:
        print("❌ No hay datos suficientes para generar un gráfico.")
        return

    # Agrupamos por categoría y sumamos los montos
    resumen = df.groupby('categoria')['monto'].sum()

    # Creamos un gráfico de tarta (Pie Chart)
    plt.figure(figsize=(8, 6))
    resumen.plot(kind='pie', autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title('Distribución de Gastos por Categoría')
    plt.ylabel('') # Quitamos la etiqueta lateral para que se vea limpio
    plt.show()
    print("📊 Gráfico generado en una ventana emergente.")


def check_presupuesto(limite):
    conexion = sqlite3.connect("finanzas.db")
    total = conexion.execute("SELECT SUM(monto) FROM gastos").fetchone()[0]
    conexion.close()
    if total > limite:
        print(f"⚠️ ¡ATENCIÓN! Has gastado ${total}. Superaste tu límite de ${limite}.")
    else:
        print(f"✅ Vas bien. Llevas ${total} de ${limite} disponibles.")    

def menu():
    # LLAMAMOS A LA CREACIÓN AQUÍ
    inicializar_base_de_datos() 
    
    while True:
        print("\n💰 GESTOR DE FINANZAS PERSONALES")
        print("1. Agregar nuevo gasto")
        print("2. Borrar gasto")
        print("3. Ver todos los gastos")
        print("4. Generar reporte de gastos por categoría")
        print("5. Limite de presupuesto mensual")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            fecha = input("Fecha (AAAA-MM-DD): ")
            desc = input("Descripción: ")
            cat = input("Categoría: ")
            monto = float(input("Monto: "))
            insertar_gasto(fecha, desc, cat, monto)
        elif opcion == "2":
            borrar_gasto()
        elif opcion == "3":
            ver_gastos()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            limite = float(input("Introduce el límite de presupuesto mensual: "))
            check_presupuesto(limite)
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()

    