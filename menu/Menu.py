from controlador.controller import Controlador

# ==========================================
# CLASE MENU (Interfaz de Usuario)
# ==========================================

class menu:
    """Clase que controla la interfaz de la terminal."""

    def __init__(self):
        self.hotel = Controlador()
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
                self.hotel.mostrar_todas_las_habitaciones()
            elif opcion == "2":
                self.hotel.mostrar_habitaciones_disponibles()
            elif opcion == "3":
                self.hotel.hacer_check_in()
            elif opcion == "4":
                self.hotel.hacer_check_out()
            elif opcion == "5":
                print("Saliendo del sistema... ¡Hasta pronto!")
                break
            else:
                print(" Opción inválida. Por favor teclee un número del 1 al 5.")
