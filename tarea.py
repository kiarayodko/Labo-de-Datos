import pandas as pd

#armo la matriz normal
matriz = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 25000],
    [45432345, 41, 1, 10000]
]

empleado_01=pd.DataFrame(matriz)


def superanSalarioActividad01 (empleado_01,umbral):
    salario=empleado_01.iloc[:, 3]
    empleados_ricos = empleado_01[salario > umbral].copy()
    return empleados_ricos



"""
¿Cuánto les costó implementar esta función?
mucho
"""
matriz02=[ 
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 25000],
    [45432345, 41, 1, 10000],
    [43967304, 37, 0, 12000],
    [42236276, 36, 0, 18000]
    ]
empleado_02=pd.DataFrame(matriz02)


    
matriz03=[
    [20222333, 20000, 45, 2],
    [33456234, 25000, 40, 0],
    [45432345, 10000, 41, 1],
    [43967304, 12000, 37, 0],
    [42236276, 18000, 36, 0]
]

empleado_03=pd.DataFrame(matriz03)

def superanSalarioActividad03 (empleado_03, umbral):
    salario=empleado_03.iloc[:, 1]
    empleados_ricos = empleado_02[salario > umbral].copy()
    return empleados_ricos

print(superanSalarioActividad03 (empleado_03, 15000))

"""
preguntar como hacer la actividad 4
"""

