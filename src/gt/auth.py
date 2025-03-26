"""Módulo de autenticación.

Este módulo contiene funciones para la gestión de cuentas de usuario, 
como la creación de cuentas, inicio de sesión y cambio de contraseña.
"""

usuarios = {}


def crear_cuenta(usuario, contraseña):
    """Crea una nueva cuenta de usuario.

    Verifica que el usuario y la contraseña no estén vacíos y que el usuario no exista previamente.

    Parámetros:
        usuario (str): Nombre del usuario a crear.
        contraseña (str): Contraseña del usuario.

    Retorna:
        bool: True si la cuenta se creó exitosamente, False en caso contrario.
    """
    if not usuario or not contraseña:  # Evitar usuarios o contraseñas vacíos
        return False
    if usuario in usuarios:
        return False
    usuarios[usuario] = contraseña
    return True


def iniciar_sesion(usuario, contraseña):
    """Verifica las credenciales de un usuario.

    Parámetros:
        usuario (str): Nombre del usuario.
        contraseña (str): Contraseña del usuario.

    Retorna:
        bool: True si las credenciales son correctas, False en caso contrario.
    """
    return usuarios.get(usuario) == contraseña


def cambiar_contraseña(usuario, actual, nueva):
    """Cambia la contraseña de un usuario.

    Verifica que la contraseña actual sea correcta antes de realizar el cambio.

    Parámetros:
        usuario (str): Nombre del usuario.
        actual (str): Contraseña actual del usuario.
        nueva (str): Nueva contraseña que se desea establecer.

    Retorna:
        bool: True si el cambio se realizó correctamente, False en caso contrario.
    """
    if usuarios.get(usuario) != actual:
        return False
    usuarios[usuario] = nueva
    return True
