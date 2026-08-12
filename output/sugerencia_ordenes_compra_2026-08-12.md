# Sugerencia de Órdenes de Compra — Reposición de Inventario

**Fecha de generación:** 2026-08-12
**Fuente de datos:** `data/inventario_muestra.csv`
**Alcance:** 14 productos con stock por debajo del mínimo (63 unidades de déficit)

---

## Resumen ejecutivo

Se sugieren **7 órdenes de compra** (una por proveedor) para reponer los 14 productos bajo stock mínimo. El valor total de reposición asciende a **S/ 40,290.00**. La orden de mayor monto corresponde a **DigitalWorld Corp** (S/ 29,028.00, 6 productos), concentrando el 72% del gasto de reposición.

> ⚠️ **Limitación de datos:** estas cantidades reponen el stock únicamente hasta el nivel mínimo definido en el archivo. No incluyen demanda durante el lead time, porque los archivos `data/ventas.csv` (venta promedio mensual) y `data/proveedores.csv` (lead time) **no están disponibles** en el repositorio. Ver sección "Supuestos y datos faltantes".

---

## Órdenes de compra sugeridas

### OC-01 · DigitalWorld Corp — S/ 29,028.00 (6 productos)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P005 Monitor 27" 4K | Central | 3 | 10 | 7 | 12,593.00 |
| P034 Proyector Portátil LED | Central | 4 | 8 | 4 | 6,396.00 |
| P003 Laptop UltraSlim 15 | Central | 8 | 10 | 2 | 4,998.00 |
| P029 Impresora Multifuncional | Central | 6 | 10 | 4 | 3,596.00 |
| P194 Tóner Impresora Láser | Central | 6 | 10 | 4 | 996.00 |
| P028 Router WiFi 6 | Central | 14 | 15 | 1 | 449.00 |

### OC-02 · SportTime Inc — S/ 6,892.00 (2 productos)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P101 Cámara Deportiva 4K | Central | 5 | 8 | 3 | 3,897.00 |
| P025 Smartwatch Deportivo | Central | 7 | 12 | 5 | 2,995.00 |

### OC-03 · TechSupply SA — S/ 3,897.00 (1 producto)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P002 Tablet Pro 12 | Central | 12 | 15 | 3 | 3,897.00 |

### OC-04 · CleanPro Perú — S/ 283.50 (1 producto)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P017 Desinfectante Multiuso 2L | Norte | 5 | 20 | 15 | 283.50 |

### OC-05 · ModaGlobal SAC — S/ 79.90 (1 producto)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P097 Bufanda Lana Invierno | Central | 9 | 10 | 1 | 79.90 |

### OC-06 · Lácteos del Valle — S/ 65.10 (2 productos)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P014 Leche Deslactosada 1L | Sur | 22 | 30 | 8 | 55.20 |
| P066 Bebida de Soja 1L | Sur | 14 | 15 | 1 | 9.90 |

### OC-07 · Distribuidora Andina — S/ 44.50 (1 producto)

| Producto | Almacén | Stock | Mínimo | Pedir | Subtotal (S/) |
|---|---|---|---|---|---|
| P010 Galletas Integrales Avena | Sur | 15 | 20 | 5 | 44.50 |

---

## Métricas del plan de reposición

| Métrica | Valor |
|---|---|
| Órdenes de compra | 7 |
| Productos a reponer | 14 |
| Unidades totales a pedir | 63 |
| Valor total de reposición | S/ 40,290.00 |
| Proveedor con mayor monto | DigitalWorld Corp (S/ 29,028.00) |
| Orden más urgente | OC-01 (DigitalWorld Corp) — 4 productos críticos |

---

## Priorización de ejecución

1. **OC-01 DigitalWorld Corp** — contiene 4 de los 5 productos críticos (P005, P034, P101 está en SportTime; P194) y el mayor valor en riesgo.
2. **OC-02 SportTime Inc** — 2 productos críticos/de alto valor (Cámara 4K, Smartwatch).
3. **OC-03 TechSupply SA** — Tablet Pro 12, alto valor.
4. **OC-04 a OC-07** — productos de consumo masivo, menor impacto financiero pero necesarios para evitar rotura en tienda.

---

## Supuestos y datos faltantes

Las cantidades sugeridas se calcularon con la regla mínima conservadora:

```
cantidad_sugerida = stock_minimo − stock_actual
```

Esto repone el stock **justo hasta el mínimo**, sin margen de seguridad. Para refinar el plan se necesita:

1. **`data/ventas.csv`** → venta promedio mensual, para validar el `stock_minimo` (regla: mínimo = 20% de la venta mensual) y calcular días de cobertura y riesgo de rotura.
2. **`data/proveedores.csv`** → lead time por proveedor (regla: 7–21 días), para dimensionar el stock de seguridad durante la reposición.

Con esos datos, la cantidad recomendada se ajustaría a:

```
cantidad_sugerida = stock_minimo + (venta_diaria_promedio × lead_time) − stock_actual
```

**No se ha modificado ningún archivo fuente** en `data/`. Los resultados se guardan en `output/`.
