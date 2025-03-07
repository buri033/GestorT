# auth.py - Manejo de autenticación y usuarios
usuarios = {}


def crear_cuenta(usuario, contraseña):
    if usuario in usuarios:
        return False
    usuarios[usuario] = contraseña
    return True


def iniciar_sesion(usuario, contraseña):
    return usuarios.get(usuario) == contraseña


def cambiar_contraseña(usuario, actual, nueva):
    if usuarios.get(usuario) != actual:
        return False
    usuarios[usuario] = nueva
    return True
