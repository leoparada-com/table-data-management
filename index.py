import pandas as pd
import numpy as np
from tabulate import tabulate
# la libreria tabulate permite visualizar las listas como tablas, lo cual resulta util en ciertos problemas

# TABLAS DE DATOS
# -------------------------------------------------------------------------------------------------------------------
# [1] ALTERNATIVA 1: VECTORES INDEPENDIENTES Y POSTERIOR CONSOLIDADO

nombre     = ['Olivia', 'Daniel', 'Juan', 'Germán', 'Eduardo', 'Alejandra', 'Julio','Edgardo', 'Angélica', 'Usaína']
encestadas = [12, 17, 25, np.nan, 25, 19, 13, np.nan, 18, 25]
estatura   = [1.70, 1.90, 1.85, 2.13, 1.78, 2.03, 1.65, 1.79, 1.93, 1.95]
peso       = [81.5, 92.0, 97.7, 115.2, 80, 97.3, 58, 74.5, 88, 94.0]
velocidad  = [14.9, 12.8, 13.6, 10.7, np.nan, 12.8, 13, 12.5, 11.9, 9.6]

atributos  = ['nombre','encestadas','estatura','peso','velocidad']

# funciona con cualquiera de esta alternativas
#A = list(zip(nombre,encestadas,estatura, peso, velocidad))
A = np.transpose([nombre, encestadas, estatura, peso, velocidad])
B = atributos

# ----------------------------------------------------------------------------------------

print(' ')
print(' ---------------------------- EJEMPLO 1 -------------------------------')
print('')
print('DIMENSION DEL ARRAY VANILLA:',len(A),len(A[0]))

candidatos = pd.DataFrame(A, columns = B) # creacion del data frame

print('DIMENSION DEL ARRAY USANDO LIBRERIA PANDAS: ',candidatos.shape)

# ----------------------------------------------------------------------------------------


print(' ')
# tabla comun : vista 1
print(candidatos)
print('')
# tabla usando libreria tabulate : vista 2
print(tabulate(candidatos, headers = atributos, showindex=True, tablefmt='fancy_grid'))
print(' ')

# vista 1
'''
      nombre encestadas estatura   peso velocidad
0     Olivia         12      1.7   81.5      14.9
1     Daniel         17      1.9   92.0      12.8
2       Juan         25     1.85   97.7      13.6
3     Germán        nan     2.13  115.2      10.7
4    Eduardo         25     1.78     80       nan
5  Alejandra         19     2.03   97.3      12.8
6      Julio         13     1.65     58        13
7    Edgardo        nan     1.79   74.5      12.5
8   Angélica         18     1.93     88      11.9
9     Usaína         25     1.95   94.0       9.6
'''

# vista 2

'''
╒════╤═══════════╤══════════════╤════════════╤════════╤═════════════╕
│    │ nombre    │   encestadas │   estatura │   peso │   velocidad │
╞════╪═══════════╪══════════════╪════════════╪════════╪═════════════╡
│  0 │ Olivia    │           12 │       1.7  │   81.5 │        14.9 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  1 │ Daniel    │           17 │       1.9  │   92   │        12.8 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  2 │ Juan      │           25 │       1.85 │   97.7 │        13.6 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  3 │ Germán    │          nan │       2.13 │  115.2 │        10.7 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  4 │ Eduardo   │           25 │       1.78 │   80   │       nan   │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  5 │ Alejandra │           19 │       2.03 │   97.3 │        12.8 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  6 │ Julio     │           13 │       1.65 │   58   │        13   │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  7 │ Edgardo   │          nan │       1.79 │   74.5 │        12.5 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  8 │ Angélica  │           18 │       1.93 │   88   │        11.9 │
├────┼───────────┼──────────────┼────────────┼────────┼─────────────┤
│  9 │ Usaína    │           25 │       1.95 │   94   │         9.6 │
╘════╧═══════════╧══════════════╧════════════╧════════╧═════════════╛

'''

# ======================================================================================================================

# [2] ALTERNATIVA 2: DICCIONARIO DE DATOS

# 1: crear nombre y generar asignacion mediante simbolo =
# 2: Crear llaves {}
# 3: Cambiar signos = por 2 puntos
# 4: Separar por comas cada elemento del diccionario

diccionario = {
'nombre'     : ['Olivia', 'Daniel', 'Juan', 'Germán', 'Eduardo', 'Alejandra', 'Julio','Edgardo', 'Angélica', 'Usaína'],
'encestadas' : [12, 17, 25, np.nan, 25, 19, 13, np.nan, 18, 25],
'estatura'   : [1.70, 1.90, 1.85, 2.13, 1.78, 2.03, 1.65, 1.79, 1.93, 1.95],
'peso'       : [81.5, 92.0, 97.7, 115.2, 80, 97.3, 58, 74.5, 88, 94.0],
'velocidad'  : [14.9, 12.8, 13.6, 10.7, np.nan, 12.8, 13, 12.5, 11.9, 9.6]
}

A = np.transpose(list(diccionario.values()))
B = list(diccionario.keys())

print(' ')
print(' ')
print(' ')
print(' ---------------------------- EJEMPLO 2 -------------------------------')
print(' ')
# ----------------------------------------------------------------------------------------
print('DIMENSION DEL DICCIONARIO:', 'NaN')
candidatos = pd.DataFrame(A, columns = B) # creacion del data frame

print('DIMENSION DEL DICCIONARIO USANDO LIBRERIA PANDAS: ',candidatos.shape)
# ----------------------------------------------------------------------------------------

print(' ')

candidatos = pd.DataFrame(A, columns = B)
print(' ')
# tabla comun
print(candidatos)
print(' ')
print('--------------------- TABULATE EN DICCIONARIO ------------------------')
# tabla usando libreria tabulate
print(tabulate(diccionario, headers = atributos, showindex=True, tablefmt='fancy_grid'))