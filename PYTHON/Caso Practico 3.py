#!/usr/bin/env python
# coding: utf-8

# ## Ejercicio 1: Flota de Camiones

# In[1]:


def GetNumber(matricula: str) -> int:
    """
    Recibe la matrícula completa (string) con el último carácter corrupto (un número)
    y devuelve solo el número (las 4 primeras cifras) como int.
    
    """
    num_str = matricula[:4]

    if len(num_str) != 4 or not num_str.isdigit():
        raise ValueError(f"Matrícula con formato incorrecto: {matricula}")

    return int(num_str)


def GetLetter(numero: int, letras_intermedias: str) -> str:
    """
    Recibe el número de matrícula y las letras intermedias,
    calcula el módulo 20 y devuelve la matrícula correcta.

    """
    tabla = {
        0: "B",  1: "C",  2: "D",  3: "F",  4: "G",
        5: "H",  6: "J",  7: "K",  8: "L",  9: "M",
        10: "N", 11: "P", 12: "R", 13: "S", 14: "T",
        15: "V", 16: "W", 17: "X", 18: "Y", 19: "Z"
    }

    resto = numero % 20
    letra_final = tabla[resto]

    return f"{numero}{letras_intermedias}{letra_final}"


def main():
    # Diccionario inicial de camiones
    camiones = {
        201: ["Renault", 2020, "3541BW4"],
        202: ["Mercedes", 2018, "9834HJ1"],
        203: ["Volvo", 2005, "6712CK9"],
        204: ["BMW", 2023, "1289LM2"]
    }

    # Corrección de matrículas
    for id_camion, datos in camiones.items():
        matricula = datos[2]

        # 1) Obtener el número
        numero = GetNumber(matricula)

        # 2) Obtener las letras intermedias
        letras_intermedias = matricula[4:-1]

        # 3) Obtener matrícula corregida
        matricula_corregida = GetLetter(numero, letras_intermedias)

        # 4) Actualizar diccionario
        camiones[id_camion][2] = matricula_corregida

    # Mostrar resultado
    print("Diccionario corregido:")
    for k, v in camiones.items():
        print(k, "->", v)

    return camiones


if __name__ == "__main__":
    main()


# ## Ejercicio 2: Lambda Functions

# In[2]:


def main():
    # Lista base del enunciado
    numeros = [1,2,3,4,5,6,7,8,9,10]

    # 2.1 Valores cuadrados:
    # Crear una lista cuyos elementos sean el cuadrado de cada número
    cuadrados = list(map(lambda x: x**2, numeros))
    print("2.1 Cuadrados de 1 a 10:", cuadrados)

    # 2.2 Cuadrados de los números pares:
    # Filtrar pares y elevar al cuadrado
    cuadrados_pares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))
    print("2.2 Cuadrados de los pares:", cuadrados_pares)

    # 2.3 Conteo de letras:
    # Devolver lista con el número de letras de cada palabra
    palabras = ["hola", "programacion", "lambda", "python", "IEP"]
    conteo_letras = list(map(lambda p: len(p), palabras))
    print("2.3 Número de letras por palabra:", conteo_letras)


if __name__ == "__main__":
    main()


# ## Ejercicio 3: Sistema Bancario

# ### 3.1 Método Constructor: definición de atributos 

# In[13]:


from datetime import datetime

class Cliente:
    # contador de clientes del banco para asignar IDs consecutivos
    _contador_clientes = 0

    def __init__(self, nombre: str, apellidos: str, fecha_nacimiento: str):
        """
        fecha_nacimiento entra como string en formato 'YYYY/MM/DD'
        - Se transforma a datetime
        - Se comprueba que el cliente tiene >= 18 años (ValueError si no)
        - Se asigna un id de 6 dígitos con zfill
        - El saldo inicial es 0
        """
        self.nombre = nombre
        self.apellidos = apellidos

        # 1) Convertir string a datetime
        try:
            self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Usa 'YYYY/MM/DD'.")

        # 2) Comprobar edad (365 días por año)
        hoy = datetime.now()
        edad_en_dias = (hoy - self.fecha_nacimiento).days
        edad_en_anios = edad_en_dias / 365

        if edad_en_anios < 18:
            raise ValueError("El cliente debe ser mayor de 18 años.")

        # 3) Asignar ID de 6 dígitos
        Cliente._contador_clientes += 1
        self.id_cliente = str(Cliente._contador_clientes).zfill(6)

        # 4) Saldo inicial
        self.saldo = 0.0


# ### 3.2 Métodos de instancia: saludo, depósitos y retiradas 

# In[9]:


class Cliente(Cliente):  # extendemos la clase anterior
    def saludo(self) -> None:
        print(f"Bienvenido/a al banco, {self.nombre} {self.apellidos}.")
        print(f"Tu saldo actual es: {self.saldo:.2f}€")

    def deposito(self, cantidad: float) -> None:
        if cantidad <= 0:
            print("El depósito debe ser una cantidad positiva.")
            return
        self.saldo += cantidad
        print(f"Depósito realizado: +{cantidad:.2f}€ | Saldo: {self.saldo:.2f}€")

    def retirada(self, cantidad: float) -> None:
        if cantidad <= 0:
            print("La retirada debe ser una cantidad positiva.")
            return

        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Retirada realizada: -{cantidad:.2f}€ | Saldo: {self.saldo:.2f}€")
        else:
            print("Operación no permitida: saldo insuficiente.")


# ### 3.3 Realizar transferencias

# In[10]:


def transferencia(emisor: Cliente, receptor: Cliente, cantidad: float) -> None:
    """
    - emisor: cliente que envía
    - receptor: cliente que recibe
    - cantidad: dinero a transferir
    Comprueba que el emisor tiene saldo suficiente, descuenta e ingresa.
    """
    if cantidad <= 0:
        print("La transferencia debe ser una cantidad positiva.")
        return

    if emisor.saldo >= cantidad:
        emisor.saldo -= cantidad
        receptor.saldo += cantidad
        print(
            f"Transferencia OK: {emisor.nombre} -> {receptor.nombre} | "
            f"{cantidad:.2f}€"
        )
        print(f"Saldo emisor: {emisor.saldo:.2f}€ | Saldo receptor: {receptor.saldo:.2f}€")
    else:
        print("Transferencia cancelada: el emisor no tiene saldo suficiente.")


# ### 3.4 Crear clientes y probar el sistema 

# In[18]:


class Cliente:
    _contador_id = 1
    
    def __init__(self, nombre, apellido, fecha_nacimiento):
        from datetime import datetime
        
        # calcular edad según fecha de nacimiento
        fecha_nac = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
        hoy = datetime.now()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        
        # Comprobar si el cliente es mayor de edad
        if edad < 18:
            raise ValueError("El cliente debe ser mayor de edad (18 años)")
            
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.id_cliente = Cliente._contador_id
        Cliente._contador_id += 1
        self.saldo = 0  # Initial balance is 0
    
    def saludo(self):
        # Método para dar la bienvenida e indicar saldo actual
        print(f"\n¡Bienvenido/a {self.nombre} {self.apellido}!")
        print(f"Su saldo actual es: {self.saldo:.2f}€")
    
    def deposito(self, cantidad):
        # Método para depositar dinero
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad:.2f}€ realizado. Nuevo saldo: {self.saldo:.2f}€")
        else:
            print("Error: La cantidad a depositar debe ser positiva")
    
    def retirada(self, cantidad):
        # Método para retirar dinero
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser positiva")
        elif cantidad > self.saldo:
            print(f"Error: Saldo insuficiente. Su saldo actual es: {self.saldo:.2f}€")
        else:
            self.saldo -= cantidad
            print(f"Retirada de {cantidad:.2f}€ realizada. Nuevo saldo: {self.saldo:.2f}€")

def transferencia(origen, destino, cantidad):
    # Función para transferir dinero
    if cantidad <= 0:
        print("Error: La cantidad a transferir debe ser positiva")
        return
    
    if cantidad > origen.saldo:
        print(f"Error: Saldo insuficiente para la transferencia. Saldo actual: {origen.saldo:.2f}€")
        return
    
    origen.saldo -= cantidad
    destino.saldo += cantidad
    print(f"\nTransferencia de {cantidad:.2f}€ realizada")
    print(f"De: {origen.nombre} {origen.apellido} -> A: {destino.nombre} {destino.apellido}")
    print(f"Nuevo saldo de {origen.nombre}: {origen.saldo:.2f}€")
    print(f"Nuevo saldo de {destino.nombre}: {destino.saldo:.2f}€")

def main():
    # 1) Crear tres clientes: 2 mayores de 18 y 1 menor para probar excepción
    try:
        cliente1 = Cliente("Carlos", "Moreno", "1998/07/03")
        cliente2 = Cliente("Sara", "Moreno", "2002/09/27")
        cliente_menor = Cliente("Antonio", "López", "2012/02/11")

    except ValueError as e:
        print("Error al crear cliente:", e)

    # 2) Saludo (bienvenida + saldo)
    cliente1.saludo()
    cliente2.saludo()

    # 3) Depósito y retirada en una cuenta
    cliente1.deposito(200)
    cliente1.retirada(50)

    # 4) Intentar retirada en cuenta sin saldo
    cliente2.retirada(10)

    # 5) Transferencia entre clientes
    transferencia(cliente1, cliente2, 100)

    # 6) Mostrar saldos finales
    print("\nSaldos finales:")
    print(f"{cliente1.nombre} ({cliente1.id_cliente}) -> {cliente1.saldo:.2f}€")
    print(f"{cliente2.nombre} ({cliente2.id_cliente}) -> {cliente2.saldo:.2f}€")


if __name__ == "__main__":
    main()


# ## 4 Ejercicio 4: Análisis de sentimiento

# In[12]:


import string

class AnalisisSentimiento:
    def __init__(self, palabras_positivas=None, palabras_negativas=None):
        """
        Inicializa las listas de palabras positivas y negativas.
        Si no se pasan listas, se usan las de ejemplo del enunciado.
        """
        if palabras_positivas is None:
            palabras_positivas = ["bueno", "excelente"]
        if palabras_negativas is None:
            palabras_negativas = ["malo", "horrible"]

        self.palabras_positivas = palabras_positivas
        self.palabras_negativas = palabras_negativas

    def _limpiar_texto(self, texto: str) -> str:
        """
        Pasa a minúsculas y elimina puntuación básica para mejorar el conteo.
        """
        texto = texto.lower()
        # elimina signos de puntuación comunes
        return texto.translate(str.maketrans("", "", string.punctuation + "¡¿"))

    def _contar_positivas(self, texto: str) -> int:
        """
        Devuelve cuántas palabras positivas aparecen en el texto.
        Se divide el texto por espacios (split(' ')) y se suma count(...) de cada palabra positiva.
        """
        palabras = self._limpiar_texto(texto).split(" ")
        return sum(palabras.count(p) for p in self.palabras_positivas)

    def _contar_negativas(self, texto: str) -> int:
        """
        Devuelve cuántas palabras negativas aparecen en el texto.
        """
        palabras = self._limpiar_texto(texto).split(" ")
        return sum(palabras.count(n) for n in self.palabras_negativas)

    def predict(self, opinion: str) -> str:
        """
        Devuelve 'positiva', 'negativa' o 'neutral' según haya más palabras
        positivas que negativas, viceversa o empate.
        """
        pos = self._contar_positivas(opinion)
        neg = self._contar_negativas(opinion)

        if pos > neg:
            return "positiva"
        elif neg > pos:
            return "negativa"
        else:
            return "neutral"

    def fit(self, nuevas_positivas: list, nuevas_negativas: list) -> None:
        """
        Añade nuevas palabras positivas y negativas al modelo (listas internas).
        """
        # Normalizamos a minúsculas para evitar duplicados por mayúsculas
        nuevas_positivas = [p.lower() for p in nuevas_positivas]
        nuevas_negativas = [n.lower() for n in nuevas_negativas]

        self.palabras_positivas.extend(nuevas_positivas)
        self.palabras_negativas.extend(nuevas_negativas)


def main():
    opiniones = [
        "Me ha parecido una película muy buena",
        "La música es mala, pero la fotografía es buena",
        "No me ha gustado nada, no la recomiendo",
        "El doblaje es pésimo y la trama es muy mala",
        "Excelente película, 100% recomendable",
        "La banda sonora es maravillosa y la trama me gustó"
    ]

    modelo = AnalisisSentimiento()

    print("Predicciones ANTES de fit()")
    for op in opiniones:
        print(f"- {op} -> {modelo.predict(op)}")

    # Mejoramos el modelo añadiendo palabras nuevas
    modelo.fit(
        nuevas_positivas=["maravilloso", "maravillosa", "recomendable", "gustó"],
        nuevas_negativas=["pésimo", "pésima", "mala", "nada"]
    )

    print("\n Predicciones DESPUÉS de fit()")
    for op in opiniones:
        print(f"- {op} -> {modelo.predict(op)}")


if __name__ == "__main__":
    main()

