from habitaciones.Habitacion import Habitacion


class HabitacionEjecutiva(Habitacion):
    def __init__(self, numero, precio_noche=120.0, estado="disponible", huesped="", noches=0):
        descripcion = "Ideal para negocios. Escritorio y acceso al Lounge (Cargo extra de $25)."
        super().__init__(numero, "Ejecutiva", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return (self.noches * self.precio_noche) + 25.0
