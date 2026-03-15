from habitaciones.Habitacion import Habitacion


class HabitacionDeluxe(Habitacion):
    def __init__(
        self,
        numero: str,
        precio_noche: float = 80.0,
        estado: str = "disponible",
        huesped: str = "",
        noches: int = 0,
    ) -> None:
        descripcion: str = "Cama King size, balcón con vista y minibar (Cargo extra de $15)."
        super().__init__(numero, "Deluxe", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self) -> float:
        return (self.noches * self.precio_noche) + 15.0
