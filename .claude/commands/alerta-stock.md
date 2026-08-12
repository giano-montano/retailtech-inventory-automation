---
description: Verifica productos críticos y genera alertas de stock (simuladas en .log)
argument-hint: [opcional] categoría o tienda a filtrar
---

Verifica productos en nivel crítico y genera alertas de stock.

## Pasos

1. Lee `data/inventario.csv`.
2. Detecta productos bajo mínimo (regla: `stock_actual < 0.2 × ventas_promedio_mensual`)
   y clasifica criticidad, p. ej.:
   - `stock_actual = 0` → rotura de stock
   - `stock_actual < mínimo` → crítico
   - cobertura < 50% del mínimo → alerta
3. Genera las alertas SIMULADAS en `output/alertas_stock_YYYY-MM-DD.log`
   (no envíes emails reales; usa archivo `.log`).
4. Prioriza por ABC (valor de inventario) y valor en riesgo.
5. Muestra un resumen: total de alertas, top productos, y proveedores a contactar
   (únete con `data/proveedores.csv`).

## Reglas

- Las alertas de email se simulan con archivos `.log`.
- No inventar información ausente en los datos; reportar lo que falta.
- No modificar archivos en `data/`; todo resultado va a `output/`.
