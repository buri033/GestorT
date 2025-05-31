from database.db_open_media import get_db_open_media

def obtener_id_usuario(usuario):
    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuarios FROM tbl_usuarios WHERE nombre = %s", (usuario,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None

def crear_tarea(usuario, titulo, descripcion):
    if not usuario or not titulo or not descripcion:
        return False
    id_usuario = obtener_id_usuario(usuario)
    if id_usuario is None:
        return False

    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tbl_tareas (id_tarea, titulo, descripcion, fecha_limite, id_usuarios, id_estado)
        VALUES (DEFAULT, %s, %s, CURRENT_DATE, %s, 2)
    """, (titulo, descripcion, id_usuario))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def listar_tareas(usuario):
    id_usuario = obtener_id_usuario(usuario)
    if id_usuario is None:
        return []

    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT titulo, descripcion, id_estado
        FROM tbl_tareas
        WHERE id_usuarios = %s
    """, (id_usuario,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return [
        {"titulo": row[0], "descripcion": row[1], "completada": row[2] == 1}
        for row in rows
    ]

def editar_tarea(usuario, indice, nuevo_titulo, nueva_descripcion):
    tareas = listar_tareas(usuario)
    if indice < 0 or indice >= len(tareas):
        return False

    tarea = tareas[indice]
    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tbl_tareas SET titulo=%s, descripcion=%s
        WHERE titulo=%s AND descripcion=%s AND id_usuarios=%s
    """, (
        nuevo_titulo, nueva_descripcion,
        tarea["titulo"], tarea["descripcion"],
        obtener_id_usuario(usuario)
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def eliminar_tarea(usuario, indice):
    tareas = listar_tareas(usuario)
    if indice < 0 or indice >= len(tareas):
        return False

    tarea = tareas[indice]
    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM tbl_tareas
        WHERE titulo=%s AND descripcion=%s AND id_usuarios=%s
    """, (
        tarea["titulo"], tarea["descripcion"],
        obtener_id_usuario(usuario)
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def marcar_completada(usuario, indice):
    tareas = listar_tareas(usuario)
    if indice < 0 or indice >= len(tareas):
        return False

    tarea = tareas[indice]
    conn = get_db_open_media()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tbl_tareas SET id_estado = 1
        WHERE titulo=%s AND descripcion=%s AND id_usuarios=%s
    """, (
        tarea["titulo"], tarea["descripcion"],
        obtener_id_usuario(usuario)
    ))
    conn.commit()
    cursor.close()
    conn.close()
    return True
