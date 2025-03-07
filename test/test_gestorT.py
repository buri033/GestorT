from src.gt import auth
from src.gt import tareas


def setup_module(module):
    """
    Esta función se ejecuta antes de todos los tests. Reseteamos las estructuras globales.
    """
    auth.usuarios.clear()
    tareas.tareas.clear()


def test_crear_cuenta():
    assert auth.crear_cuenta("usuario1", "clave123"), "❌ No se pudo crear la cuenta correctamente."
    assert not auth.crear_cuenta("usuario1", "clave123"), "❌ Se permitió crear un usuario duplicado."


def test_iniciar_sesion():
    assert auth.iniciar_sesion("usuario1", "clave123"), "❌ No se pudo iniciar sesión correctamente."
    assert not auth.iniciar_sesion("usuario1", "claveIncorrecta"), "❌ Se permitió iniciar sesión con clave incorrecta."


def test_cambiar_contraseña():
    assert auth.cambiar_contraseña("usuario1", "clave123", "nueva123"), "❌ Error al cambiar contraseña."
    assert not auth.cambiar_contraseña("usuario1", "claveIncorrecta",
                                       "otraClave"), "❌ Se permitió cambiar con clave incorrecta."


def test_crear_tarea():
    assert tareas.crear_tarea("usuario1", "Tarea 1", "Descripción 1"), "❌ Error al crear tarea."
    assert len(tareas.listar_tareas("usuario1")) == 1, "❌ No se agregó correctamente la tarea."


def test_editar_tarea():
    assert tareas.editar_tarea("usuario1", 0, "Tarea Editada", "Descripción Editada"), "❌ Error al editar tarea."
    assert not tareas.editar_tarea("usuario1", 99, "Nueva Tarea",
                                   "Nueva Desc"), "❌ Se permitió editar tarea inexistente."


def test_marcar_completada():
    assert tareas.marcar_completada("usuario1", 0), "❌ Error al marcar tarea como completada."
    assert not tareas.marcar_completada("usuario1", 99), "❌ Se permitió marcar completada una tarea inexistente."


def test_eliminar_tarea():
    assert tareas.eliminar_tarea("usuario1", 0), "❌ Error al eliminar tarea."
    assert not tareas.eliminar_tarea("usuario1", 99), "❌ Se permitió eliminar una tarea inexistente."
