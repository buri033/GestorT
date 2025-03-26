# tareas.py - Manejo de tareas
"""Módulo de gestión de tareas.

Este módulo permite crear, listar, editar, eliminar y marcar tareas como completadas para cada usuario.
"""
tareas = {}


def crear_tarea(usuario, titulo, descripcion):
    """Crea una nueva tarea para un usuario.

    Verifica que los campos no estén vacíos y agrega la tarea a la lista del usuario.

    Parámetros:
        usuario (str): Nombre del usuario.
        titulo (str): Título de la tarea.
        descripcion (str): Descripción de la tarea.

    Retorna:
        bool: True si la tarea se creó exitosamente, False en caso contrario.
    """
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
    """Lista las tareas de un usuario.

    Parámetros:
        usuario (str): Nombre del usuario.

    Retorna:
        list: Lista de tareas del usuario o una lista vacía si no existen tareas.
    """
    return tareas.get(usuario, [])


def editar_tarea(usuario, indice, nuevo_titulo, nueva_descripcion):
    """Edita una tarea existente de un usuario.

    Verifica que los nuevos valores no estén vacíos y que el índice de la tarea sea válido.

    Parámetros:
        usuario (str): Nombre del usuario.
        indice (int): Índice de la tarea a editar.
        nuevo_titulo (str): Nuevo título para la tarea.
        nueva_descripcion (str): Nueva descripción para la tarea.

    Retorna:
        bool: True si la tarea se editó correctamente, False en caso contrario.
    """
    if not nuevo_titulo or not nueva_descripcion:
        return False  # Evitar editar con valores vacíos
    if usuario not in tareas or indice < 0 or indice >= len(tareas[usuario]):
        return False
    tareas[usuario][indice]["titulo"] = nuevo_titulo
    tareas[usuario][indice]["descripcion"] = nueva_descripcion
    return True


def eliminar_tarea(usuario, indice):
    """Elimina una tarea de un usuario.

    Verifica que el usuario y el índice sean válidos.

    Parámetros:
        usuario (str): Nombre del usuario.
        indice (int): Índice de la tarea a eliminar.

    Retorna:
        bool: True si la tarea se eliminó correctamente, False en caso contrario.
    """
    if usuario not in tareas or indice < 0 or indice >= len(tareas[usuario]):
        return False
    del tareas[usuario][indice]
    return True


def marcar_completada(usuario, indice):
    """Marca una tarea como completada para un usuario.

    Verifica que el usuario y el índice sean válidos.

    Parámetros:
        usuario (str): Nombre del usuario.
        indice (int): Índice de la tarea a marcar como completada.

    Retorna:
        bool: True si la tarea se marcó correctamente como completada, False en caso contrario.
    """
    if usuario not in tareas or indice < 0 or indice >= len(tareas[usuario]):
        return False
    tareas[usuario][indice]["completada"] = True
    return True
