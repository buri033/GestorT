"""Módulo de pruebas para la gestión de usuarios.

Utiliza pytest para validar el correcto funcionamiento de las operaciones de 
creación de cuenta, inicio de sesión y cambio de contraseña.
"""

import pytest
from src.gt import auth


class TestUsuario:
    def setup_method(self):
        """Se ejecuta antes de cada prueba para reiniciar los datos."""
        auth.usuarios.clear()

    # 🟢 Casos normales
    def test_crear_cuenta_normal_1(self):
        assert auth.crear_cuenta("usuario1", "clave123")

    def test_crear_cuenta_normal_2(self):
        assert auth.crear_cuenta("usuario2", "password456")

    def test_crear_cuenta_normal_3(self):
        assert auth.crear_cuenta("usuario_largo12345", "segura789")

    # 🔴 Casos de error
    def test_crear_cuenta_error_1(self):
        auth.crear_cuenta("usuario1", "clave123")
        assert not auth.crear_cuenta("usuario1", "otraClave")  # Usuario ya existe

    def test_crear_cuenta_error_2(self):
        assert not auth.crear_cuenta("", "clave123")  # Usuario vacío

    def test_crear_cuenta_error_3(self):
        assert not auth.crear_cuenta("usuario3", "")  # Contraseña vacía

    def test_crear_cuenta_error_4(self):
        assert not auth.crear_cuenta(" ", "password")  # Usuario solo con espacios

    def test_crear_cuenta_error_5(self):
        assert not auth.crear_cuenta("usuario?*&$", "claveSegura")  # Caracteres especiales inválidos

    # ⚠️ Casos extremos
    def test_crear_cuenta_extremo_1(self):
        assert auth.crear_cuenta("a", "clave123")  # Usuario de un solo carácter

    def test_crear_cuenta_extremo_2(self):
        assert auth.crear_cuenta("usuario_extremo", "x" * 1000)  # Contraseña muy larga

    def test_crear_cuenta_extremo_3(self):
        assert auth.crear_cuenta("u" * 50, "claveSegura")  # Usuario muy largo

    def test_crear_cuenta_extremo_4(self):
        assert not auth.crear_cuenta("usuario4", "123")  # Contraseña muy corta

    # 🟢 Casos normales de inicio de sesión
    def test_iniciar_sesion_normal_1(self):
        auth.crear_cuenta("usuario1", "clave123")
        assert auth.iniciar_sesion("usuario1", "clave123")

    def test_iniciar_sesion_normal_2(self):
        auth.crear_cuenta("usuario2", "password456")
        assert auth.iniciar_sesion("usuario2", "password456")

    def test_iniciar_sesion_normal_3(self):
        auth.crear_cuenta("usuario3", "miClaveSegura")
        assert auth.iniciar_sesion("usuario3", "miClaveSegura")

    # 🔴 Casos de error de inicio de sesión
    def test_iniciar_sesion_error_1(self):
        auth.crear_cuenta("usuario1", "clave123")
        assert not auth.iniciar_sesion("usuario1", "claveIncorrecta")  # Contraseña incorrecta

    def test_iniciar_sesion_error_2(self):
        assert not auth.iniciar_sesion("usuario_no_existe", "clave123")  # Usuario no existe

    def test_iniciar_sesion_error_3(self):
        auth.crear_cuenta("usuario1", "clave123")
        assert not auth.iniciar_sesion("usuario1", "")  # Contraseña vacía

    def test_iniciar_sesion_error_4(self):
        assert not auth.iniciar_sesion("", "password")  # Usuario vacío

    # 🟢 Casos normales de cambio de contraseña
    def test_cambiar_contraseña_normal_1(self):
        auth.crear_cuenta("usuario1", "clave123")
        assert auth.cambiar_contraseña("usuario1", "clave123", "nuevaClave")

    def test_cambiar_contraseña_normal_2(self):
        auth.crear_cuenta("usuario2", "password456")
        assert auth.cambiar_contraseña("usuario2", "password456", "claveNueva")

    # 🔴 Casos de error en cambio de contraseña
    def test_cambiar_contraseña_error_1(self):
        auth.crear_cuenta("usuario1", "clave123")
        assert not auth.cambiar_contraseña("usuario1", "claveIncorrecta", "nuevaClave")  # Clave incorrecta

    def test_cambiar_contraseña_error_2(self):
        assert not auth.cambiar_contraseña("usuario_no_existe", "clave123", "nuevaClave")  # Usuario no existe

    def test_cambiar_contraseña_error_3(self):
        auth.crear_cuenta("usuario3", "clave123")
        assert not auth.cambiar_contraseña("usuario3", "clave123", "")  # Nueva contraseña vacía

    def test_cambiar_contraseña_error_4(self):
        auth.crear_cuenta("usuario4", "clave123")
        assert not auth.cambiar_contraseña("usuario4", "clave123", "12")  # Nueva contraseña demasiado corta

    def test_cambiar_contraseña_error_5(self):
        auth.crear_cuenta("usuario5", "clave123")
        assert not auth.cambiar_contraseña("usuario5", "", "nuevaClave")  # Contraseña actual vacía
