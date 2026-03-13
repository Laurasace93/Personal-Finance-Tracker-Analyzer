import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def generar_reporte():
    conexion = sqlite3.connect("finanzas.db")
    # Leemos la tabla directamente a un DataFrame de Pandas
    df = pd.read_sql_query("SELECT * FROM gastos", conexion)
    conexion.close()

    if df.empty:
        print("No hay datos para analizar.")
        return

    # Agrupamos por categoría y sumamos
    resumen = df.groupby('categoria')['monto'].sum()
    
    # Creamos un gráfico sencillo
    resumen.plot(kind='bar', color='skyblue')
    plt.title('Gastos por Categoría')
    plt.ylabel('Dinero Gastado')
    plt.show()

if __name__ == "__main__":
    generar_reporte()


