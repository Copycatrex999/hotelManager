from habitaciones.Habitacion import Habitacion


class HabitacionEjecutiva(Habitacion):
    def __init__(self, numero: str, precio_noche: float = 120.0, estado: str = "disponible",
                 huesped: str = "", noches: int = 0) -> None:
        descripcion: str = "Ideal para negocios. Escritorio y acceso al Lounge (Cargo extra de $25)."
        super().__init__(numero, "Ejecutiva", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self) -> float:
        return (self.noches * self.precio_noche) + 25.0