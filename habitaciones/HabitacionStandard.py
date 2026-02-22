
from habitaciones.Habitacion import Habitacion


class HabitacionStandard(Habitacion):
    def __init__(self, numero, precio_noche=50.0, estado="disponible", huesped="", noches=0):
        descripcion = "Habitación cómoda con cama matrimonial y TV por cable."
        super().__init__(numero, "Standard", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return self.noches * self.precio_noche
