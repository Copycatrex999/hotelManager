from habitaciones.Habitacion import Habitacion


class HabitacionPresidencial(Habitacion):
    def __init__(self, numero, precio_noche=500.0, estado="disponible", huesped="", noches=0):
        descripcion = "Penthouse completo con chef privado (Cargo extra de $100)."
        super().__init__(numero, "Presidencial", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return (self.noches * self.precio_noche) + 100.0

