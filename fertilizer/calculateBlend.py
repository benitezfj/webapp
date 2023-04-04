# import psycopg2
import pandas as pd
import numpy as np
from numpy import linalg as LA
from pulp import *

# from config import Config


def calculateBlend(n, p, k, db):

    # cambiar las necesidades
    necesidades = {"N": n, "P": p, "K": k}

    # elegir cual mercado es (db=1 si es Iberia, db=2 si es Paraguay)
    # Cargar columnas N, P, K en excel
    if db == 1:
        # try:
        #     conn = psycopg2.connect(database=Config.DATABASE_NAME,
        #                                 host=Config.HOST,
        #                                 user=Config.DB_USER,
        #                                 password=Config.DB_PASSWORD,
        #                                 port=Config.POST)
        #     cursor = conn.cursor()
        #     postgreSQL_select = "select nitrogen_total_perc, phosphorus_2o5_total_perc, potassium_2o2_soluble_water_perc from fertiberia"

        #     cursor.execute(postgreSQL_select)
        #     records = cursor.fetchall()

        #     result=[]
        #     for row in records:
        #         result.append(row)
        #     df=np.asarray(result,dtype='int')

        # except (Exception, psycopg2.Error) as error:
        #     print("Error while fetching data from PostgreSQL", error)

        # finally:
        #     if conn:
        #         cursor.close()
        #         conn.close()

        # Obtain N, P2O5 and K2O columns from FertilizersFertiberia.xlsx
        # We convert the Pandas dataframe to numpy in order to access the elements of the matrix easily
        df = pd.read_excel(
            "fertilizer/FertilizersFertiberia_AWS.xlsx", usecols=[1, 2, 3]
        )
    if db == 2:
        # try:
        #     conn = psycopg2.connect(database=Config.DATABASE_NAME,
        #                                 host=Config.HOST,
        #                                 user=Config.DB_USER,
        #                                 password=Config.DB_PASSWORD,
        #                                 port=Config.POST)
        #     cursor = conn.cursor()
        #     postgreSQL_select = "select nitrogen, phosphorus, potassium from bunge"

        #     cursor.execute(postgreSQL_select)
        #     records = cursor.fetchall()

        #     result=[]
        #     for row in records:
        #         result.append(row)
        #     matrix=np.asarray(result,dtype='int')

        # except (Exception, psycopg2.Error) as error:
        #     print("Error while fetching data from PostgreSQL", error)

        # finally:
        #     if conn:
        #         cursor.close()
        #         conn.close()
        df = pd.read_excel("fertilizer/BungeParaguay_AWS.xlsx", usecols=[1, 2, 3])

    # Crear una lista de Python con los valores de la columna cargada
    lista_N = df["N"].tolist()
    lista_P = df["P"].tolist()
    lista_K = df["K"].tolist()

    Nombre_fertilizante = []
    for i in range(len(lista_N)):
        Nombre_fertilizante.append(
            str(lista_N[i]) + "-" + str(lista_P[i]) + "-" + str(lista_K[i])
        )

    # df['nombre fertilizante']=Nombre_fertilizante

    # para crear el DataFrame a usar
    data = pd.DataFrame(
        {
            "Fertilizante": Nombre_fertilizante,
            "% de N": lista_N,
            "% de P": lista_P,
            "% de K": lista_K,
        }
    )

    # Definimos el modelo de programación lineal
    model = LpProblem("Optimización de fertilizantes", LpMinimize)

    # Definimos las variables de decisión
    nfertilizantes = len(data)
    x = LpVariable.dicts("x", list(range(nfertilizantes)), lowBound=0)

    # Definimos la función objetivo
    model += lpSum([x[i] for i in range(nfertilizantes)])

    # Definimos las restricciones
    for nutriente in necesidades:
        model += (
            lpSum(
                [
                    data[f"% de {nutriente}"][i] / 100 * x[i]
                    for i in range(nfertilizantes)
                ]
            )
            >= necesidades[nutriente]
        )

    # Resolvemos el modelo
    model.solve()

    # Imprimimos la solución y la diferencia
    N_tot = 0
    P_tot = 0
    K_tot = 0
    amount = []
    Fertiliz = []
    fertilizers = []
    blend = []

    for i in range(nfertilizantes):
        if x[i].value() > 0:
            # print(f"{data['Fertilizante'][i]}: {x[i].value()} gramos por hectárea")
            amount.append(x[i].value())
            Fertiliz.append([data["Fertilizante"][i]])
            N_tot += x[i].value() * data["% de N"][i]
            P_tot += x[i].value() * data["% de P"][i]
            K_tot += x[i].value() * data["% de K"][i]

    for item in Fertiliz:
        string_numbers = item[0].split("-")
        integer_numbers = [int(num) for num in string_numbers]
        fertilizers.append(integer_numbers)

    Diferencia_N = N_tot / 100 - necesidades["N"]
    if Diferencia_N < 0.01 and Diferencia_N > -0.01:
        Diferencia_N = 0.0

    Diferencia_P = P_tot / 100 - necesidades["P"]
    if Diferencia_P < 0.01 and Diferencia_P > -0.01:
        Diferencia_P = 0.0

    Diferencia_K = K_tot / 100 - necesidades["K"]
    if Diferencia_K < 0.01 and Diferencia_K > -0.01:
        Diferencia_K = 0.0

    blend = [Diferencia_N, Diferencia_P, Diferencia_K]

    return (amount, fertilizers, blend)
