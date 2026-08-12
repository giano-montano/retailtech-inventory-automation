# Reporte de Productos Bajo Stock Mínimo

**Fecha de generación:** 2026-08-12
**Fuente de datos:** `data/inventario_muestra.csv` (200 SKUs)
**Criterio:** `stock_actual < stock_minimo`

---

## Resumen ejecutivo

Se identificaron **14 productos** (7% del catálogo) con stock por debajo de su nivel mínimo definido, de los cuales **5 están en estado crítico**. El déficit total es de **63 unidades** y el valor de inventario actual de estos productos asciende a **S/ 72,472.50**.

La categoría **Electrónica** concentra 8 de los 14 productos afectados y el mayor valor en riesgo, por lo que debe priorizarse su reposición.

---

## Productos afectados (ordenados por gravedad)

| ID | Producto | Categoría | Stock | Mínimo | % cubierto | Déficit | Valor actual (S/) | Estado |
|---|---|---|---|---|---|---|---|---|
| P017 | Desinfectante Multiuso 2L | Limpieza | 5 | 20 | 25% | 15 | 94.50 | Crítico |
| P005 | Monitor 27" 4K | Electrónica | 3 | 10 | 30% | 7 | 5,397.00 | Crítico |
| P034 | Proyector Portátil LED | Electrónica | 4 | 8 | 50% | 4 | 6,396.00 | Crítico |
| P025 | Smartwatch Deportivo | Electrónica | 7 | 12 | 58% | 5 | 4,193.00 | Bajo stock |
| P029 | Impresora Multifuncional | Electrónica | 6 | 10 | 60% | 4 | 5,394.00 | Bajo stock |
| P194 | Tóner Impresora Láser | Oficina | 6 | 10 | 60% | 4 | 1,494.00 | Crítico |
| P101 | Cámara Deportiva 4K | Electrónica | 5 | 8 | 62% | 3 | 6,495.00 | Crítico |
| P014 | Leche Deslactosada 1L | Bebidas | 22 | 30 | 73% | 8 | 151.80 | Bajo stock |
| P010 | Galletas Integrales Avena | Alimentos | 15 | 20 | 75% | 5 | 133.50 | Bajo stock |
| P002 | Tablet Pro 12 | Electrónica | 12 | 15 | 80% | 3 | 15,588.00 | Bajo stock |
| P003 | Laptop UltraSlim 15 | Electrónica | 8 | 10 | 80% | 2 | 19,992.00 | Bajo stock |
| P097 | Bufanda Lana Invierno | Accesorios | 9 | 10 | 90% | 1 | 719.10 | Bajo stock |
| P028 | Router WiFi 6 | Electrónica | 14 | 15 | 93% | 1 | 6,286.00 | Bajo stock |
| P066 | Bebida de Soja 1L | Bebidas | 14 | 15 | 93% | 1 | 138.60 | Bajo stock |

---

## Métricas relevantes

- **Total de productos bajo mínimo:** 14 (de 200)
- **Productos críticos:** 5
- **Déficit total:** 63 unidades
- **Valor de inventario en los 14 productos:** S/ 72,472.50
- **Categorías afectadas:** Electrónica (8), Bebidas (2), Limpieza (1), Oficina (1), Alimentos (1), Accesorios (1)
- **Almacén más afectado:** Almacén Central (10 de 14 productos)

---

## Priorización

1. **Prioridad alta — valor en riesgo:** P003 Laptop (S/ 19,992), P002 Tablet (S/ 15,588), P101 Cámara 4K (S/ 6,495), P034 Proyector (S/ 6,396), P028 Router (S/ 6,286). Roturas aquí representan pérdidas de venta de alto importe.
2. **Prioridad alta — criticidad de cobertura:** P017 (25%), P005 (30%), P034 (50%). Son los de menor porcentaje de cobertura sobre el mínimo.
3. **Prioridad media:** P025, P029, P194 (58–60%) y el resto de productos de consumo (Leche, Galletas, Soja).

---

## Recomendaciones

1. **Reabastecer de inmediato los 5 productos críticos**, priorizando Electrónica de alto valor (P005, P034, P101) por su impacto financiero.
2. **Revisar con los proveedores** DigitalWorld Corp (6 productos), SportTime Inc (2) y Lácteos del Valle (2), que concentran 10 de los 14 ítems afectados.
3. Para calcular cantidades de reposición y riesgo de rotura de stock (días de cobertura), se requiere el archivo **`data/ventas.csv`**, ausente en el repositorio actual.
4. Considerar el lead time por proveedor (regla de 7–21 días) antes de definir fechas de pedido.

---

## Notas de calidad de datos

- La columna `estado` presenta una inconsistencia de criterio: P029 y P194 tienen el mismo % de cobertura (60%) pero estados distintos ("Bajo stock" y "Crítico" respectivamente). Se recomienda unificar el umbral que distingue ambos estados.
- El stock mínimo aquí proviene de la columna `stock_minimo` del archivo, no del cálculo de regla de negocio (20% de la venta mensual), ya que no hay datos de ventas disponibles.
