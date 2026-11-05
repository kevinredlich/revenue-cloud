# Playbook — Marketing Cloud

## Índice
1. Elegir variante (pregunta obligatoria si no está clara)
2. Marketing Cloud Next (Growth/Advanced) — variante por defecto
3. Account Engagement (antes Pardot)
4. Marketing Cloud Engagement (clásico)
5. Datos de ejemplo comunes

> Marketing Cloud es la nube con **más pasos manuales**: gran parte de su configuración vive en
> asistentes de Setup y editores visuales, no en metadata desplegable. Automatiza los datos y lo
> que viva en la org core; guía al SE en lo demás. Los nombres de menús cambian por release: si un
> menú no aparece con ese nombre, búscalo en Quick Find por palabra clave y díselo al usuario.

---

## 1. Elegir variante

| Variante | Qué es | Entorno de demo | ¿Automatizable con sf CLI? |
|---|---|---|---|
| **Marketing Cloud Next** (Growth / Advanced) | Marketing nativo en la plataforma core sobre Data Cloud, con agentes | SDO de Partner Learning Camp (Demo Org → SDO) o Developer Edition de MC Next en Trailhead Playground | Parcial: datos CRM, campañas, permisos. Activos de marketing, manual |
| **Account Engagement** | Automatización B2B conectada a Sales Cloud (formularios, scoring, Engagement Studio) | Org de desarrollo de Account Engagement o SDO | Parcial: lado Sales Cloud. Activos de AE, manual |
| **Marketing Cloud Engagement** | Plataforma clásica en tenant aparte (Email Studio, Journey Builder) | Cuenta no productiva de partner | No: guía + ficheros para importar |

Si el usuario solo dice "Marketing Cloud", **pregunta cuál**. Si no lo sabe, recomienda **Marketing
Cloud Next**: es la línea principal de Salesforce, se monta en una org core y es la más rápida de
dejar lista. Para B2B con ciclo largo y equipo comercial en Sales Cloud, Account Engagement sigue
siendo una opción creíble.

---

## 2. Marketing Cloud Next (variante por defecto)

### Org y licencias
- Org: SDO de Partner Learning Camp (Nespon es partner) o Developer Edition de MC Next en
  Trailhead Playground. Una Developer Edition normal **no** trae Marketing Cloud Next.
- Comprobar en pre-flight (coincidencia parcial en `PermissionSetLicense`): Marketing Cloud /
  Marketing, Data Cloud, Einstein / Agentforce (para escenas con IA).

### Escenas canónicas (elige 3-5)

| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Segmento en lenguaje natural** | Einstein crea un segmento sobre datos unificados a partir de una frase ("clientes de Murcia y Alicante del sector alimentación") | ⭐ el segmento aparece con su recuento sin escribir una regla | Segmento ya creado y publicado |
| 2 | **Email generado y personalizado** | Crear email con contenido generado por IA, marca y campos de personalización; preview como un contacto concreto | ⭐ el email se escribe solo y se ve con el nombre del contacto | Email ya creado; enseñar preview |
| 3 | **Formulario y landing page** | Un formulario publicado; al rellenarlo, el contacto nuevo aparece en CRM con su consentimiento | El registro aparece en CRM al momento | Contacto de ejemplo ya capturado |
| 4 | **Flow de marketing (journey)** | Flow disparado por segmento o formulario: email → espera → decisión por apertura/clic → segundo email o tarea al comercial | La tarea del comercial nace de la interacción | Captura del flow y la tarea ya creada |
| 5 | **Campaña con agente** (si Agentforce está activo) | El agente de marketing genera brief, audiencia, email y flow de una campaña a partir de un objetivo | ⭐ la campaña completa en borrador desde una frase | Campaña generada en el ensayo |
| 6 | **Analítica** | Dashboard de rendimiento de campaña y engagement | KPIs de la campaña en un vistazo | Captura del dashboard |

Demo básica recomendada: **1 → 2 → 4 → 6**, más **5** si hay Agentforce.

### Qué hace el agente por CLI
- Pre-flight completo, idioma/zona del usuario.
- Datos CRM de ejemplo (sección 5): Accounts, Contacts (y Leads si aplica), Campaign.
- Asignar permission sets de Marketing Cloud al usuario de demo si existen y no están asignados
  (busca en `PermissionSet` por label que contenga "Marketing").
- Verificación de datos en CRM.

### Pasos manuales (guíalos en orden)
1. **Data Cloud Setup → Get Started** si no está aprovisionado. Puede tardar hasta una hora: si hay
   que hacerlo, **es lo primero** y el resto se prepara mientras tanto.
2. **Marketing Cloud → Assisted Setup**: Basic Settings y canal Email.
3. **Instalar los Data Kits de Marketing Cloud** en Data Cloud Setup (streams y mapeos). Esperar a
   estado *Deployed*.
4. Activar funciones de Einstein de marketing (creación de segmentos, send time optimization,
   contenido generativo) si están disponibles.
5. **Envío de email:** en SDO recientes la dirección remitente por defecto suele estar habilitada;
   si no, enviar exige dominio autenticado con registros DNS. **Para una demo rápida no configures
   dominio**: usa preview y envío de prueba a la dirección del SE.
6. Crear en la interfaz los activos de las escenas (segmento, email, formulario, flow) siguiendo
   la guía; el agente redacta los textos exactos (asunto, cuerpo, frase del segmento) en español
   para copiar y pegar.

### Verificación
- `SELECT COUNT() FROM Contact WHERE Email LIKE '%@example.com'` ≥ datos cargados.
- Manual: los contactos aparecen en Data Cloud (Data Explorer / perfil unificado) tras la ingesta.
- Manual: preview del email con un contacto concreto muestra su nombre.

### Trampas
- Empezar la demo sin que la ingesta a Data Cloud haya terminado → segmento vacío.
- Usar Marketing Setup (el menú naranja) en lugar de Setup de Marketing Cloud: es el de Account
  Engagement.
- Contactos de prueba sin suscripción o consentimiento al canal email → no se puede hacer envío de
  prueba. Asegura que al menos el contacto del SE lo tiene.
- Enviar a direcciones reales. Todo `@example.com` excepto el SE.

---

## 3. Account Engagement

### Org
Org de desarrollo de Account Engagement o SDO. Comprobar la licencia y que la business unit está
conectada a la org (Account Engagement Setup Assistant en Marketing Setup).

### Escenas canónicas
| # | Escena | Qué enseña | Wow |
|---|---|---|---|
| 1 | Formulario + landing page | Captura de prospect | ⭐ el prospect aparece como Lead en Sales Cloud con su actividad |
| 2 | Scoring & grading | Puntuación por comportamiento y calificación por perfil | Lead caliente destacado para el comercial |
| 3 | Engagement Studio | Programa de nurturing con ramas por comportamiento | Recorrido visual del prospect |
| 4 | Vista del comercial | Actividad de marketing en el registro del Lead/Contact y Campaign influence | ⭐ el comercial sabe qué ha leído el cliente antes de llamar |

### Por CLI
Datos de Sales Cloud (Leads, Contacts, Campaigns) y list views/reports de Leads por score.
Los activos de Account Engagement (formularios, programas, reglas de scoring) son manuales.

### Trampas
Conector sin sincronizar → el prospect no llega a CRM. Verifica la sincronización con un prospect
de prueba antes de la demo.

---

## 4. Marketing Cloud Engagement (clásico)

Tenant aparte: **sf CLI no aplica**. El agente:
- Genera CSV de suscriptores de ejemplo (sección 5) para importar en una Data Extension.
- Redacta el contenido del email (HTML simple con personalización `%%FirstName%%`) y los textos del
  journey.
- Escribe la guía de montaje: Data Extension → email en Content Builder → journey en Journey
  Builder (entrada, email, espera, decisión) → envío de prueba al SE.
Escenas típicas: segmentación por Data Extension, email personalizado, journey con decisión,
informe de envío.

---

## 5. Datos de ejemplo comunes

Base en `assets/seed-marketing-cloud.json`. Ajustar al sector si el usuario lo indica.
- 8 Accounts (empresas españolas creíbles, varias ciudades y sectores).
- 30-40 Contacts repartidos por ciudad, cargo y sector para que los segmentos tengan recuentos
  distintos; emails `nombre.apellido@example.com`.
- **1 Contact con el email real del SE** (pídelo si no lo tienes) para previews y envíos de prueba:
  en la spec es `{{SE_EMAIL}}`; se rellena con `--var SE_EMAIL=<email>`.
- 1 Campaign "Lanzamiento Otoño" con estado *Planned* y fechas relativas.
