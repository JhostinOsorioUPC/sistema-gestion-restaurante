# =====================================================
# VARIABLES GLOBALES
# =====================================================

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

pedidos = []


# =====================================================
# PARTE DE JEAN PAUL - TOMAR PEDIDO
# CORRECCIÓN 1: try/except para que no explote con letras
# CORRECCIÓN 2: se pide número de mesa al inicio, y se
#               guarda en cada pedido para que las demás
#               funciones puedan filtrar por mesa
# =====================================================

def tomar_pedido():

    # ── CORRECCIÓN JEAN PAUL (mesa) ───────────────
    # Antes: los pedidos no tenían mesa, todo se mezclaba
    # Ahora: se pide la mesa UNA vez al entrar a la función
    try:
        mesa = int(input("\nIngrese el número de mesa: "))
    except ValueError:
        print("Número de mesa inválido.")
        return
    # ─────────────────────────────────────────────

    while True:

        print("\nQue te gustaría pedir? ")

        try:
            que_pedir = int(input(
                "Seco de pollo (1), Tallarín rojo (2), "
                "Estofado de pollo (3) o Terminar pedido (0): "
            ))
        except ValueError:
            print("Por favor ingresa un número válido (0, 1, 2 o 3).")
            continue

        if que_pedir == 0:
            print("Saliendo de pedidos...")
            break

        elif que_pedir == 1:
            plato = "Seco de pollo"

        elif que_pedir == 2:
            plato = "Tallarín rojo"

        elif que_pedir == 3:
            plato = "Estofado de pollo"

        else:
            print("Opción inválida")
            continue

        disponible = True

        for clave, valor in platos[plato]["ingredientes"].items():
            if stock[clave] < valor:
                disponible = False
                print("No hay suficiente", clave)
                break

        if disponible:
            print("Pedido registrado correctamente.")
            for clave, valor in platos[plato]["ingredientes"].items():
                stock[clave] -= valor

            # ── CORRECCIÓN JEAN PAUL (mesa) ───────────
            # Antes: {"plato": plato, "estado": "Pendiente"}
            # Ahora: se agrega "mesa" para que cocina y
            #        facturación puedan identificar de quién es
            pedidos.append({
                "mesa"  : mesa,
                "plato" : plato,
                "estado": "Pendiente"
            })
            # ─────────────────────────────────────────
        else:
            print("No se pudo procesar el pedido (sin stock)")


# =====================================================
# PARTE DE ENRIQUE - CONTROL DE STOCK
# (sin cambios de mesa, el stock es global)
# CORRECCIÓN anterior mantenida: variables renombradas
# =====================================================

def control_stock():

    while True:

        print("\n╔══════════════════════════════════╗")
        print("║        CONTROL DE STOCK         ║")
        print("╠══════════════════════════════════╣")
        print("║ 1. Ver stock                    ║")
        print("║ 2. Registrar compra             ║")
        print("║ 0. Volver al menú principal     ║")
        print("╚══════════════════════════════════╝")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            print("\n======= STOCK DISPONIBLE =======")
            for producto, cantidad in stock.items():
                print(producto, ":", cantidad)
                if cantidad <= 1:
                    print("ALERTA: Stock crítico de", producto)
            print("================================")

        elif opcion == "2":

            producto_comprado = input("Ingrese el nombre del insumo: ")
            cantidad_comprada = int(input("Ingrese la cantidad comprada: "))

            if producto_comprado in stock:
                stock[producto_comprado] += cantidad_comprada
            else:
                stock[producto_comprado] = cantidad_comprada

            print("Compra registrada correctamente.")
            print("\n======= STOCK ACTUALIZADO =======")
            for item_nombre, item_cantidad in stock.items():
                print(item_nombre, ":", item_cantidad)
            print("=================================")

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


# =====================================================
# PARTE DE LIMBERG - FACTURAR MESA
# CORRECCIÓN: se pregunta qué mesa facturar y solo se
# muestran/cobran los pedidos "Listos" de esa mesa
# =====================================================

# =====================================================
# PARTE DE LIMBERG - FACTURAR MESA
# =====================================================

def facturar_mesa():

    try:
        mesa = int(input("\nIngrese el número de mesa a facturar: "))
    except ValueError:
        print("Número de mesa inválido.")
        return

    # Buscar TODOS los pedidos de la mesa
    pedidos_mesa = []

    for pedido in pedidos:
        if pedido["mesa"] == mesa:
            pedidos_mesa.append(pedido)

    # Verificar si existen pedidos
    if len(pedidos_mesa) == 0:
        print(f"\nNo hay pedidos registrados para la mesa {mesa}")
        return

    print("\n" + "=" * 40)
    print(f"         FACTURA - MESA {mesa}")
    print("=" * 40)

    subtotal = 0

    # Mostrar pedidos
    for i, pedido in enumerate(pedidos_mesa, start=1):

        nombre_plato = pedido["plato"]
        estado = pedido["estado"]
        precio = platos[nombre_plato]["precio"]

        print(f"{i}. {nombre_plato} - {estado} -> S/. {precio:.2f}")

        subtotal += precio

    # Cálculos
    igv = subtotal * 0.18
    total = subtotal + igv

    print("-" * 40)
    print(f"Subtotal : S/. {subtotal:.2f}")
    print(f"IGV (18%) : S/. {igv:.2f}")
    print(f"TOTAL : S/. {total:.2f}")
    print("=" * 40)

    confirmar = input("¿Desea pagar? (S/N): ")

    if confirmar.upper() == "S":

        # Guardar ventas
        for pedido in pedidos_mesa:
            historial_ventas.append(pedido["plato"])

        # Eliminar pedidos pagados
        for pedido in pedidos_mesa:
            pedidos.remove(pedido)

        print(f"\nPago realizado correctamente para la mesa {mesa}")

    else:
        print("\nPago cancelado.")


# =====================================================
# PARTE DE JHOSTIN - COLA DE COCINA
# CORRECCIÓN 1: pedido "Listo" ya no retrocede a "Pendiente"
# CORRECCIÓN 2: muestra el número de mesa en cada pedido
#               para que cocina sepa a quién entregar
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

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            if len(pedidos) == 0:
                print("\n [!] No hay pedidos en la cola.")
            else:
                for i in range(len(pedidos)):
                    # ── CORRECCIÓN JHOSTIN (mesa) ─────────
                    # Antes: solo mostraba plato y estado
                    # Ahora: también muestra la mesa para saber
                    #        a quién llevar el plato cuando esté listo
                    print(i + 1, "- Mesa", pedidos[i]["mesa"],
                          "-", pedidos[i]["plato"],
                          "-", pedidos[i]["estado"])
                    # ─────────────────────────────────────

        elif opcion == "2":

            if len(pedidos) == 0:
                print("\n [!] No hay pedidos en la cola.")
            else:
                for i in range(len(pedidos)):
                    print(i + 1, "- Mesa", pedidos[i]["mesa"],
                          "-", pedidos[i]["plato"],
                          "-", pedidos[i]["estado"])
                print("-" * 40)

                try:
                    numero = int(input("Ingrese el N° del pedido a actualizar: "))
                except ValueError:
                    print("\n [!] Ingresa un número válido.")
                    continue

                if 1 <= numero <= len(pedidos):
                    pedido     = pedidos[numero - 1]
                    idx_actual = ESTADOS.index(pedido["estado"])

                    if idx_actual == len(ESTADOS) - 1:
                        print(f"\n [!] '{pedido['plato']}' ya está Listo, no puede avanzar más.")
                    else:
                        idx_nuevo        = idx_actual + 1
                        pedido["estado"] = ESTADOS[idx_nuevo]
                        print(f"\n [✓] Mesa {pedido['mesa']} - '{pedido['plato']}' → {pedido['estado']}")
                else:
                    print("\n [!] Número inválido.")

        elif opcion == "3":

            encontrado = False

            for i in range(len(pedidos)):
                if pedidos[i]["estado"] == "Pendiente" and not encontrado:
                    pedidos[i]["estado"] = "En preparación"
                    print(f"\n [✓] Mesa {pedidos[i]['mesa']} - '{pedidos[i]['plato']}' → En preparación")
                    encontrado = True

            if not encontrado:
                for i in range(len(pedidos)):
                    if pedidos[i]["estado"] == "En preparación" and not encontrado:
                        pedidos[i]["estado"] = "Listo"
                        print(f"\n [✓] Mesa {pedidos[i]['mesa']} - '{pedidos[i]['plato']}' → Listo")
                        encontrado = True

            if not encontrado:
                print("\n [✓] Todos los pedidos ya están listos.")

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
                        mesa   = pedidos[i]["mesa"]
                        print(f" - Mesa {mesa} - {nombre} - {t} min - {estado}")
                print("-" * 40)

        elif opcion == "0":
            break

        else:
            print(" [!] Opción inválida.")


# =====================================================
# PARTE DE PABLO - REPORTE DEL DÍA
# (sin cambios de mesa, el reporte es global del día)
# CORRECCIÓN anterior mantenida: verifica que el plato
# exista en el diccionario antes de buscar su precio
# =====================================================

def reporte_dia():
    print("\n" + "═"*40)
    print("        REPORTE DEL DÍA              ")
    print("═"*40)

    if len(historial_ventas) == 0:
        print(" [!] No hay ventas registradas hoy.")
        print("═"*40)
        return

    conteo = {}
    for plato in historial_ventas:
        if plato in conteo:
            conteo[plato] += 1
        else:
            conteo[plato] = 1

    print(f" Total de platos vendidos: {len(historial_ventas)}")
    print("-" * 40)
    print(f" {'Plato':<22} {'Cant':>4}  {'Subtotal':>9}")
    print("-" * 40)

    total_bruto = 0.0

    for plato, cantidad in conteo.items():

        if plato in platos:
            precio_unitario = platos[plato]["precio"]
        else:
            precio_unitario = 0.0
            print(f" [!] Advertencia: '{plato}' ya no está en el menú (precio=0)")

        subtotal_plato  = precio_unitario * cantidad
        total_bruto    += subtotal_plato
        print(f" {plato:<22} {cantidad:>4}  S/. {subtotal_plato:>6.2f}")

    print("-" * 40)

    igv_total     = total_bruto * 0.18
    total_con_igv = total_bruto + igv_total

    print(f" Subtotal (sin IGV)  : S/. {total_bruto:>7.2f}")
    print(f" IGV recaudado (18%) : S/. {igv_total:>7.2f}")
    print("-" * 40)
    print(f" TOTAL DEL DÍA       : S/. {total_con_igv:>7.2f}")

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

    opcion = input("Seleccione una opción: ").strip()

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