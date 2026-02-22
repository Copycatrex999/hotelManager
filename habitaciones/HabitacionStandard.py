
from habitaciones.Habitacion import Habitacion


class HabitacionStandard(Habitacion):
    def __init__(self, numero: str, precio_noche: float = 50.0, estado: str = "disponible",
                 huesped: str = "", noches: int = 0) -> None:
        descripcion: str = "Habitación cómoda con cama matrimonial y TV por cable."
        super().__init__(numero, "Standard", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self) -> float:
        return float(self.noches * self.precio_noche)