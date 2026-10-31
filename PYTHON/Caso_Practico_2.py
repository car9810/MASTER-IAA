#!/usr/bin/env python
# coding: utf-8

# # Ejercicio 1: Don Quijote

# ## 1.1 Sancho vs Dulcinea

# In[26]:


#importamos el archivo en modo lectura

with open("C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/quijote.txt", "r", encoding="utf-8") as fichero:
    texto = fichero.read()

#usamos texto_lower para que no haya problemas con mayúsculas y minúsculas
texto_lower = texto.lower()

#usamos .count para contar el numero de repeticiones
conteo_sancho = texto_lower.count("sancho")
conteo_dulcinea = texto_lower.count("dulcinea")
print (conteo_sancho)
print (conteo_dulcinea)




# ## 1.2 Reescribiendo el Quijote 

# ### Sin list comprehension

# In[27]:


#Nombre que queremos usar en lugar de Quijote
nuevo_nombre = "Manolito"

#Lista donde iremos guardando las líneas modificada
lineas_modificadas = []

#Ruta del archivo original y del archivo de salida
ruta_entrada = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/quijote.txt"
ruta_salida = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/manolito.txt"

#Abrimos el archivo original en modo lectura, leemos todas las líneas del archivo y las guardamos en una lista
with open(ruta_entrada, "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    for linea in lineas:
        #Reemplazamos Quijote por Manolito y guardamos la línea modificada en la nueva lista
        linea_modificada = linea.replace("Quijote", nuevo_nombre)
        lineas_modificadas.append(linea_modificada)
        
#Creamos el archivo de salida
with open(ruta_salida, "w", encoding="utf-8") as salida:
    salida.writelines(lineas_modificadas)
    
#Abrimos una parte del archivo generado para comprobar que se ha hecho el reemplazo
with open(ruta_salida, "r", encoding="utf-8") as f:
        print(f.read(500))


# ### Con list comprehension

# In[73]:


#Nombre que queremos usar en lugar de Quijote
nuevo_nombre = "Manolito"

#Ruta del archivo original y del archivo de salida
ruta_entrada = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/quijote.txt"
ruta_salida = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/manolito.txt"

#Abrimos el archivo original y leemos todas sus líneas
with open(ruta_entrada, "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()

#List comprehension que modifica cada línea
lineas_modificadas = [linea.replace("Quijote", nuevo_nombre) for linea in lineas]

#Creamos el archivo de salida
with open(ruta_salida, "w", encoding="utf-8") as salida:
    salida.writelines(lineas_modificadas)

#Abrimos una parte del archivo generado para comprobar que se ha hecho el reemplaz
with open(ruta_salida, "r", encoding="utf-8") as f:
        print(f.read(500))


# ## 1.3 Conteo de Palabras 

# In[84]:


#Abrimos el txt
ruta_entrada = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/quijote.txt"
with open(ruta_entrada, "r", encoding="utf-8") as fichero:
    lineas = fichero.read()

#Convertimos todo a minusculas
lineas = lineas.lower()

#Limpiamos los signos de puntuacion y los eliminamos (los sustituimos por nada)
signos_puntuacion = ".,;():[]¡!¿?/"
for caracter in signos_puntuacion:
    lineas = lineas.replace(caracter, "")
    
#Generamos la lista de palabras usando split()
palabras = lineas.split()

#Creamos un diccionario vacio
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras: 
        #Si la palabra ya existe, sumamos 1
        conteo_palabras[palabra] += 1
    else:
        # Si no existe, creamos la entrada con valor 1
        conteo_palabras[palabra] = 1 
        
#Usamos Dict Comprehension para filtrar palabras repetidas más de 100 veces
frecuentes = {palabra: cantidad for palabra, cantidad in conteo_palabras.items() if cantidad > 100}

print("Palabras que se repiten más de 100 veces:")
for palabra, cantidad in frecuentes.items():
    print(f"La palabra '{palabra}' aparece {cantidad} veces.")


# # Ejercicio 2: Gestión de Usuarios

# ## 2.1 Registro de Usuarios

# In[9]:


import json

#Creamos diccionario vacio
registro_usuarios = {}

while True:
    #Solicitamos el nombre de usuario
    usuario = input("Introduce nombre de usuario: ").strip()
    
    #Condición de salida del bucle
    if usuario.upper() == "SALIR":
        print("Registro finalizado.")
        break
        
    #Verificamos si el usuario ya existe
    if usuario in registro_usuarios:
        print(f" El usuario '{usuario}' ya existe. Intenta con otro nombre.")
        continue #Vuelve al inicio del bucle
        
    #Solicitamos contraseña
    contraseña = input ("Introduce contraseña: ").strip()

    #Guardamos el nuevo par en el diccionario
    registro_usuarios[usuario]=contraseña
    print(f" Usuario '{usuario}' registrado con éxito.\n")

#Almacenamiento en JSON
archivo = "usuarios.json"

try:
    #Creamos el archivo JSON
    with open(archivo, 'w', encoding='utf-8') as archivo_json:
        # La función json.dump() escribe el diccionario 'usuarios_registrdos'en el archivo abierto.
        json.dump(registro_usuarios, archivo_json)

    print(f"Se han guardado {len(registro_usuarios)} usuarios en '{archivo}'.")
    print(f"Contenido del archivo: {registro_usuarios}")
   
except Exception:
    print(f" Error al intentar guardar el archivo JSON: ")


# ## 2.2 Visualización de Usuarios Registrados: 

# In[17]:


import json
archivo = "usuarios.json"

usuarios_registrados = {}

#Cargar los datos
try:
    with open (archivo, "r", encoding= "utf8") as archivo_json:
        #Cargamos el contenido del archivo JSON y lo convertimos en un diccionario de Python
        usuarios_registrados = json.load(archivo_json)

#Si el archivo no existe, mostramos un mensaje y terminamos el programa
except FileNotFoundError:
    print(f'El archivo {archivo} no ha sido encontrado.')
#Si el archivo existe pero su contenido no es válido JSON
except json.JSONDecodeError: 
    print(f'El archivo {archivo} no es válido.')
    
print ("Listado de nombres: ")
#List comprehension para extraer todas las claves del diccionario en una lista nueva
nombres = [nombre for nombre in usuarios_registrados.keys()]
print (nombres)
    


# ## 2.3  Inicio de Sesión:

# In[25]:


import json
archivo = "usuarios.json"
numero_intentos = 3


usuarios_registrados = {}

#Cargamos los datos
try:
    with open (archivo, "r", encoding= "utf8") as archivo_json:
        #Cargamos el diccionario desde el archivo JSON
        usuarios_registrados = json.load(archivo_json)
except FileNotFoundError:
    print(f'El archivo {archivo} no ha sido encontrado.')
except json.JSONDecodeError: 
    print(f'El archivo {archivo} no es válido.')

#El bucle se ejecutará 3 veces
for intento in range (numero_intentos):
    #Calculamos los intentos restantes
    intentos_restantes = 3 - (intento + 1)

    #solicitamos nombre y contraseña
    usuario_ingresado = input ('Usuario: ').strip()
    contraseña_ingresada = input ('Contraseña: ').strip()

    #Verificación de credenciales segura con .get
    contraseña_almacenada = usuarios_registrados.get(usuario_ingresado)

    #Verificamos si la contraseña almacenada existe y si la contraseña ingresada coincide con la almacenada
    if contraseña_almacenada is not None and contraseña_ingresada == contraseña_almacenada:
        print ("¡Bienvenido!")
        break
    else:
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas. Le quedan {intentos_restantes} intentos.")
        else:
            print ("Límite de intentos alcanzado. Acceso denegado.")


# ## 2.4 Utilización de archivos binarios 

# In[25]:


import pickle

#Inicialización del diccionario de usuarios
usuarios_registrados = {}
nombre_archivo = "usuarios.pkl"

#Bucle para el registro interactivo
while True:
    usuario = input("Introduce nombre de usuario: ").strip()

    #Condición de salida del bucle
    if usuario.upper() == "SALIR":
        print("Registro finalizado.")
        break

    if usuario in usuarios_registrados:
        print(f"El usuario '{usuario}' ya existe. Intenta con otro nombre.")
        continue

    contrasena = input("Introduce contraseña: ").strip()

    #Almacenamos el nuevo par en el diccionario
    usuarios_registrados[usuario] = contrasena
    print(f"Usuario '{usuario}' registrado con éxito.\n")


#Almacenamiento de la información en formato binario con pickle
try:
    #Abrimos el archivo en modo escritura binaria ('wb')
    with open(nombre_archivo, 'wb') as archivo_binario:
        #pickle.dump() serializa el diccionario a formato binario
        pickle.dump(usuarios_registrados, archivo_binario)

    print(f"Se han guardado {len(usuarios_registrados)} usuarios en '{nombre_archivo}'.")
    print(f"El archivo '{nombre_archivo}' es binario y no se puede leer directamente.")


except Exception:
    print(f"Error al intentar guardar el archivo binario")
    


# # EJERCICIO 3: VENTAS

# ## 3.1 Total Ventas

# In[14]:


import csv

#Importamos el archivo

ruta_entrada = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/ventas.csv"

#Establecemos un punto de partida para ir acumulando los valores de las ventas
suma_total = 0

#Abrimos el archivo como lista
with open (ruta_entrada, newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)

    #Saltar cabecera
    next(lector)

    #Iterar por las filas
    for fila in lector:
        #El total está en la última fila
        total_venta = float (fila[-1]) 
        suma_total += total_venta
        
print("La suma total de las ventas es:", suma_total)


# ## 3.2 Ventas de Camisetas 

# In[20]:


import csv
ruta_salida = "C:/Users/carte/OneDrive/Documentos/MASTER IA/PYTHON PROGRAMMING/PRACTICA/datos_Unidad2/venta_camisetas.csv"

with open (ruta_entrada, newline="", encoding = "utf-8") as archivo:
    #Convertimos cada fila del CSV en una lista
    lector = csv.reader(archivo)
    #Guardamos la cabecera
    cabecera = next(lector)
    #List comprehension para obtener solo las camisetas
    camisetas = [fila for fila in lector if fila[1] == "Camiseta"]

#Creamos el nuevo CSV con solo camisetas
with open (ruta_salida , "w", newline="", encoding = "utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(cabecera) 
    escritor.writerow(camisetas) 

print("Archivo creado: ventas_camisetas.csv")    


# ## 3.3 Producto más caro 

# In[23]:


import csv

with open(ruta_entrada, newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)  #Saltamos la cabecera

    #Tupla que guardará producto, precio.
    producto_mas_caro = ("", 0)

    for fila in lector:
        producto = fila[1]
        #Precio unitario está en columna 3
        precio = float(fila[3])  

        #Si encontramos un precio más caro, actualizamos la tupla
        if precio > producto_mas_caro[1]:
            producto_mas_caro = (producto, precio)

print("El producto más caro es:", producto_mas_caro)

