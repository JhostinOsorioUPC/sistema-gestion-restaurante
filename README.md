# 🍽️ Sistema - Sabor y Tradición

Sistema de gestión para restaurante desarrollado en Python. Permite tomar pedidos, controlar stock, facturar mesas y gestionar la cola de cocina.

## Funcionalidades

- **Tomar pedido** – Registra el plato elegido por el cliente y descuenta los ingredientes del stock automáticamente.
- **Control de stock** – Consulta el inventario disponible y registra nuevas compras de insumos.
- **Facturar mesa** – Calcula el subtotal, IGV (18%) y total a pagar, luego libera la mesa.
- **Cola de cocina** – Gestiona el estado de cada pedido (Pendiente → En preparación → Listo) y muestra el tiempo estimado de espera.
- **Reporte del día** – Muestra el resumen de ventas, ingresos totales y el plato más vendido.

## Platos disponibles

| Plato | Precio | Tiempo de prep. |
|---|---|---|
| Seco de pollo | S/. 15.50 | 12 min |
| Tallarín rojo | S/. 14.00 | 10 min |
| Estofado de pollo | S/. 16.00 | 15 min |

## Requisitos

- Python 3.x
- No requiere librerías externas

## Cómo ejecutar

```bash
python application.py
```

## Integrantes

| Módulo | Responsable |
|---|---|
| Tomar pedido | Jean Paul |
| Control de stock | Enrique |
| Facturar mesa | Limberg |
| Cola de cocina | Jhostin |
| Reporte del día | Pablo |
