"""Módulo de pruebas para la gestión de tareas.

Utiliza pytest para validar el correcto funcionamiento de las operaciones 
de creación, edición, eliminación y manejo de tareas.
"""

import pytest
from src.gt import tareas


class TestTarea:
    def setup_method(self):
        """Se ejecuta antes de cada prueba para reiniciar los datos."""
        tareas.tareas.clear()

    # 🟢 Casos normales
    def test_crear_tarea_normal_1(self):
        """Crear una tarea con datos válidos"""
        assert tareas.crear_tarea("usuario1", "Comprar leche", "Ir al supermercado")

    def test_crear_tarea_normal_2(self):
        """Crear otra tarea diferente"""
        assert tareas.crear_tarea("usuario1", "Hacer ejercicio", "Entrenar por 30 min")

    def test_crear_tarea_normal_3(self):
        """Crear una tercera tarea"""
        assert tareas.crear_tarea("usuario1", "Estudiar", "Revisar apuntes de matemáticas")

    # 🔴 Casos de error
    def test_crear_tarea_error_1(self):
        """Error: usuario vacío"""
        assert not tareas.crear_tarea("", "Tarea 1", "Descripción")

    def test_crear_tarea_error_2(self):
        """Error: título de la tarea vacío"""
        assert not tareas.crear_tarea("usuario1", "", "Descripción válida")

    def test_crear_tarea_error_3(self):
        """Error: descripción vacía"""
        assert not tareas.crear_tarea("usuario1", "Título válido", "")

    # ⚠️ Casos extremos
    def test_crear_tarea_extremo_1(self):
        """Extremo: título de la tarea con 1000 caracteres"""
        titulo_largo = "A" * 1000
        assert tareas.crear_tarea("usuario1", titulo_largo, "Descripción normal")

    def test_crear_tarea_extremo_2(self):
        """Extremo: descripción con 5000 caracteres"""
        descripcion_larga = "B" * 5000
        assert tareas.crear_tarea("usuario1", "Tarea con mucha info", descripcion_larga)

    def test_crear_tarea_extremo_3(self):
        """Extremo: usuario con nombre de 50 caracteres"""
        usuario_largo = "u" * 50
        assert tareas.crear_tarea(usuario_largo, "Tarea", "Descripción")

    # 🟢 Casos normales de edición
    def test_editar_tarea_normal_1(self):
        tareas.crear_tarea("usuario1", "Tarea 1", "Descripción 1")
        assert tareas.editar_tarea("usuario1", 0, "Tarea Editada", "Nueva descripción")

    def test_editar_tarea_normal_2(self):
        tareas.crear_tarea("usuario1", "Tarea 2", "Otra descripción")
        assert tareas.editar_tarea("usuario1", 0, "Tarea 2 Editada", "Descripción mejorada")

    def test_editar_tarea_normal_3(self):
        tareas.crear_tarea("usuario1", "Tarea 3", "Algo para hacer")
        assert tareas.editar_tarea("usuario1", 0, "Tarea Modificada", "Cambio pequeño")

    # 🔴 Casos de error en edición
    def test_editar_tarea_error_1(self):
        """Error: editar una tarea inexistente"""
        assert not tareas.editar_tarea("usuario1", 99, "No existe", "Descripción")

    def test_editar_tarea_error_2(self):
        """Error: título vacío"""
        tareas.crear_tarea("usuario1", "Tarea 1", "Descripción")
        assert not tareas.editar_tarea("usuario1", 0, "", "Nueva descripción")

    def test_editar_tarea_error_3(self):
        """Error: usuario no coincide"""
        tareas.crear_tarea("usuario1", "Tarea 1", "Descripción")
        assert not tareas.editar_tarea("usuario2", 0, "Nueva", "Nueva descripción")

    # ⚠️ Casos extremos de edición
    def test_editar_tarea_extremo_1(self):
        """Editar con un título de 1000 caracteres"""
        tareas.crear_tarea("usuario1", "Original", "Descripción")
        titulo_largo = "X" * 1000
        assert tareas.editar_tarea("usuario1", 0, titulo_largo, "Nueva descripción")

    def test_editar_tarea_extremo_2(self):
        """Editar con una descripción de 5000 caracteres"""
        tareas.crear_tarea("usuario1", "Original", "Descripción")
        descripcion_larga = "Y" * 5000
        assert tareas.editar_tarea("usuario1", 0, "Título Editado", descripcion_larga)

    def test_editar_tarea_extremo_3(self):
        """Editar con índice negativo"""
        tareas.crear_tarea("usuario1", "Tarea", "Descripción")
        assert not tareas.editar_tarea("usuario1", -1, "Título", "Descripción")  # Índice inválido

    def test_editar_tarea_extremo_4(self):
        """Editar con índice fuera de rango"""
        tareas.crear_tarea("usuario1", "Tarea", "Descripción")
        assert not tareas.editar_tarea("usuario1", 10, "Título", "Descripción")  # Índice inválido

    # 🟢 Casos normales de eliminación
    def test_eliminar_tarea_normal_1(self):
        """Eliminar una tarea existente"""
        tareas.crear_tarea("usuario1", "Tarea 1", "Descripción")
        assert tareas.eliminar_tarea("usuario1", 0)

    def test_eliminar_tarea_normal_2(self):
        """Eliminar varias tareas en orden"""
        tareas.crear_tarea("usuario1", "Tarea 1", "Descripción")
        tareas.crear_tarea("usuario1", "Tarea 2", "Otra descripción")
        assert tareas.eliminar_tarea("usuario1", 1)  # Elimina la segunda
        assert tareas.eliminar_tarea("usuario1", 0)  # Elimina la primera

    # 🔴 Casos de error en eliminación
    def test_eliminar_tarea_error_1(self):
        """Error: eliminar una tarea inexistente"""
        assert not tareas.eliminar_tarea("usuario1", 99)

    def test_eliminar_tarea_error_2(self):
        """Error: usuario incorrecto"""
        tareas.crear_tarea("usuario1", "Tarea", "Descripción")
        assert not tareas.eliminar_tarea("usuario2", 0)  # Usuario no coincide

    def test_eliminar_tarea_error_3(self):
        """Error: eliminar con índice negativo"""
        tareas.crear_tarea("usuario1", "Tarea", "Descripción")
        assert not tareas.eliminar_tarea("usuario1", -1)

    def test_eliminar_tarea_error_4(self):
        """Error: eliminar con índice fuera de rango"""
        tareas.crear_tarea("usuario1", "Tarea", "Descripción")
        assert not tareas.eliminar_tarea("usuario1", 5)  # Solo hay una tarea

