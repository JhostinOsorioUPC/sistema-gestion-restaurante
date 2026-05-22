# =====================================================
# VARIABLES GLOBALES
# =====================================================

# Precios de los platos para el proceso de facturación
precios = {
    "Seco de pollo": 15.50,
    "Tallarín rojo": 14.00,
    "Estofado de pollo": 16.00
}

# Historial acumulado del día (opcional, para que Pablo luego haga su reporte)
historial_ventas = []

stock = {
    "Pollo": 20,
    "Arroz": 30,
    "Papa": 25,
    "Fideos": 20,
    "Tomate": 15,
    "Cebolla": 18,
    "Ajo": 10,
    "Aceite": 12,
    "Ají amarillo": 8,
    "Zanahoria": 14,
    "Arvejas": 13,
    "Culantro": 9,
    "Sal": 20
}

platos = {

    "Seco de pollo": {
        "Pollo": 1,
        "Arroz": 1,
        "Papa": 1,
        "Culantro": 1,
        "Cebolla": 1,
        "Ají amarillo": 1
    },

    "Tallarín rojo": {
        "Fideos": 1,
        "Pollo": 1,
        "Tomate": 2,
        "Cebolla": 1,
        "Ajo": 1,
        "Aceite": 1
    },

    "Estofado de pollo": {
        "Pollo": 1,
        "Papa": 1,
        "Zanahoria": 1,
        "Arvejas": 1,
        "Tomate": 1,
        "Cebolla": 1
    }
}

pedidos = [
    "Seco de pollo",
    "Tallarín rojo",
    "Estofado de pollo"
]



# AQUÍ VA LA PARTE DE JEAN PAUL - TOMAR PEDIDO


def tomar_pedido():
    while True:

        print("Que te gustaría pedir? ")

        que_pedir = int(input(
            "Seco de pollo (1), Tallarín rojo (2), "
            "Estofado de pollo (3) o Terminar pedido (0): "
        ))

        
        # SECO DE POLLO
        
        if que_pedir == 1:

            disponible = True

            # VERIFICAR STOCK
            for clave, valor in platos["Seco de pollo"].items():

                if stock[clave] < valor:

                    disponible = False
                    print("No hay suficiente stock de", clave)
                    break

            # DESCONTAR STOCK SOLO SI HAY INSUMOS
            if disponible:

                print("Tu pedido ha sido seleccionado correctamente.")

                for clave, valor in platos["Seco de pollo"].items():

                    stock[clave] -= valor

                print(stock)

            else:

                print("Ya no tenemos disponible ese plato")


        
        # TALLARÍN ROJO
        
        elif que_pedir == 2:

            disponible = True

            # VERIFICAR STOCK
            for clave, valor in platos["Tallarín rojo"].items():

                if stock[clave] < valor:

                    disponible = False
                    print("No hay suficiente stock de", clave)
                    break

            # DESCONTAR STOCK SOLO SI HAY INSUMOS
            if disponible:

                print("Tu pedido ha sido seleccionado correctamente.")

                for clave, valor in platos["Tallarín rojo"].items():

                    stock[clave] -= valor

                print(stock)

            else:

                print("Ya no tenemos disponible ese plato")


        
        # ESTOFADO DE POLLO
        
        elif que_pedir == 3:

            disponible = True

            # VERIFICAR STOCK
            for clave, valor in platos["Estofado de pollo"].items():

                if stock[clave] < valor:

                    disponible = False
                    print("No hay suficiente stock de", clave)
                    break

            
            if disponible:

                print("Tu pedido ha sido seleccionado correctamente.")

                for clave, valor in platos["Estofado de pollo"].items():

                    stock[clave] -= valor

                print(stock)

            else:

                print("Ya no tenemos disponible ese plato")


        
        elif que_pedir == 0:

            print("Gracias por su compra.")
            break


        
        else:

            print(f"Tu variable {que_pedir} es inválida.")

def control_stock():

    while True:

        print("\n╔══════════════════════════════════╗")
        print("║        CONTROL DE STOCK         ║")
        print("╠══════════════════════════════════╣")
        print("║ 1. Ver stock                    ║")
        print("║ 2. Registrar compra             ║")
        print("║ 0. Volver al menú principal     ║")
        print("╚══════════════════════════════════╝")

        opcion = input("Seleccione una opción: ")

        # =====================================
        # VER STOCK
        # =====================================
        if opcion == "1":

            print("\n======= STOCK DISPONIBLE =======")

            for producto, cantidad in stock.items():

                print(producto, ":", cantidad)

                # ALERTA DE STOCK CRÍTICO
                if cantidad <= 1:
                    print("ALERTA: Stock crítico de", producto)

            print("================================")


        # =====================================
        # REGISTRAR COMPRA
        # =====================================
        elif opcion == "2":

            producto = input("Ingrese el nombre del insumo: ")
            cantidad = int(input("Ingrese la cantidad comprada: "))

            # SI EL PRODUCTO YA EXISTE
            if producto in stock:

                stock[producto] += cantidad

            # SI EL PRODUCTO NO EXISTE
            else:

                stock[producto] = cantidad

            print("Compra registrada correctamente.")

            print("\n======= STOCK ACTUALIZADO =======")

            for producto, cantidad in stock.items():

                print(producto, ":", cantidad)

            print("=================================")


        # =====================================
        # VOLVER AL MENÚ PRINCIPAL
        # =====================================
        elif opcion == "0":

            break


        # =====================================
        # OPCIÓN INVÁLIDA
        # =====================================
        else:

            print("Opción inválida")


# =====================================================
# AQUÍ VA LA PARTE DE LIMBERG - FACTURAR MESA
# =====================================================

def facturar_mesa():
    print("\n" + "═"*40)
    print("           FACTURACIÓN DE MESA          ")
    print("═"*40)
    
    # Validación: Si Jean Paul aún no ha agregado nada a la lista de pedidos, no hay nada que cobrar
    if len(pedidos) == 0:
        print(" [!] No hay consumos registrados en este momento.")
        print("═"*40)
        return  # Sale de la función y regresa al menú principal

    subtotal = 0.0
    print(" Detalle del consumo actual:")
    print("-" * 40)
    
    # ESTRUCTURA REPETITIVA: Recorre cada plato que se encuentra en la lista de pedidos
    for plato in pedidos:
        # Busca el precio asignado en nuestro diccionario de precios
        precio_plato = precios[plato]
        print(f" • {plato:<20} : S/. {precio_plato:>6.2f}")
        # Acumulador para obtener la suma de los platos
        subtotal += precio_plato

    print("-" * 40)
    
    # CÁLCULOS DE IGV Y TOTAL A PAGAR
    igv = subtotal * 0.18
    total_pagar = subtotal + igv

    # Impresión de montos formateados a 2 decimales (.2f)
    print(f" Subtotal           : S/. {subtotal:>6.2f}")
    print(f" IGV (18%)           : S/. {igv:>6.2f}")
    print("-" * 40)
    print(f" TOTAL A PAGAR      : S/. {total_pagar:>6.2f}")
    print("═"*40)
    
    # PROCESO DE CIERRE Y LIBERACIÓN (Modifica variables globales en tiempo real)
    confirmar = input("¿Confirmar el pago y cerrar la cuenta? (S/N): ").upper()
    
    if confirmar == "S":
        # Antes de vaciar la mesa, registramos los platos en el historial para el reporte final del día
        for plato in pedidos:
            historial_ventas.append(plato)
            
        # Limpiamos la lista de pedidos (la mesa queda libre y el mozo puede volver a tomar otra orden)
        pedidos.clear()
        print("\n [✓] Cuenta pagada con éxito. Mesa liberada.")
    else:
        print("\n [!] Operación cancelada. El consumo sigue pendiente de pago.")
    
    print("═"*40)


# =====================================================
# AQUÍ VA LA PARTE DE JHOSTIN - COLA DE COCINA
# =====================================================

def cola_cocina():
    pass


# =====================================================
# AQUÍ VA LA PARTE DE PABLO - REPORTE DEL DÍA
# =====================================================

def reporte_dia():
    pass


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

while True:

    print("\n╔══════════════════════════════════╗")
    print("║  SISTEMA - SABOR Y TRADICIÓN    ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Tomar pedido (Jean Paul)    ║")
    print("║  2. Control de stock (Enrique)  ║")
    print("║  3. Facturar mesa (Limberg)     ║")
    print("║  4. Cola de cocina (Jhostin)    ║")
    print("║  5. Reporte del día (Pablo)     ║")
    print("║  0. Salir                       ║")
    print("╚══════════════════════════════════╝")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tomar_pedido()

    elif opcion == "2":
        control_stock()

    elif opcion == "3":
        facturar_mesa()

    elif opcion == "4":
        cola_cocina()

    elif opcion == "5":
        reporte_dia()

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")