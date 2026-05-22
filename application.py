# =====================================================
# VARIABLES GLOBALES
# =====================================================

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
        "ingredientes": {
            "Pollo": 1,
            "Arroz": 1,
            "Papa": 1,
            "Culantro": 1,
            "Cebolla": 1,
            "Ají amarillo": 1
        },
        "precio": 15.50,
        "tiempo_prep": 12
    },

    "Tallarín rojo": {
        "ingredientes": {
            "Fideos": 1,
            "Pollo": 1,
            "Tomate": 2,
            "Cebolla": 1,
            "Ajo": 1,
            "Aceite": 1
        },
        "precio": 14.00,
        "tiempo_prep": 10
    },

    "Estofado de pollo": {
        "ingredientes": {
            "Pollo": 1,
            "Papa": 1,
            "Zanahoria": 1,
            "Arvejas": 1,
            "Tomate": 1,
            "Cebolla": 1
        },
        "precio": 16.00,
        "tiempo_prep": 15
    }
}

pedidos = [
    {"plato": "Seco de pollo",      "estado": "Pendiente"},
    {"plato": "Tallarín rojo",      "estado": "Pendiente"},
    {"plato": "Estofado de pollo",  "estado": "Pendiente"}
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
            for clave, valor in platos["Seco de pollo"]["ingredientes"].items():

                if stock[clave] < valor:

                    disponible = False
                    print("No hay suficiente stock de", clave)
                    break

            # DESCONTAR STOCK SOLO SI HAY INSUMOS
            if disponible:

                print("Tu pedido ha sido seleccionado correctamente.")

                for clave, valor in platos["Seco de pollo"]["ingredientes"].items():

                    stock[clave] -= valor

                print(stock)

            else:

                print("Ya no tenemos disponible ese plato")


        
        # TALLARÍN ROJO
        
        elif que_pedir == 2:

            disponible = True

            # VERIFICAR STOCK
            for clave, valor in platos["Tallarín rojo"]["ingredientes"].items():

                if stock[clave] < valor:

                    disponible = False
                    print("No hay suficiente stock de", clave)
                    break

            # DESCONTAR STOCK SOLO SI HAY INSUMOS
            if disponible:

                print("Tu pedido ha sido seleccionado correctamente.")

                for clave, valor in platos["Tallarín rojo"]["ingredientes"].items():

                    stock[clave] -= valor

                print(stock)

            else:

                print("Ya no tenemos disponible ese plato")


        
        # ESTOFADO DE POLLO
        
        elif que_pedir == 3:

            disponible = True

            # VERIFICAR STOCK
            for clave, valor in platos["Estofado de pollo"]["ingredientes"].items():

                if stock[clave] < valor:

                    disponible = False
                    print("No hay suficiente stock de", clave)
                    break

            
            if disponible:

                print("Tu pedido ha sido seleccionado correctamente.")

                for clave, valor in platos["Estofado de pollo"]["ingredientes"].items():

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
    for pedido in pedidos:
        nombre_plato = pedido["plato"]
        precio_plato = platos[nombre_plato]["precio"]
        print(f" • {nombre_plato:<20} : S/. {precio_plato:>6.2f}")
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
        for pedido in pedidos:
            historial_ventas.append(pedido["plato"])
            
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

    ESTADOS = ["Pendiente", "En preparación", "Listo"]

    while True:

        print("\n╔══════════════════════════════════╗")
        print("║         COLA DE COCINA          ║")
        print("╠══════════════════════════════════╣")
        print("║ 1. Ver cola de pedidos          ║")
        print("║ 2. Cambiar estado de un pedido  ║")
        print("║ 3. Atender siguiente            ║")
        print("║ 4. Tiempo estimado de espera    ║")
        print("║ 0. Volver al menú principal     ║")
        print("╚══════════════════════════════════╝")

        opcion = input("Seleccione una opción: ")


        # =====================================
        # VER COLA DE PEDIDOS
        # =====================================
        if opcion == "1":

            if len(pedidos) == 0:
                print("\n [!] No hay pedidos en la cola.")
            else:
                for i in range(len(pedidos)):
                    print(i + 1, "-", pedidos[i]["plato"], "-", pedidos[i]["estado"])


        # =====================================
        # CAMBIAR ESTADO DE UN PEDIDO
        # =====================================
        elif opcion == "2":

            if len(pedidos) == 0:
                print("\n [!] No hay pedidos en la cola.")
            else:
                for i in range(len(pedidos)):
                    print(i + 1, "-", pedidos[i]["plato"], "-", pedidos[i]["estado"])
                print("-" * 40)

                numero = int(input("Ingrese el N° del pedido a actualizar: "))

                if 1 <= numero <= len(pedidos):
                    pedido     = pedidos[numero - 1]
                    idx_actual = ESTADOS.index(pedido["estado"])
                    idx_nuevo  = (idx_actual + 1) % len(ESTADOS)
                    pedido["estado"] = ESTADOS[idx_nuevo]
                    print(f"\n [✓] '{pedido['plato']}' → {pedido['estado']}")
                else:
                    print("\n [!] Número inválido.")


        # =====================================
        # ATENDER SIGUIENTE PEDIDO
        # =====================================
        elif opcion == "3":

            encontrado = False

            # Buscar primero uno "Pendiente"
            for i in range(len(pedidos)):
                if pedidos[i]["estado"] == "Pendiente" and not encontrado:
                    pedidos[i]["estado"] = "En preparación"
                    print(f"\n [✓] '{pedidos[i]['plato']}' pasó a → En preparación")
                    encontrado = True

            # Si no hay pendientes, buscar uno "En preparación"
            if not encontrado:
                for i in range(len(pedidos)):
                    if pedidos[i]["estado"] == "En preparación" and not encontrado:
                        pedidos[i]["estado"] = "Listo"
                        print(f"\n [✓] '{pedidos[i]['plato']}' pasó a → Listo")
                        encontrado = True

            if not encontrado:
                print("\n [✓] Todos los pedidos ya están listos.")


        # =====================================
        # TIEMPO ESTIMADO DE ESPERA
        # =====================================
        elif opcion == "4":

            cantidad_pendientes = 0
            tiempo_total        = 0

            for i in range(len(pedidos)):
                if pedidos[i]["estado"] != "Listo":
                    cantidad_pendientes += 1
                    tiempo_total        += platos[pedidos[i]["plato"]]["tiempo_prep"]

            if cantidad_pendientes == 0:
                print("\n [✓] No hay pedidos pendientes. ¡La cocina está al día!")
            else:
                print(f"\n Pedidos en espera  : {cantidad_pendientes}")
                print(f" Tiempo estimado    : {tiempo_total} minutos")
                print("\n Detalle:")
                print("-" * 40)
                for i in range(len(pedidos)):
                    if pedidos[i]["estado"] != "Listo":
                        nombre = pedidos[i]["plato"]
                        t      = platos[nombre]["tiempo_prep"]
                        estado = pedidos[i]["estado"]
                        print(" -", nombre, "-", t, "min -", estado)
                print("-" * 40)


        # =====================================
        # VOLVER AL MENÚ PRINCIPAL
        # =====================================
        elif opcion == "0":
            break


        # =====================================
        # OPCIÓN INVÁLIDA
        # =====================================
        else:
            print(" [!] Opción inválida.")


# =====================================================
# AQUÍ VA LA PARTE DE PABLO - REPORTE DEL DÍA
# =====================================================

def reporte_dia():
    print("\n" + "═"*40)
    print("        REPORTE DEL DÍA              ")
    print("═"*40)

    # Validar que haya ventas registradas
    if len(historial_ventas) == 0:
        print(" [!] No hay ventas registradas hoy.")
        print("═"*40)
        return

    # ─────────────────────────────────────────
    # CONTEO DE PLATOS VENDIDOS
    # ─────────────────────────────────────────
    conteo = {}

    for plato in historial_ventas:
        if plato in conteo:
            conteo[plato] += 1
        else:
            conteo[plato] = 1

    # ─────────────────────────────────────────
    # DETALLE DE VENTAS
    # ─────────────────────────────────────────
    print(f" Total de platos vendidos: {len(historial_ventas)}")
    print("-" * 40)
    print(f" {'Plato':<22} {'Cant':>4}  {'Subtotal':>9}")
    print("-" * 40)

    total_bruto = 0.0

    for plato, cantidad in conteo.items():
        subtotal_plato = platos[plato]["precio"] * cantidad
        total_bruto += subtotal_plato
        print(f" {plato:<22} {cantidad:>4}  S/. {subtotal_plato:>6.2f}")

    print("-" * 40)

    # ─────────────────────────────────────────
    # TOTALES
    # ─────────────────────────────────────────
    igv_total = total_bruto * 0.18
    total_con_igv = total_bruto + igv_total

    print(f" Subtotal (sin IGV)  : S/. {total_bruto:>7.2f}")
    print(f" IGV recaudado (18%) : S/. {igv_total:>7.2f}")
    print("-" * 40)
    print(f" TOTAL DEL DÍA       : S/. {total_con_igv:>7.2f}")

    # ─────────────────────────────────────────
    # PLATO MÁS VENDIDO
    # ─────────────────────────────────────────
    plato_estrella = max(conteo, key=conteo.get)
    print("-" * 40)
    print(f" Plato más vendido : {plato_estrella}")
    print("═"*40)


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