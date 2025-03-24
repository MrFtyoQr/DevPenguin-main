import mysql.connector

def conectar_mysql(host, usuario, password, base_de_datos):
    """
    Establece una conexión a una base de datos MySQL.

    Args:
        host (str): La dirección del servidor MySQL.
        usuario (str): El nombre de usuario para la conexión.
        password (str): La contraseña del usuario.
        base_de_datos (str): El nombre de la base de datos a la que conectarse.

    Returns:
        mysql.connector.connection.MySQLConnection: Un objeto de conexión a la base de datos.
        None: Si ocurre un error durante la conexión.
    """
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=usuario,
            password=password,
            database=base_de_datos
        )
        print("Conexión a MySQL exitosa!")
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return None

def ejecutar_consulta(conexion, consulta):
    """
    Ejecuta una consulta SQL en la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): El objeto de conexión a la base de datos.
        consulta (str): La consulta SQL a ejecutar.

    Returns:
        list: Una lista de tuplas con los resultados de la consulta.
        None: Si ocurre un error durante la ejecución de la consulta.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        resultados = cursor.fetchall()  # Obtener todos los resultados
        return resultados
    except mysql.connector.Error as error:
        print(f"Error al ejecutar la consulta: {error}")
        return None
    finally:
        if cursor:
            cursor.close()

def insertar_datos(conexion, consulta, valores):
    """
    Inserta datos en una tabla de la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): El objeto de conexión a la base de datos.
        consulta (str): La consulta SQL de inserción.
        valores (tuple): Una tupla con los valores a insertar.

    Returns:
        int: El ID de la última fila insertada (puedes usar `cursor.lastrowid` para obtenerlo).
        None: Si ocurre un error durante la inserción.
    """
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, valores)
        conexion.commit()  # Guarda los cambios en la base de datos
        return cursor.lastrowid  # Devuelve el ID de la última fila insertada
    except mysql.connector.Error as error:
        print(f"Error al insertar datos: {error}")
        conexion.rollback()  # Deshace los cambios si hay un error
        return None
    finally:
        if cursor:
            cursor.close()

def cerrar_conexion(conexion):
    """
    Cierra la conexión a la base de datos.

    Args:
        conexion (mysql.connector.connection.MySQLConnection): El objeto de conexión a la base de datos.
    """
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")

# Ejemplo de uso
if __name__ == "__main__":
    # Credenciales de la base de datos (CAMBIAR ESTO CON TUS PROPIAS CREDENCIALES)
    host = "localhost"  # Ej: "127.0.0.1", "midominio.com"
    usuario = "root"
    password = "tu_contraseña"  # Reemplaza con tu contraseña
    base_de_datos = "mi_base_de_datos"  # Reemplaza con el nombre de tu base de datos

    # 1. Establecer conexión
    conexion = conectar_mysql(host, usuario, password, base_de_datos)

    if conexion:
        try:
            # 2. Ejecutar consultas
            # Ejemplo de...
            pass
        finally:
            cerrar_conexion(conexion)
