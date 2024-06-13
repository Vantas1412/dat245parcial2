import mysql.connector

class AgenteBusquedaBD:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def conectar_bd(self):
        self.conexion = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )


    def buscar_datos(self, tabla, columna, valor):
        if not self.conexion:
            print("No hay una conexión establecida a la base de datos.")
            return []

        consulta = f"SELECT * FROM {tabla} WHERE {columna} = '{valor}'"
        return self.ejecutar_consulta(consulta)

    def buscar_datos_avanzado(self, consulta):
        if not self.conexion:
            print("No hay una conexión establecida a la base de datos.")
            return []

        return self.ejecutar_consulta(consulta)

    def ejecutar_consulta(self, consulta):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return []

    def desconectar_bd(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión a la base de datos cerrada.")
        else:
            print("No hay una conexión establecida a la base de datos.")

# Ejemplo de uso con tus datos:
agente = AgenteBusquedaBD(host="localhost", port=8080, user="Aaron", password="12345678", database="p5ia")
agente.conectar_bd()

# Búsqueda básica
columnax = "destino"
valorx = "A"
resultados_basicos = agente.buscar_datos(tabla="conexiones", columna=columnax, valor=valorx)  
print("Resultados básicos:")
print(resultados_basicos)

# Búsqueda avanzada
valor1 = "A"
consulta_avanzada = f"SELECT * FROM conexiones WHERE origen = '{valor1}' AND peso > 18 ORDER BY destino DESC LIMIT 10"  
resultados_avanzados = agente.buscar_datos_avanzado(consulta_avanzada)
print("Resultados avanzados:")
print(resultados_avanzados)

agente.desconectar_bd()
