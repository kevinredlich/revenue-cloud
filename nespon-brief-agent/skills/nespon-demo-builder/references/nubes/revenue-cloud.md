# Playbook — Revenue Cloud (RLM)

## Carga obligatoria
Carga también la skill `revenue-cloud-demo`: define objetos RLM, catálogo (PCM), selling models,
pricing y patrones de demo. Este playbook solo fija la demo rápida.

## Org y licencias
Org con Revenue Cloud provisionado (SDO o trial). Pre-flight: `PermissionSetLicense` con
"Revenue", "Product Catalog" o "Pricing". Si solo hay Sales Cloud y el catálogo es simple, la demo
rápida puede hacerse con Quotes estándar (dilo como alternativa, no como RLM).

## Escenas canónicas
| # | Escena | Qué enseña | Wow |
|---|---|---|---|
| 1 | **Catálogo** | Productos, bundles y atributos en un catálogo gobernado | Un solo sitio para todo lo que se vende |
| 2 | **Configurar y presupuestar** | Desde la oportunidad: bundle configurado, reglas que impiden errores | ⭐ imposible vender una combinación inválida |
| 3 | **Precio correcto** | Descuento por volumen / precio por cliente aplicado solo; aprobación si se excede | ⭐ el precio sale bien a la primera |
| 4 | **Quote → Order** | El presupuesto aceptado se convierte en pedido | Sin reescribir nada |
| 5 | **Renovación / amendment** | Suscripción que se amplía o renueva | Ingresos recurrentes bajo control |

Demo básica: **1 → 2 → 3 → 4**.

## Por CLI y manual
Sigue `revenue-cloud-demo` para qué objetos se cargan como datos y qué se configura en la interfaz.
Precios en EUR con el impuesto de la zona fiscal.
