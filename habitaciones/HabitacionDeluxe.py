from habitaciones.Habitacion import Habitacion


class HabitacionDeluxe(Habitacion):
    def __init__(self, numero, precio_noche=80.0, estado="disponible", huesped="", noches=0):
        descripcion = "Cama King size, balcón con vista y minibar (Cargo extra de $15)."
        super().__init__(numero, "Deluxe", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return (self.noches * self.precio_noche) + 15.0
