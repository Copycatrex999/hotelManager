import json
import os


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


class HabitacionStandard(Habitacion):
    def __init__(self, numero, precio_noche=50.0, estado="disponible", huesped="", noches=0):
        descripcion = "Habitación cómoda con cama matrimonial y TV por cable."
        super().__init__(numero, "Standard", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return self.noches * self.precio_noche


class HabitacionDeluxe(Habitacion):
    def __init__(self, numero, precio_noche=80.0, estado="disponible", huesped="", noches=0):
        descripcion = "Cama King size, balcón con vista y minibar (Cargo extra de $15)."
        super().__init__(numero, "Deluxe", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return (self.noches * self.precio_noche) + 15.0


class HabitacionEjecutiva(Habitacion):
    def __init__(self, numero, precio_noche=120.0, estado="disponible", huesped="", noches=0):
        descripcion = "Ideal para negocios. Escritorio y acceso al Lounge (Cargo extra de $25)."
        super().__init__(numero, "Ejecutiva", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return (self.noches * self.precio_noche) + 25.0


class HabitacionSuite(Habitacion):
    def __init__(self, numero, precio_noche=200.0, estado="disponible", huesped="", noches=0):
        descripcion = "Jacuzzi y room service premium (Cargo extra del 10%)."
        super().__init__(numero, "Suite", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        costo_base = self.noches * self.precio_noche
        return costo_base + (costo_base * 0.10)


class HabitacionPresidencial(Habitacion):
    def __init__(self, numero, precio_noche=500.0, estado="disponible", huesped="", noches=0):
        descripcion = "Penthouse completo con chef privado (Cargo extra de $100)."
        super().__init__(numero, "Presidencial", precio_noche, descripcion, estado, huesped, noches)

    def calcular_total(self):
        return (self.noches * self.precio_noche) + 100.0


# ==========================================
# CLASE DEL SISTEMA HOTELERO (Controlador)
# ==========================================
class Hotel:
    def __init__(self, archivo_json="habitaciones.json"):
        self.archivo_json = archivo_json
        self.habitaciones = {}
        self._cargar_datos()

    def _inicializar_datos(self, forzar=False):
        if forzar or not os.path.exists(self.archivo_json):
            datos_iniciales = {
                "101": {"tipo": "Standard", "precio_noche": 50.0, "estado": "disponible", "huesped": "", "noches": 0},
                "102": {"tipo": "Deluxe", "precio_noche": 80.0, "estado": "disponible", "huesped": "", "noches": 0},
                "201": {"tipo": "Ejecutiva", "precio_noche": 120.0, "estado": "disponible", "huesped": "", "noches": 0},
                "202": {"tipo": "Suite", "precio_noche": 200.0, "estado": "disponible", "huesped": "", "noches": 0},
                "301": {"tipo": "Presidencial", "precio_noche": 500.0, "estado": "disponible", "huesped": "",
                        "noches": 0}
            }
            with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
                json.dump(datos_iniciales, archivo, indent=4, ensure_ascii=False)

    def _cargar_datos(self):
        self._inicializar_datos()
        try:
            with open(self.archivo_json, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for numero, info in datos.items():
                    tipo = info.get("tipo", "Standard")
                    precio = info.get("precio_noche", 50.0)
                    estado = info.get("estado", "disponible")
                    huesped = info.get("huesped", "")
                    noches = info.get("noches", 0)

                    if tipo == "Standard":
                        hab = HabitacionStandard(numero, precio, estado, huesped, noches)
                    elif tipo == "Deluxe":
                        hab = HabitacionDeluxe(numero, precio, estado, huesped, noches)
                    elif tipo == "Ejecutiva":
                        hab = HabitacionEjecutiva(numero, precio, estado, huesped, noches)
                    elif tipo == "Suite":
                        hab = HabitacionSuite(numero, precio, estado, huesped, noches)
                    elif tipo == "Presidencial":
                        hab = HabitacionPresidencial(numero, precio, estado, huesped, noches)
                    else:
                        hab = HabitacionStandard(numero, precio, estado, huesped, noches)

                    self.habitaciones[numero] = hab
        except (json.JSONDecodeError, AttributeError):
            print("\n⚠️ ERROR: Archivo corrupto. Restaurando...")
            self._inicializar_datos(forzar=True)
            self._cargar_datos()

    def guardar_datos(self):
        datos_a_guardar = {numero: hab.to_dict() for numero, hab in self.habitaciones.items()}
        with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)

    def _leer_cadena(self, mensaje):
        while True:
            texto = input(mensaje).strip()
            if texto:
                return texto
            print("❌ Error: Este campo no puede estar vacío.")

    def _leer_entero(self, mensaje, minimo=1):
        while True:
            try:
                numero = int(input(mensaje).strip())
                if numero >= minimo:
                    return numero
                else:
                    print(f"❌ Error: Debe ingresar un número mayor o igual a {minimo}.")
            except ValueError:
                print("❌ Error: Por favor, ingrese un número válido.")

    def mostrar_todas_las_habitaciones(self):
        print("\n=== TODAS LAS HABITACIONES ===")
        for habitacion in self.habitaciones.values():
            print(habitacion)
        print("==============================")

    def mostrar_habitaciones_disponibles(self):
        print("\n=== HABITACIONES DISPONIBLES ===")
        hay_disponibles = False
        for habitacion in self.habitaciones.values():
            if habitacion.esta_disponible():
                print(habitacion)
                hay_disponibles = True
        if not hay_disponibles:
            print("❌ No hay habitaciones disponibles.")
        print("================================")
        return hay_disponibles

    def hacer_check_in(self):
        if not self.mostrar_habitaciones_disponibles():
            return

        while True:
            num_hab = input("\nIngrese el número de la habitación (o 'X' para cancelar): ").strip().upper()
            if num_hab == 'X':
                print("➡️ Operación cancelada. Regresando al menú.")
                return
            if num_hab in self.habitaciones:
                habitacion = self.habitaciones[num_hab]
                if habitacion.esta_disponible():
                    break
                else:
                    print("❌ La habitación ya está ocupada. Elija otra.")
            else:
                print("❌ Número de habitación incorrecto. Intente de nuevo.")

        nombre = self._leer_cadena("Ingrese el nombre del huésped: ").title()
        noches = self._leer_entero("Ingrese la cantidad de noches: ", minimo=1)

        habitacion.ocupar(nombre, noches)
        self.guardar_datos()
        print(f"\n✅ CHECK-IN EXITOSO: La habitación {num_hab} ahora está ocupada por {nombre}.")

    def hacer_check_out(self):
        while True:
            num_hab = input(
                "\nIngrese el número de la habitación para Check-out (o 'X' para cancelar): ").strip().upper()
            if num_hab == 'X':
                print("➡️ Operación cancelada. Regresando al menú.")
                return
            if num_hab in self.habitaciones:
                habitacion = self.habitaciones[num_hab]
                if not habitacion.esta_disponible():
                    break
                else:
                    print("❌ La habitación está vacía.")
            else:
                print("❌ Número de habitación incorrecto.")

        total = habitacion.calcular_total()
        print("\n🧾 === RECIBO DE CHECK-OUT ===")
        print(f"Huésped:   {habitacion.huesped}")
        print(f"Habitación: {habitacion.numero} ({habitacion.tipo})")
        print(f"Estadía:   {habitacion.noches} noches a ${habitacion.precio_noche} c/u")
        print(f"TOTAL A PAGAR: ${total:.2f}")
        print("==============================")

        habitacion.liberar()
        self.guardar_datos()
        print(f"✅ Check-out exitoso. Habitación {num_hab} liberada.")


# ==========================================
# CLASE MENU (Interfaz de Usuario)
# ==========================================
class Menu:
    """Clase que controla la interfaz de la terminal."""

    def __init__(self):
        self.mi_hotel = Hotel()
        self.ejecutar_menu()  # Llama al bucle automáticamente al instanciar la clase

    def ejecutar_menu(self):
        while True:
            print("\n🏨 === SISTEMA DE GESTIÓN HOTELERA === 🏨")
            print("1. Ver TODAS las habitaciones")
            print("2. Ver habitaciones DISPONIBLES")
            print("3. Realizar Check-in")
            print("4. Realizar Check-out (Salida y cobro)")
            print("5. Salir")

            opcion = input("Seleccione una opción (1-5): ").strip()

            if opcion == "1":
                self.mi_hotel.mostrar_todas_las_habitaciones()
            elif opcion == "2":
                self.mi_hotel.mostrar_habitaciones_disponibles()
            elif opcion == "3":
                self.mi_hotel.hacer_check_in()
            elif opcion == "4":
                self.mi_hotel.hacer_check_out()
            elif opcion == "5":
                print("Saliendo del sistema... ¡Hasta pronto!")
                break
            else:
                print("❌ Opción inválida. Por favor teclee un número del 1 al 5.")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    m_v_menu = Menu()  # ¡ESTA LÍNEA AHORA FUNCIONA PERFECTAMENTE!