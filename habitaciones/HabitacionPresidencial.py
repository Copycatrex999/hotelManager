
from habitaciones.Habitacion import Habitacion


class HabitacionPresidencial(Habitacion):
    def __init__(self, numero: str, precio_noche: float = 500.0, estado: str = "disponible",
                 huesped: str = "", noches: int = 0) -> None:
        descripcion: str = "Penthouse completo con chef privado (Cargo extra de $100)."
        super().__init__(numero, "Presidencial", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self) -> float:
        return (self.noches * self.precio_noche) + 100.0