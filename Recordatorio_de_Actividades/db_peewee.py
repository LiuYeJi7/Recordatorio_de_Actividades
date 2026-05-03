from peewee import MySQLDatabase, Model, CharField, DateTimeField
import datetime

# 1. Configuración de la conexión a MySQL
db = MySQLDatabase(
    'db_recordatorio', # El nombre exacto que pusiste en phpMyAdmin
    user='root',
    password='',
    host='127.0.0.1',
    port=3306
)

# 2. Definición del Modelo (La tabla de tareas)
class Tarea(Model):
    nombre = CharField()
    descripcion = CharField()
    fecha_creacion = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

# 3. Función para crear la tabla
def conectar_y_crear():
    try:
        if db.is_closed():
            db.connect()
        db.create_tables([Tarea])
        print("¡CONEXIÓN EXITOSA! La tabla 'Tarea' se ha creado en MySQL.")
    except Exception as e:
        print(f"Hubo un error: {e}")

if __name__ == "__main__":
    conectar_y_crear()