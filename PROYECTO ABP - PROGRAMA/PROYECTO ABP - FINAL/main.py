#main.py

from gestion_clientes import opcion_clientes
from gestion_destinos import opcion_destinos
from gestion_ventas import opcion_ventas
from gestion_arrepentimiento import opcion_arrepentimiento
from consultas import opcion_consulta

#Inicio de programa con opciones del menu principal
def menu_principal():
    while True:
        print("\n Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes \n")
        print("==== Menu Principal ====")
        print("1. Gestionar Clientes")
        print("2. Gestionar Destinos")
        print("3. Gestionar Ventas")
        print("4. Boton de Arrepentimiento")
        print("5. Consulta de datos")
        print("6. Acerca del Sistema")
        print("7. Salir")
    
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            opcion_clientes()
        elif opcion == "2":
            opcion_destinos()
        elif opcion == "3":
            opcion_ventas()
        elif opcion == "4":
            opcion_arrepentimiento()
        elif opcion == "5":
            opcion_consulta()
        elif opcion == "6":
            print("\n ==== Acerca del sistema ==== \n")
            print("""
                ¡Bienvenidos al sistema de destión de pasajes SkyRoute S.R.L!
                SkyRoute S.R.L es un sistema desarrollado como parte de un proyecto academico,
                con el propósito de simular el funcionamiento de una agencia de pasajes aéreos.
                Aquí se pueden registrar diferentes tipos de clientes, tanto empresas como
                personas físicas, gestionar destinos con sus respectivos costos y asociar cada
                venta a un cliente y destino específico.
                Además, incorpora la función del “botón de arrepentimiento”, que simula el
                derechodel usuario a cancelar una compra dentro de un plazo determinado, en
                línea con la normativa de defensa al consumidor.""")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

# Ejecuta el menú principal solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    menu_principal()