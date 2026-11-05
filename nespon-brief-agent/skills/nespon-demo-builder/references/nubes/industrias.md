# Playbook — Industries (Manufacturing, Public Sector, Consumer Goods, Automotive, Energy,
# Communications, Media, Nonprofit, Education)

Todas necesitan una **org de su industria** (trial específica o SDO de industria): el modelo de
datos no existe en una org genérica. Pre-flight: `PermissionSetLicense` con el nombre de la
industria y `sf sobject list` para descubrir los objetos reales antes de escribir la spec.
Estructura común: 3-4 escenas, la primera siempre es la "vista 360" propia del sector.

| Industria | Escenas básicas | Wow típico |
|---|---|---|
| **Manufacturing** | Sales Agreements (volumen pactado vs real) · Account Forecasting · Rebates · Gestión de distribuidores | ⭐ desviación entre lo pactado y lo pedido, a tiempo de actuar |
| **Public Sector** | Portal ciudadano de trámites · Expediente con fases y plazos · Inspecciones · Licencias y permisos | ⭐ el ciudadano ve en qué fase está su expediente |
| **Consumer Goods** | Visitas a punto de venta · Auditoría de lineal con el móvil · Pedido en tienda · Promociones | ⭐ el comercial llega sabiendo qué falta en el lineal |
| **Automotive** | Vehículo y su historial · Lead del concesionario · Cita de taller · Campañas de revisión | ⭐ el taller ve el vehículo completo antes de recibirlo |
| **Energy & Utilities** | Punto de suministro y contratos · Reclamación de factura · Alta/cambio de titular en portal | ⭐ el cambio de titular sin papel |
| **Communications** | Configurar oferta con tarifas · Contrato y renovación · Incidencia con contexto de línea | ⭐ la renovación se propone antes de que el cliente se vaya |
| **Media** | Plan de medios y órdenes de inserción · Cuentas de anunciantes | Del brief a la orden sin Excel |
| **Nonprofit** | Donante 360 · Campañas de captación · Programas y beneficiarios | ⭐ cuánto y a quién ha llegado cada donación |
| **Education** | Captación de alumnos · Expediente del estudiante · Portal del alumno | ⭐ del interesado a la matrícula sin perderlo |

Por CLI: datos del modelo de la industria (descubiertos con `describe`), permission sets del
paquete. Manual: plantillas y asistentes de la industria. Si la industria es la nube ancla y no
hay org de industria, propone hacer la demo con la nube horizontal equivalente (Sales/Service/
Experience) y dilo como alternativa, no como la industria.
