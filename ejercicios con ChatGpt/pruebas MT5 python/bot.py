import pandas as pd
import numpy as np

# Crear un informe simulado de MT5
np.random.seed(42)

# Generar datos simulados
bots = [f'Bot_{i}' for i in range(1, 6)]  # IDs de bots
n_operaciones = 100

data = {
    'ID_Bot': np.random.choice(bots, n_operaciones),
    'Resultado': np.random.uniform(-100, 100, n_operaciones),  # Ganancia o pérdida
    'Balance': 1000 + np.cumsum(np.random.uniform(-100, 100, n_operaciones)),
}

df = pd.DataFrame(data)

# Función para calcular métricas por bot
def calcular_metricas(df):
    resumen = {}

    for bot_id, grupo in df.groupby('ID_Bot'):
        beneficio_neto = grupo['Resultado'].sum()
        ganancia_total = grupo[grupo['Resultado'] > 0]['Resultado'].sum()
        perdida_total = abs(grupo[grupo['Resultado'] < 0]['Resultado'].sum())
        factor_beneficio = ganancia_total / perdida_total if perdida_total != 0 else np.inf
        operaciones_totales = len(grupo)

        # Cálculo de pérdidas consecutivas
        perdidas_consecutivas = 0
        max_perdidas_consecutivas = 0

        for resultado in grupo['Resultado']:
            if resultado < 0:
                perdidas_consecutivas += 1
                max_perdidas_consecutivas = max(max_perdidas_consecutivas, perdidas_consecutivas)
            else:
                perdidas_consecutivas = 0

        # Drawdown
        drawdown = max(1000 - grupo['Balance'].min(), 0)

        resumen[bot_id] = {
            'Beneficio Neto': beneficio_neto,
            'Factor de Beneficio': factor_beneficio,
            'Operaciones Totales': operaciones_totales,
            'Pérdidas Consecutivas': max_perdidas_consecutivas,
            'Drawdown': drawdown,
        }

    return resumen

# Calcular métricas por bot
resumen_bots = calcular_metricas(df)

# Menú interactivo para consultar métricas
while True:
    print("\n\n=== Menú de Consulta de Bots ===")
    print("1. Ver métricas de un bot por ID")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        bot_id = input("Ingresa el ID del bot (e.g., Bot_1): ")
        if bot_id in resumen_bots:
            print("\n--- Métricas del Bot ---")
            for key, value in resumen_bots[bot_id].items():
                print(f"{key}: {value}")
        else:
            print("\nID de Bot no encontrado.")
    elif opcion == '2':
        print("\nSaliendo del programa. ¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Intenta de nuevo.")
