from habitaciones.Habitacion import Habitacion


class HabitacionSuite(Habitacion):
    def __init__(self, numero, precio_noche=200.0, estado="disponible", huesped="", noches=0):
        descripcion = "Jacuzzi y room service premium (Cargo extra del 10%)."
        super().__init__(numero, "Suite", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        costo_base = self.noches * self.precio_noche
        return costo_base + (costo_base * 0.10)
