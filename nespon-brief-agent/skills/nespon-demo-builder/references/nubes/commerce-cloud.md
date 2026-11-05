# Playbook — Commerce Cloud (B2B / D2C en plataforma)

## Org y licencias
Trial de B2B Commerce / D2C o SDO. Pre-flight: `PermissionSetLicense` con "Commerce" o "B2B". Una
Developer Edition normal no trae tienda.

## Escenas canónicas
| # | Escena | Qué enseña | Wow |
|---|---|---|---|
| 1 | **Tienda con catálogo y precios del cliente** | El comprador B2B ve sus precios y su catálogo | ⭐ cada cliente ve su propio precio |
| 2 | **Recompra rápida** | Repetir pedido o carga por lista/CSV | Lo que antes era un email con Excel |
| 3 | **Checkout** | Carrito, envío, pago de prueba | Pedido cerrado sin llamar al comercial |
| 4 | **Pedido en Salesforce** | El pedido aparece en el CRM y en servicio | Una sola verdad para ventas y servicio |

Demo básica: **1 → 2 → 4**.

## Por CLI
Datos: Product2 (20-30 productos con imágenes solo si están embebidas en la tienda), Pricebook y
entradas por cliente, cuentas compradoras con contactos. Los objetos de catálogo y buyer groups
varían por versión: `sf sobject describe` antes de escribir la spec.

## Manual
Crear la tienda desde la plantilla (Commerce app → Create store), asignar catálogo, buyer group,
entitlements y publicar. Usuario comprador: contacto + usuario externo con licencia de comunidad.

## Trampas
Tienda sin reindexar tras cargar productos → búsqueda vacía: reconstruir el índice de búsqueda y
esperar a que termine antes de la demo.
