# RetailTech — Agente de Automatización de Inventario

Agente de IA construido con **Claude Code** para automatizar tareas de análisis y
gestión de inventario de **RetailTech S.A.** (25 tiendas, +50.000 SKU, 3 centros
de distribución: Lima, Arequipa y Trujillo).

Ayuda con:

- Análisis de datos de inventario.
- Identificación de productos con stock crítico o bajo mínimo.
- Generación de reportes de inventario.
- Sugerencia de cantidades de reposición.
- Generación de alertas de stock y proveedores.
- Análisis de patrones y tendencias.
- Consolidación de KPIs de inventario.

Las recomendaciones se basan en los datos disponibles y en las reglas de negocio
definidas en [`CLAUDE.md`](CLAUDE.md).

---

## Requisitos previos

| Requisito | Versión | Uso |
|---|---|---|
| [Claude Code](https://claude.com/claude-code) | reciente | Agente de automatización |
| Python | 3.6+ (solo stdlib) | Hook de contexto de inicio |
| Git Bash | — | Shell de los hooks (Windows) |

> En Windows, los hooks usan `bash`. Si Git Bash no está en el `PATH`, los hooks
> `SessionStart` y `Stop` pueden fallar silenciosamente.

---

## Estructura del proyecto

```
retailtech-automatizacion-inventario/
├── CLAUDE.md                        # Reglas de negocio y contexto del proyecto
├── README.md
├── data/                            # Datos fuente (NO modificar)
│   ├── inventario.csv               # Stock actual por tienda (2.400 filas)
│   ├── ventas.csv                   # Historial de ventas 12 meses (28.800 filas)
│   ├── proveedores.csv              # Proveedores y lead time
│   ├── ordenes.csv                  # Órdenes de compra emitidas
│   └── inventario_muestra.csv       # Muestra para ejercicios (esquema distinto)
├── output/                          # Resultados generados (reportes, logs)
└── .claude/
    ├── settings.json                # Hooks (SessionStart, Stop)
    ├── settings.local.json          # Credenciales locales (gitignored)
    ├── hooks/
    │   └── cargar_contexto.py       # Inyecta estado de datos + reglas al iniciar
    ├── commands/
    │   ├── inventario-critico.md    # Comando /inventario-critico
    │   └── alerta-stock.md          # Comando /alerta-stock
    └── skills/
        └── inventory-analyst.md     # Skill reutilizable de análisis
```

---

## Instalación / Configuración

1. **Clona o abre** el repositorio en tu máquina.

2. **Abre Claude Code** en la raíz del proyecto:

   ```bash
   cd retailtech-automatizacion-inventario
   claude
   ```

3. **(Opcional) Credenciales locales.** Si usas un proxy/endpoint propio, define
   tus variables en `.claude/settings.local.json` (nunca en `settings.json`):

   ```json
   {
     "env": {
       "ANTHROPIC_BASE_URL": "https://tu-endpoint/...",
       "ANTHROPIC_AUTH_TOKEN": "tu-token"
     }
   }
   ```

   Este archivo está **gitignored** (patrón `**/.claude/settings.local.json`), así
   que no se versiona.

4. **Recarga la configuración.** Tras clonar o editar `settings.json` por primera
   vez, abre `/hooks` una vez o reinicia Claude Code para que los hooks y comandos
   queden registrados.

---

## Configuración incluida

### Hooks (`.claude/settings.json`)

| Hook | Evento | Qué hace |
|---|---|---|
| Contexto de inicio | `SessionStart` | Ejecuta `cargar_contexto.py`, que inyecta en el modelo el **estado de los datos** (`data/*.csv`: columnas, nº de filas, fecha) y un **recordatorio de las reglas de negocio**. |
| Registro de cierre | `Stop` | Añade una línea con fecha/hora a `output/sesiones.log` al terminar cada respuesta. |

### Comandos personalizados (`.claude/commands/`)

| Comando | Descripción |
|---|---|
| `/inventario-critico [top N]` | Genera un reporte rápido de productos bajo stock mínimo. |
| `/alerta-stock [categoría]` | Verifica productos críticos y genera alertas simuladas en `output/alertas_stock_*.log`. |

### Skill (`.claude/skills/inventory-analyst.md`)

El skill `inventory-analyst` encapsula el flujo completo de análisis de inventario
(validar datos → aplicar reglas → priorizar → generar en `output/` → resumir).
Se activa automáticamente por descripción cuando pides cualquier análisis de
inventario, o puedes invocarlo explícitamente con `/inventory-analyst`.

---

## Uso

### Con comandos

```
/inventario-critico          → reporte rápido de bajo stock
/inventario-critico 10       → reporte limitado a los 10 productos más críticos
/alerta-stock                → alertas de stock simuladas (.log)
/alerta-stock Línea Blanca   → alertas filtradas por categoría
```

### Con lenguaje natural

Puedes pedir análisis directamente y el agente aplicará las reglas de negocio:

- "¿Qué productos están por debajo del stock mínimo?"
- "Sugiere órdenes de compra para los productos críticos."
- "Reconcilia el inventario entre tiendas y centros de distribución."
- "Genera un dashboard de KPIs de inventario."

### Flujo de trabajo

El agente sigue este flujo (definido en `CLAUDE.md`):

1. Identifica los archivos de datos relevantes.
2. Inspecciona estructura y valida columnas/tipos.
3. Valida calidad de datos antes de calcular.
4. Aplica las reglas de negocio.
5. Prioriza por impacto (ABC + valor en riesgo).
6. Genera resultados en `output/`.
7. Muestra un resumen de hallazgos.
8. Distingue datos observados de recomendaciones.

---

## Datos

| Archivo | Contenido | Columnas clave |
|---|---|---|
| `data/inventario.csv` | Stock por tienda | `producto_id`, `categoria`, `stock_actual`, `ventas_promedio_mensual`, `stock_minimo`, `precio_costo`, `precio_venta` |
| `data/ventas.csv` | Ventas 12 meses | `mes`, `tienda_id`, `producto_id`, `cantidad`, `total` |
| `data/proveedores.csv` | Proveedores | `proveedor_id`, `categoria`, `lead_time_dias` |
| `data/ordenes.csv` | Órdenes emitidas | `orden_id`, `proveedor_id`, `producto_id`, `cantidad`, `estado` |
| `data/inventario_muestra.csv` | Muestra de ejercicios | Esquema distinto al real |

---

## Reglas de negocio (resumen)

- **Stock mínimo** = 20% de la venta mensual promedio.
  `stock_actual < 0.2 × ventas_promedio_mensual` ⇒ producto bajo mínimo.
- **Lead time**: 7–21 días según categoría.
- **Clasificación ABC** por valor de inventario: A > 70%, B 20–70%, C < 20%.
- **Frecuencia de revisión**: A diario; B y C semanal.
- **Reconciliación**: discrepancia > 2% entre fuentes = significativa.

---

## Salidas (`output/`)

- Reportes en Markdown/CSV con nombre descriptivo y fecha (`YYYY-MM-DD`).
- Alertas de email **simuladas** con archivos `.log` (no se envían emails reales).
- Cada reporte incluye: resumen ejecutivo, productos/categorías afectadas,
  métricas, priorización, recomendaciones accionables y fecha de generación.

> Recomendado: añadir `output/` a un `.gitignore` local para no versionar
> resultados generados (o versionar solo los reportes que quieras conservar).

---

## Seguridad y notas

- **No modificar** los archivos fuente en `data/`; el agente solo escribe en `output/`.
- El token de `settings.local.json` está excluido del control de versiones por un
  gitignore global. No lo copies a `settings.json` ni a otros archivos versionados.
- Los hooks se cargan al iniciar sesión; tras cambiarlos, usa `/hooks` o reinicia.
