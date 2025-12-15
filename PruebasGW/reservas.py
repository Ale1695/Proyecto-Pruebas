vuelos = [
    {"id": 1, "origen": "SJO", "destino": "Liberia", "asientos": 12, "precio": 120},
    {"id": 2, "origen": "Liberia", "destino": "SJO", "asientos": 12, "precio": 120},
    {"id": 4, "origen": "SJO", "destino": "Cobano", "asientos": 12, "precio":100},
    {"id": 5, "origen": "Cobano", "destino": "SJO", "asientos": 12, "precio":100}
]

reservas = []

def buscar_vuelos (origen,destino):
    return [v for v in vuelos if v["origen"].upper() == origen.upper() and v["destino"].upper() == destino.upper()]


def crear_reserva(nombre, vuelo_id, asientos):
    for v in vuelos:
        if v["id"] == vuelo_id:
            if asientos > v["asientos"]:
                raise ValueError("No hay suficientes asientos")
            v["asientos"] -= asientos
            total = v["precio"] * asientos
            reserva = {
                "cliente": nombre,
                "vuelo": vuelo_id, 
                "asientos": asientos,
                "total": total
            }
            reservas.append(reserva)
            return reserva
    raise ValueError("Vuelo no encontrado")
    
def cancelar_reserva(nombre):
    for r in reservas:
        if r["cliente"] == nombre:
            # Busca el vuelo asociado a la reserva
            for v in vuelos:
                if v["id"] == r["vuelo"]:  
                    v["asientos"] += r["asientos"]  # ✅ devolver asientos
                    break
            reservas.remove(r)
            return True
    raise ValueError("Reserva no encontrada")


def obtener_reservas():
    return reservas

        
