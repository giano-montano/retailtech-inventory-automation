---
description: Reporte rápido de inventario crítico (productos bajo stock mínimo)
argument-hint: [opcional] top N productos a mostrar
---

Genera un reporte rápido de inventario crítico.

## Pasos

1. Lee `data/inventario.csv` (y `data/proveedores.csv` si necesitas lead time).
2. Valida columnas y tipos antes de calcular. No asumas que un valor faltante es cero.
3. Identifica productos bajo stock mínimo usando la regla de negocio:

   ```
   stock_actual < 0.2 × ventas_promedio_mensual
   ```

   Compara también con la columna `stock_minimo` y reporta cualquier inconsistencia.
4. Prioriza por valor de inventario (clasificación ABC): A > 70% del valor, B 20–70%, C < 20%.
5. Escribe el reporte en `output/` con nombre descriptivo y fecha, p. ej.
   `output/reporte_inventario_critico_YYYY-MM-DD.md`.
6. Muestra un resumen ejecutivo: nº de productos críticos, categorías afectadas,
   valor en riesgo, y top prioridades con su justificación.

## Reglas

- No modificar archivos en `data/`.
- Distinguir datos observados de recomendaciones.
- Incluir métricas, priorización y recomendaciones accionables.
- Si falta algún dato requerido, indicarlo explícitamente.
