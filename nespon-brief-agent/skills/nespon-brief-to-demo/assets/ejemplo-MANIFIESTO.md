# MANIFIESTO DE DESARROLLO — Bodegas Altiplano — v1

**Estado de revisión:** BORRADOR
**Revisado por:** — · **Fecha de aprobación:** —
**Cliente:** Bodegas Altiplano SA · **Sector:** Vino (bodega) · **Zona fiscal:** Península (IVA 21%)
**Nube ancla:** Sales Cloud · **Nubes de apoyo:** Einstein (prompt templates) · **Org objetivo:** Developer Edition con Einstein generativo, o SDO
**Protagonista:** Andrés Molina, Director Comercial
**Audiencia negocio:** Director Comercial, Gerente · **Audiencia técnica:** Responsable de IT
**Restricciones del SE:** Solo Sales Cloud; IA "sin volverse locos" (nada de agentes complejos)
**Reparto:** IA 14 (70%) · IA+Revisión 3 · Persona 3 · **Niveles:** 🟢 9 · 🔵 11 · 🟠 0

## 1. Necesidades del cliente
| ID | Necesidad | Origen |
|----|-----------|--------|
| NEC-1 | El director comercial no sabe qué distribuidor vende más hasta que cierra el mes | Brief |
| NEC-2 | Los 9 comerciales llevan todo en Excel; no hay visión del pipeline ni de lo que se atasca | Brief |
| NEC-3 | Los descuentos se dan "a ojo" y dirección se entera tarde | Brief |
| NEC-4 | Preparar una visita exige buscar información en varios sitios | Supuesto |
| NEC-5 | Ver "lo de la IA" de forma práctica, sin complejidad | Brief |

## 2. Historia y escenas
**Historia en una frase:** Andrés pasa de enterarse a fin de mes a ver cada mañana qué distribuidor tira, qué operación se atasca y qué descuento necesita su visto bueno, desde el móvil.

| ID | Escena | Necesidades | Qué ve el cliente | Wow | Plan B |
|----|--------|-------------|-------------------|-----|--------|
| ESC-1 | Su CRM, con su marca | NEC-2, NEC-4 | App "Altiplano Ventas" con sus colores; ficha 360 de un distribuidor con contactos, oportunidades, actividad y gráfico de ventas | — | — |
| ESC-2 | El mes sin sorpresas | NEC-1, NEC-2 | Dashboard de Dirección: ranking de distribuidores, pipeline por etapa y 3 operaciones en rojo | ⭐ el ranking de distribuidores y el riesgo, de un vistazo | List view "Operaciones en riesgo" |
| ESC-3 | La alerta que llega sola | NEC-2 | Una operación pasa a riesgo: aparece la notificación en la campana y la tarea al comercial | — | Tarea ya creada en el ensayo |
| ESC-4 | El descuento bajo control | NEC-3 | El comercial pide un 18%; Andrés lo aprueba desde el móvil | ⭐ aprobación en el móvil en directo | Enseñar la aprobación en escritorio |
| ESC-5 | La visita preparada en un clic | NEC-4, NEC-5 | En la ficha del distribuidor, un botón genera el resumen para la visita | ⭐ resumen escrito por la IA con datos reales | Resumen generado en el ensayo |

## 3. Componentes
| ID | Escena | Componente | Tipo | Especificación | Nivel | Responsable | Motivo | Tamaño | Estado |
|----|--------|------------|------|----------------|-------|-------------|--------|--------|--------|
| CMP-1 | ESC-1 | Tema con colores de la bodega | BrandingSet | LightningExperienceTheme "Altiplano": color de marca granate #7B1E3A, cabecera clara | 🟢 | IA+Revisión | Colores a validar por el SE | S | Pendiente |
| CMP-2 | ESC-1 | Logo de la bodega | Setup | Subir el logo y asignarlo al tema CMP-1 | 🟢 | Persona | El logo real lo aporta el SE | S | Pendiente |
| CMP-3 | ESC-1 | App Altiplano Ventas | CustomApplication | Tabs: Home, Accounts, Contacts, Opportunities, Reports, Dashboards; utility bar con Notes | 🟢 | IA | — | S | Pendiente |
| CMP-4 | ESC-1 | Ficha 360 del distribuidor | FlexiPage | Account record page: Highlights, pestañas Detalle/Actividad/Relacionados, report chart de CMP-9 filtrado por la cuenta, related lists Contacts y Opportunities | 🟢 | IA | — | M | Pendiente |
| CMP-5 | ESC-1 | Canal del cliente | CustomField | Account.Canal__c Picklist[Distribuidor;HORECA;Gran superficie;Exportación] | 🔵 | IA | — | S | Pendiente |
| CMP-6 | ESC-2 | Fecha de entrada en etapa | CustomField | Opportunity.Stage_Entered_Date__c Date | 🔵 | IA | — | S | Pendiente |
| CMP-7 | ESC-2 | Nivel de riesgo | CustomField | Opportunity.Nivel_Riesgo__c Formula(Text): IF(AND(NOT(IsClosed), TODAY()-Stage_Entered_Date__c>30),"En riesgo","En plazo") | 🔵 | IA | — | S | Pendiente |
| CMP-8 | ESC-2 | Sellar fecha de etapa | Flow | Record-Triggered, Opportunity, before save, ISCHANGED(StageName) → Stage_Entered_Date__c = TODAY(). Desplegar inactivo; activar tras la carga | 🔵 | IA | — | S | Pendiente |
| CMP-9 | ESC-1, ESC-2 | Ventas por distribuidor | Report | Opportunities, StageName = Closed Won, agrupado por Account.Name, suma Amount, gráfico de barras horizontal | 🟢 | IA | — | S | Pendiente |
| CMP-10 | ESC-2 | Pipeline y riesgo | Report | Opportunities abiertas agrupadas por StageName; columnas Name, Account, Amount, CloseDate, Nivel_Riesgo__c | 🟢 | IA | — | S | Pendiente |
| CMP-11 | ESC-2 | Dashboard Dirección Comercial | Dashboard | Top 10 distribuidores (CMP-9), pipeline por etapa (CMP-10), tabla "En riesgo" con formato condicional rojo, métrica de ganado del trimestre | 🟢 | IA+Revisión | Composición y estética a validar | M | Pendiente |
| CMP-12 | ESC-2 | Path de oportunidad | PathAssistant | Opportunity, todas las etapas, guía de venta en español por etapa | 🟢 | IA | — | S | Pendiente |
| CMP-13 | ESC-3 | Notificación de riesgo | CustomNotificationType | "Operación en riesgo", escritorio y móvil | 🔵 | IA | — | S | Pendiente |
| CMP-14 | ESC-3 | Aviso automático de riesgo | Flow | Record-Triggered, Opportunity, after save, Nivel_Riesgo__c = "En riesgo" y sin tarea abierta → Task "Revisar operación en riesgo" al owner (mañana) + custom notification CMP-13 al owner y a su manager. Activar tras la carga | 🔵 | IA | — | M | Pendiente |
| CMP-15 | ESC-4 | Descuento | CustomField | Opportunity.Descuento__c Percent(3,0) | 🔵 | IA | — | S | Pendiente |
| CMP-16 | ESC-4 | Aprobación de descuento | ApprovalProcess | Opportunity, entrada Descuento__c > 15; aprobador = manager del owner; al aprobar marcar estado y notificar | 🔵 | IA | — | M | Pendiente |
| CMP-17 | ESC-4 | Usuario del Director Comercial | Setup | La IA crea el usuario Andrés Molina (Standard User, email del SE) como manager de los comerciales; el SE lo activa desde el email e inicia sesión en la app móvil | 🟢 | Persona | Activación por email y login en el móvil | S | Pendiente |
| CMP-18 | ESC-5 | Activar IA generativa | Setup | Einstein Setup → activar; Prompt Builder disponible | 🔵 | Persona | Aceptación de términos en la interfaz | S | Pendiente |
| CMP-19 | ESC-5 | Resumen para la visita | GenAiPromptTemplate | Field/Flex template sobre Account: resumen de últimas oportunidades, actividad y ventas del año, tono cercano, en español; botón en CMP-4 | 🔵 | IA+Revisión | Respuesta no determinista: ensayar | M | Pendiente |
| CMP-20 | ESC-1, ESC-4 | Permisos de la demo | PermissionSet | Demo_Altiplano: CRUD Account/Opportunity/Task, FLS de CMP-5, CMP-6, CMP-7, CMP-15, app CMP-3, uso del prompt CMP-19 | 🔵 | IA | — | S | Pendiente |

## 4. Tareas de persona
### CMP-2 — Logo de la bodega
- **Ruta:** Setup → Themes and Branding → tema "Altiplano" → Edit → Brand Image (el nombre del menú puede variar).
- **Valores:** logo en PNG con fondo transparente, ancho mínimo 300 px.
- **Comprobar:** el logo aparece arriba a la izquierda al recargar.
- **Desbloquea:** —

### CMP-17 — Usuario del Director Comercial
- **Ruta:** abrir el email de activación que llega al buzón del SE → fijar contraseña; instalar la app Salesforce en el móvil e iniciar sesión con ese usuario.
- **Valores:** usuario `andres.molina@demo-altiplano.example`.
- **Comprobar:** la app móvil abre la home de Altiplano Ventas.
- **Desbloquea:** CMP-16

### CMP-18 — Activar IA generativa
- **Ruta:** Setup → Einstein Setup → activar Einstein; aceptar los términos (el nombre del menú puede variar).
- **Valores:** —
- **Comprobar:** Setup → Prompt Builder abre sin error.
- **Desbloquea:** CMP-19

## 5. Datos de demo
Spec: `datos/seed-spec.json` (generada con `fill_data.py` desde `datos/fill-config.json` y `datos/heroes.json`) · Historia de los datos: `datos/HISTORIA-DATOS.md`

| ID | Objeto | Registros | Contenido / valores clave | Escenas |
|----|--------|-----------|---------------------------|---------|
| DAT-1 | Account | 2 protagonistas + 24 relleno | ACC-ESTRELLA "Distribuciones Vinícolas del Sureste SL" (Canal Distribuidor, Murcia, todos los campos visibles rellenos); ACC-HORECA "Grupo Hostelero Mar Menor SL" | ESC-1, ESC-2, ESC-5 |
| DAT-2 | Opportunity | 5 protagonistas + ~40 relleno | OPP-RIESGO-1..3 con Stage_Entered_Date__c TODAY-35, TODAY-42, TODAY-50; OPP-DESCUENTO con Descuento__c 18; ganadas de ACC-ESTRELLA para liderar el ranking | ESC-2, ESC-3, ESC-4 |
| DAT-3 | Contact, Task | 3 protagonistas + relleno | Contactos de ACC-ESTRELLA con cargo y móvil; tareas completadas TODAY-3..TODAY-40 para que el resumen de IA tenga contexto | ESC-1, ESC-5 |

## 6. Orden de construcción
CMP-18 → CMP-5 → CMP-6 → CMP-7 → CMP-15 → CMP-13 → CMP-8 (inactivo) → CMP-14 (inactivo) → CMP-20 → CMP-3 → CMP-1 → CMP-2 → CMP-4 → CMP-12 → CMP-9 → CMP-10 → CMP-11 → CMP-17 → CMP-16 → CMP-19 → DAT-1 → DAT-2 → DAT-3 → activar CMP-8 y CMP-14

## 7. Supuestos y preguntas abiertas
- Supuesto: NEC-4 (preparación de visitas) no está en el brief; se deduce del sector.
- Supuesto: la org tiene Einstein generativo; si no, ESC-5 sale de la demo y se cuenta como siguiente paso.
- Pregunta para el SE: ¿tienes el logo de la bodega o usamos solo los colores?

## 8. Registro de cambios
- v1: versión inicial a partir del brief de Marta.
