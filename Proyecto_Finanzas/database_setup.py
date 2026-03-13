import sqlite3

def crear_base_de_datos():
    conexion = sqlite3.connect("finanzas.db")
    cursor = conexion.cursor()
    
    # Creamos la tabla si no existe
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
    print("¡Base de datos y tabla creadas con éxito!")

if __name__ == "__main__":
    crear_base_de_datos()