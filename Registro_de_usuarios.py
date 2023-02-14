import pyodbc

# Connection string for SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOPDANIEL\SQLSERVER;DATABASE=Registro de usuarios;UID=Grupo_1;PWD=123456789')
cursor = conn.cursor()

#print(conn)

def check_id(id, external_id, email, phone, language, create_user, password, intent):
    if(read_user(id) == None):
        create_User(id, external_id, email, phone, language, create_user, password, intent)
    else:
        print("id existe")

# Crear nuevo usuario
def create_User(id, external_id, email, phone, language, create_user, password, intent):

    cursor.execute("INSERT INTO Table_Estudiantes (ID, ExternalID, UserEmail, UserPhone, Language, CreateUser, CreateDate, UpdateDate, UpdateUser, Password, Intent) VALUES (?, ?, ?, ?, ?, ?, GETDATE(), GETDATE(), ?, ?, ?)",
                   id, external_id, email, phone, language, create_user, create_user, password, intent)
    conn.commit()

# Leer todos los usuARIOS
def read_all_users():
    cursor.execute("SELECT * FROM Table_Estudiantes")
    return cursor.fetchall()

# Leer usuario por id
def read_user(id):
    cursor.execute("SELECT * FROM Table_Estudiantes WHERE ID = ?", id)
    return cursor.fetchone()

# Actualizar correo de los usuarios
def update_email(id, email):
    cursor.execute(f"UPDATE Table_Estudiantes SET UserEmail = ?, UpdateDate = GETDATE(), UpdateUser = 'python_script' WHERE ID = ?", email, id)
    conn.commit()

# Eliminar usuario
def delete_user(id):
    cursor.execute(f"DELETE FROM Table_Estudiantes WHERE ID = ?", 1)
    conn.commit()

# Ejemplo
user_id = 'b1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
check_id(user_id, None, 'test@example.com', '555-555-1212', 'en-US', 'python_script', 'password123', 1)
#print(read_user(user_id))
#update_email(user_id, 'new_email1@example.com')
#print(read_user(user_id))
#delete_user(user_id)
#print(read_all_users())

# Cerrar cursor y conexión
cursor.close()
conn.close()
