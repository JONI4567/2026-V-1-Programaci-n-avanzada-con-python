from panol.insumo import Insumo
from panol.electrica import HerramientaElectrica

inventario = []

print("==================================================")
print("  SISTEMA DE CONTROL DE PAÑOL - TALLER TÉCNICO   ")
print("==================================================")

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar insumo estándar")
    print("2. Registrar máquina o herramienta eléctrica")
    print("3. Listar inventario total")
    print("4. Buscar elemento por código")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre del insumo: ")
        try:
            stock = int(input("Ingrese cantidad de stock disponible: "))
            nuevo_insumo = Insumo(codigo, nombre, stock)
            inventario.append(nuevo_insumo)
            print("Insumo registrado correctamente.")
        except ValueError:
            print("Error: El stock debe ser un número entero.")
        menu()

    elif opcion == "2":
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre de la máquina: ")
        try:
            stock = int(input("Ingrese cantidad de stock disponible: "))
            potencia = float(input("Ingrese potencia nominal en Watts: "))
            nueva_maquina = HerramientaElectrica(codigo, nombre, stock, potencia)
            inventario.append(nueva_maquina)
            print("Herramienta eléctrica registrada correctamente.")
        except ValueError:
            print("Error: Ingrese valores numéricos válidos para stock y potencia.")
        menu()

    elif opcion == "3":
        if len(inventario) == 0:
            print("El inventario del pañol está actualmente vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL DEL PAÑOL ---")
            for item in inventario:
                item.mostrar_datos()
                if isinstance(item, HerramientaElectrica):
                    item.verificar_consumo()
        menu()

    elif opcion == "4":
        codigo_busqueda = input("Ingrese el código a buscar: ")
        encontrado = False
        for item in inventario:
            if item.codigo == codigo_busqueda:
                print("Elemento encontrado:")
                item.mostrar_datos()
                if isinstance(item, HerramientaElectrica):
                    item.verificar_consumo()
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún elemento registrado con ese código.")
        menu()

    elif opcion == "5":
        print("Sesión cerrada. Programa finalizado con éxito.")

    else:
        print("Opción incorrecta. Intente nuevamente.")
        menu()

menu()