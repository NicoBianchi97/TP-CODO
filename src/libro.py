import mysql.connector

# Conexión a la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'librosdb',
    'port': 3306
}


class Libro:
    def __init__(self, id_libros=None, nombre_libro=None, autor=None, precio=None, genero=None, imagen=None):
        self.id_libros = id_libros
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.precio = precio
        self.genero = genero
        self.imagen = imagen
     
     #Conexión a la base de datos  
    def save(self):
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor() #Se crea un cursor para ejecutar las consultas SQL

        if self.id_libros:
            # Actualizar el libro existente. Si self.id_libros está definido, se ejecuta una consulta UPDATE para actualizar el registro existente.
            query = """
            UPDATE libros
            SET nombre_libro = %s, autor = %s, precio = %s, genero = %s, imagen = %s
            WHERE id_libros = %s
            """
            values = (self.nombre_libro, self.autor, self.precio, self.genero, self.imagen, self.id_libros)
        else:
            # Insertar un nuevo libro. Si self.id_libros no está definido, se ejecuta una consulta INSERT para insertar un nuevo registro.
            query = """
            INSERT INTO libros (nombre_libro, autor, precio, genero, imagen)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (self.nombre_libro, self.autor, self.precio, self.genero, self.imagen)
        
        cursor.execute(query, values)
        db.commit() #Guarda los cambios en la base de datos

        if not self.id_libros: #Comprueba si el objeto Libro aún no tiene un ID asignado
            self.id_libros = cursor.lastrowid #Devuelve el valor del último ID que se ha generado automáticamente 

        cursor.close()
        db.close()

    @staticmethod #Obtiene todas las peliculas
    def get_all():
        db = mysql.connector.connect(**DB_CONFIG) #Conexión a la base de datos
        cursor = db.cursor(dictionary=True) #Se crea un cursor en modo diccionario (dictionary=True) para ejecutar las consultas SQL.
        
        query = "SELECT * FROM libros"
        cursor.execute(query)
        result = cursor.fetchall() #Se obtienen todos los registros usando cursor.fetchall()
        
        cursor.close()
        db.close()
        
        return result
    
    @staticmethod #Obtiene peliculas por el id
    def get_by_id(id_libros):
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor(dictionary=True) #obteniene el resultado como un diccionario
        
        query = "SELECT * FROM libros WHERE id_libros = %s"
        cursor.execute(query, (id_libros,))
        row = cursor.fetchone() #Recupera una sola fila del resultado de la consulta
        
        cursor.close()
        db.close()
        
        return Libro(**row) if row else None #Crea una instancia de Libro a partir de un diccionario y asegura que solo se intente crear una instancia si hay datos disponibles, devolviendo None si no hay datos

    @staticmethod
    def delete(id_libros):
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        
        query = "DELETE FROM libros WHERE id_libros = %s"
        cursor.execute(query, (id_libros,))
        db.commit()
        
        cursor.close()
        db.close()