from database.db_open_media import get_db_open_media

def crear_cuenta(usuario, contraseña):
    if not usuario or not contraseña:
        return False
    conn = get_db_open_media()
    cursor = conn.cursor()

    # Verifica si ya existe
    cursor.execute("SELECT 1 FROM tbl_usuarios WHERE nombre = %s", (usuario,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return False

    # Crear usuario
    cursor.execute("INSERT INTO tbl_usuarios (id_usuarios, nombre, clave) VALUES (DEFAULT, %s, %s)", (usuario, contraseña))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def iniciar_sesion(usuario, contraseña):
    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM tbl_usuarios WHERE nombre = %s", (usuario,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result and result[0] == contraseña

def cambiar_contraseña(usuario, actual, nueva):
    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("SELECT clave FROM tbl_usuarios WHERE nombre = %s", (usuario,))
    result = cursor.fetchone()

    if not result or result[0] != actual:
        cursor.close()
        conn.close()
        return False

    cursor.execute("UPDATE tbl_usuarios SET clave = %s WHERE nombre = %s", (nueva, usuario))
    conn.commit()
    cursor.close()
    conn.close()
    return True
