

from habitaciones.Habitacion import Habitacion



class HabitacionSuite(Habitacion):
    def __init__(self, numero: str, precio_noche: float = 200.0, estado: str = "disponible",
                 huesped: str = "", noches: int = 0) -> None:
        descripcion: str = "Jacuzzi y room service premium (Cargo extra del 10%)."
        super().__init__(numero, "Suite", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self) -> float:
        costo_base: float = self.noches * self.precio_noche
        return costo_base + (costo_base * 0.10)
