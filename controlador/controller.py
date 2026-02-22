import os
import json
from typing import Dict, Any, Union, Optional

from habitaciones import Habitacion
from habitaciones.HabitacionDeluxe import HabitacionDeluxe
from habitaciones.HabitacionEjecutiva import HabitacionEjecutiva
from habitaciones.HabitacionPresidencial import HabitacionPresidencial
from habitaciones.HabitacionStandard import HabitacionStandard
from habitaciones.HabitacionSuite import HabitacionSuite
# ==========================================
# Controlador
# ==========================================


class Controlador:
    def __init__(self, archivo_json="habitaciones.json")-> None:
        self.archivo_json = archivo_json
        self.habitaciones = {}
        self._cargar_datos()

    def _inicializar_datos(self, forzar: bool = False):
        """Crea el archivo JSON con datos por defecto. Si 'forzar' es True, lo sobreescribe."""
        if forzar or not os.path.exists(self.archivo_json):
            datos_iniciales: Dict[str, Dict[str, Any]] = {
                "101": {"tipo": "Standard", "precio_noche": 50.0, "estado": "disponible", "huesped": "", "noches": 0},
                "102": {"tipo": "Deluxe", "precio_noche": 80.0, "estado": "disponible", "huesped": "", "noches": 0},
                "201": {"tipo": "Ejecutiva", "precio_noche": 120.0, "estado": "disponible", "huesped": "", "noches": 0},
                "202": {"tipo": "Suite", "precio_noche": 200.0, "estado": "disponible", "huesped": "", "noches": 0},
                "301": {"tipo": "Presidencial", "precio_noche": 500.0, "estado": "disponible", "huesped": "",
                        "noches": 0}
            }
            with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
                json.dump(datos_iniciales, archivo, indent=4, ensure_ascii=False)

    def _cargar_datos(self)-> None:
        """Intenta cargar el JSON de forma segura. Si está corrupto, lo regenera."""
        self._inicializar_datos()  # Se asegura de que exista antes de leer

        try:
            with open(self.archivo_json, 'r', encoding='utf-8') as archivo:
                datos: Dict[str, Any] = json.load(archivo)
                for numero, info in datos.items():
                    tipo: str = info.get("tipo", "Standard")
                    precio: float = info.get("precio_noche", 50.0)
                    estado: str = info.get("estado", "disponible")
                    huesped: str = info.get("huesped", "")
                    noches: int = info.get("noches", 0)

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
            print("\nERROR: El archivo de base de datos está corrupto. Restaurando a los valores por defecto...")
            self._inicializar_datos(forzar=True)
            self._cargar_datos()  # Reintenta cargar tras reparar

    def guardar_datos(self) -> None:
        datos_a_guardar: Dict[str, Dict[str, Any]] = {numero: hab.to_dict() for numero, hab in self.habitaciones.items()}

        with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)

    # Métodos privados de validación
    def _leer_cadena(self, mensaje:str) -> str:
        """evita que se deje en blanco"""
        while True:
            texto : str = input(mensaje).strip()
            if texto:
                return texto
            print("Error: Este campo no puede estar vacío.")

    def _leer_entero(self, mensaje:str , minimo: int =1):
        """para confirmar que se usen solo numeros enteros positivos"""
        while True:
            try:
                numero : str = int(input(mensaje).strip())
                if numero >= minimo:
                    return numero
                else:
                    print(f" Error: Debe ingresar un número mayor o igual a {minimo}.")
            except ValueError:
                print(" Error: Por favor, ingrese un número válido (ejemplo: 2).")

    # Métodos públicos
    def mostrar_todas_las_habitaciones(self)-> None:
        print("\n=== TODAS LAS HABITACIONES ===")
        for habitacion in self.habitaciones.values():
            print(habitacion)
        print("==============================")

    def mostrar_habitaciones_disponibles(self)-> bool:
        print("\n=== HABITACIONES DISPONIBLES ===")
        hay_disponibles: bool = False
        for habitacion in self.habitaciones.values():
            if habitacion.esta_disponible():
                print(habitacion)
                hay_disponibles = True

        if not hay_disponibles:
            print("No hay habitaciones disponibles.")
        print("================================")
        return hay_disponibles

    def hacer_check_in(self) -> None:
        if not self.mostrar_habitaciones_disponibles():
            return

        # Bucle para asegurar que elija una habitación correcta
        num_hab : str
        while True:
            num_hab = input("\nIngrese el número de la habitación (o 'X' para cancelar): ").strip().upper()

            if num_hab == 'X':
                print(" Operación cancelada. Regresando al menú.")
                return

            if num_hab in self.habitaciones:
                habitacion = self.habitaciones[num_hab]
                if habitacion.esta_disponible():
                    break  # Salimos del bucle si la habitación es válida y libre
                else:
                    print("La habitación ya está ocupada. Elija otra.")
            else:
                print(" Número de habitación incorrecto. Intente de nuevo.")

        # Recopilación de datos validada
        nombre : str = self._leer_cadena("Ingrese el nombre del huésped: ").title()  # .title() pone mayúsculas (Juan Perez)
        noches : int = self._leer_entero("Ingrese la cantidad de noches: ", minimo=1)

        habitacion.ocupar(nombre, noches)
        self.guardar_datos()
        print(f"\n CHECK-IN EXITOSO: La habitación {num_hab} ahora está ocupada por {nombre}.")

    def hacer_check_out(self)-> None:
        # Bucle para asegurar que elija una habitación ocupada correcta
        num_hab: str
        habitacion: Optional[Habitacion]
        while True:
            num_hab = input(
                "\nIngrese el número de la habitación para Check-out (o 'X' para cancelar): ").strip().upper()

            if num_hab == 'X':
                print("Operación cancelada. Regresando al menú.")
                return

            if num_hab in self.habitaciones:
                habitacion = self.habitaciones[num_hab]
                if not habitacion.esta_disponible():
                    break  # Salimos del bucle si la habitación es válida y está ocupada
                else:
                    print(" La habitación está vacía. No hay nadie para hacer Check-out.")
            else:
                print(" Número de habitación incorrecto. Intente de nuevo.")

        total:float = habitacion.calcular_total()

        print("\n === RECIBO DE CHECK-OUT ===")
        print(f"Huésped:   {habitacion.huesped}")
        print(f"Habitación: {habitacion.numero} ({habitacion.tipo})")
        print(f"Estadía:   {habitacion.noches} noches a ${habitacion.precio_noche} c/u")
        print(f"Detalles:  {habitacion.descripcion}")
        print(f"TOTAL A PAGAR: ${total:.2f}")
        print("==============================")

        habitacion.liberar()
        self.guardar_datos()
        print(f" Check-out exitoso. Habitación {num_hab} liberada y datos actualizados.")
