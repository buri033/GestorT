# tareas.py - Manejo de tareas
tareas = {}


def crear_tarea(usuario, titulo, descripcion):
    if not usuario or not titulo or not descripcion:
        return False  # Evitar valores vacíos
    if usuario not in tareas:
        tareas[usuario] = []
    tareas[usuario].append({
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False
    })
    return True


def listar_tareas(usuario):
    return tareas.get(usuario, [])


def editar_tarea(usuario, indice, nuevo_titulo, nueva_descripcion):
    if not nuevo_titulo or not nueva_descripcion:
        return False  # Evitar editar con valores vacíos
    if usuario not in tareas or indice < 0 or indice >= len(tareas[usuario]):
        return False
    tareas[usuario][indice]["titulo"] = nuevo_titulo
    tareas[usuario][indice]["descripcion"] = nueva_descripcion
    return True


def eliminar_tarea(usuario, indice):
    if usuario not in tareas or indice < 0 or indice >= len(tareas[usuario]):
        return False
    del tareas[usuario][indice]
    return True


def marcar_completada(usuario, indice):
    if usuario not in tareas or indice < 0 or indice >= len(tareas[usuario]):
        return False
    tareas[usuario][indice]["completada"] = True
    return True
