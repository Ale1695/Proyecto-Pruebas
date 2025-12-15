import pytest
from reservas import buscar_vuelos, crear_reserva, cancelar_reserva, vuelos, reservas

# def test_buscar_vuelo():
#     r = buscar_vuelos("SJO", "Liberia")  # existe en la oferta de vuelos
#     assert len(r) == 1
#     assert r[0]["destino"] == "Liberia"

# def test_crear_reserva_exitosa():
#     vuelos[0]["asientos"] = 12  # vuelo 1 tiene 12 asientos
#     r = crear_reserva("Alejandro", 1, 2)
#     assert r["total"] == 240  # 120 * 2 = 240
#     assert vuelos[0]["asientos"] == 10  # se reducen los asientos

# def test_crear_reserva_sin_asientos():
#     vuelos[1]["asientos"] = 1
#     with pytest.raises(ValueError):
#         crear_reserva("Luis", 2, 5)  # vuelo 2 tiene solo 1 asiento

# def test_cancelar_reserva_exitosa():
#     vuelos[0]["asientos"] = 12
#     crear_reserva("Sofia", 1, 2)
#     assert cancelar_reserva("Sofia") == True
#     assert vuelos[0]["asientos"] == 12


# def test_cancelar_reserva_inexistente():
#     with pytest.raises(ValueError):
#         cancelar_reserva("PersonaNoExiste")


# # 🔴 1. Fallará porque busca un vuelo que no existe
# def test_buscar_vuelo_inexistente():
#     r = buscar_vuelos("SJO", "Puntarenas")
#     assert len(r) == 1  # ❌ No existe ese destino, len(r)=0

# # 🔴 2. Fallará porque el total esperado es incorrecto
# def test_crear_reserva_total_incorrecto():
#     vuelos[0]["asientos"] = 12
#     r = crear_reserva("Alejandro", 1, 2)
#     assert r["total"] == 999  # ❌ debería ser 240

# # 🔴 3. Fallará porque se lanza un ValueError, pero el test espera True
# def test_cancelar_reserva_inexistente():
#     resultado = cancelar_reserva("ClienteFalso")  # ❌ Lanza ValueError
#     assert resultado == True

# # 🔴 4. Fallará porque espera que los asientos no cambien
# def test_crear_reserva_asientos_no_reducen():
#     vuelos[0]["asientos"] = 12
#     crear_reserva("Luis", 1, 2)
#     assert vuelos[0]["asientos"] == 12  # ❌ después de reservar quedan 10

# # 🔴 5. Fallará porque espera que cancelar sume más asientos de los que había
# def test_cancelar_reserva_suma_extra():
#     vuelos[0]["asientos"] = 12
#     crear_reserva("Sofia", 1, 2)
#     cancelar_reserva("Sofia")
#     assert vuelos[0]["asientos"] == 14  # ❌ debería volver a 12


# Pruba Complementaria

def test_integracion_crear_y_cancelar():
    # Estado inicial
    vuelos[0]["asientos"] = 12

    # Crear reserva
    r = crear_reserva("Daniel", 1, 3)
    assert r["total"] == 360
    assert vuelos[0]["asientos"] == 9  # 12 - 3

    # Cancelar reserva
    cancelar_reserva("Daniel")
    assert vuelos[0]["asientos"] == 12  # ✅ Asientos restaurados correctamente

