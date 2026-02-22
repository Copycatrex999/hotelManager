# ==========================================
# CLASES DE HABITACIONES
# ==========================================
class Habitacion:
    def __init__(self, numero, tipo, precio_noche, descripcion, estado="disponible", huesped="", noches=0):
        self.numero = numero
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.descripcion = descripcion
        self.estado = estado
        self.huesped = huesped
        self.noches = noches

    def esta_disponible(self):
        return self.estado == "disponible"

    def ocupar(self, nombre_huesped, cantidad_noches):
        self.estado = "ocupada"
        self.huesped = nombre_huesped
        self.noches = cantidad_noches

    def liberar(self):
        self.estado = "disponible"
        self.huesped = ""
        self.noches = 0

    def calcular_total(self):
        pass

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "precio_noche": self.precio_noche,
            "estado": self.estado,
            "huesped": self.huesped,
            "noches": self.noches
        }

    def __str__(self):
        texto = f"[{self.numero}] {self.tipo.upper()} - ${self.precio_noche}/noche\n"
        texto += f"      Info: {self.descripcion}\n"
        texto += f"      Estado: {self.estado.upper()}"
        if not self.esta_disponible():
            texto += f" (Huésped: {self.huesped})"
        return texto + "\n"
