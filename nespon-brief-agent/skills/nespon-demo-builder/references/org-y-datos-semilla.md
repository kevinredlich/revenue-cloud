# Org desde cero y datos semilla

## Índice
1. Pre-flight de org y licencias
2. Campos que NO se pueden cargar
3. Fechas relativas
4. Especificar datos semilla en el manifiesto
5. Generar ficheros de carga (`scripts/build_seed.py`)
6. Ensayo y reset

La premisa de esta skill: **la org de partida está vacía**. Todo lo que la demo necesita tiene que
aparecer en el manifiesto: licencias, funciones de Setup, usuarios, permisos y datos. Si algo "ya
estaba en mi org", en una org nueva no estará.

---

## 1. Pre-flight de org y licencias

Decide la org (en modo a medida, documéntalo en la tabla `ORG`):

| Opción de org | Cuándo | Qué vigilar |
|---|---|---|
| **Scratch org** (desde Dev Hub, sf CLI) | Demos reconstruibles: se crea, se construye, se tira | Las funciones se piden en el fichero de definición (`features`, `settings`); confirma nombres exactos con `salesforce-skill` |
| **Developer Edition** | Demos de Sales/Service/Platform sencillas | Límites de almacenamiento y de usuarios; algunas nubes no vienen incluidas |
| **Trial específica de la nube** (FSC, Health, Field Service, Revenue, Agentforce…) | Cuando la nube ancla exige un modelo de datos o paquete propio | Caducan; apunta la fecha de expiración en `ORG` |
| **Org de partner con licencias** | Demos recurrentes del mismo tipo | Que no arrastre configuración de otra demo: asume vacía igualmente |

Para cada nube del backlog, una fila en `ORG` con la licencia o paquete requerido y su estado
(`Required` / `Verify`). Si una nube no puede estar en la org elegida, **cámbiala de org o sácala
del alcance**; no la dejes como sorpresa para el día de la demo.

Funciones de Setup que casi siempre hay que activar y que van en `SET`: Collaborative Forecasting
(y forecast types), Omni-Channel, Entitlement Management, Knowledge, Einstein/Agentforce, Path,
Set Audit Fields upon Record Creation, Experience Cloud (Digital Experiences), idioma y locale
`es_ES`, moneda EUR, zona horaria `Europe/Madrid` (o `Atlantic/Canary` / `Europe/Lisbon`).

Usuarios (`USR`): el protagonista y, si la historia lo pide, un segundo usuario (manager que
aprueba, agente que recibe el handoff, usuario externo del portal). Cada uno con perfil, licencia
y permission sets. El SE hace la demo logueado como el protagonista (o usando *Log in as*).

---

## 2. Campos que NO se pueden cargar

Calculados por el sistema, solo lectura en cualquier carga:

| Objeto | Campos | Alternativa para el WOW |
|---|---|---|
| Opportunity | `LastStageChangeDate`, `IsClosed`, `IsWon`, `HasOpenActivity`, `LastActivityDate`, `Age`* | `Stage_Entered_Date__c` (Date, 🔵) + fórmula sobre él; `IsWon/IsClosed` salen del `StageName` |
| Account / Contact / Lead | `LastActivityDate`, `LastViewedDate`, `LastReferencedDate` | Cargar Tasks/Events con `ActivityDate` relativa |
| Case | `IsClosed`, `ClosedDate`*, `IsEscalated` (según reglas) | Status cerrado + audit fields para `CreatedDate`; `ClosedDate` lo pone el sistema al cerrar |
| Cualquiera | `SystemModstamp`, `LastModifiedById`*, `Id`, campos fórmula, roll-up summary, auto-number | Diseña el WOW sobre campos que sí controlas |

\* Campos de auditoría: `CreatedDate`, `CreatedById`, `LastModifiedDate`, `LastModifiedById` **solo**
se pueden fijar al crear el registro si se activa *Set Audit Fields upon Record Creation* en Setup
(fila en `SET`) y el usuario que carga tiene ese permiso (fila en `PS`). Úsalo solo cuando el WOW
dependa de antigüedad real de creación (p. ej. casos abiertos "hace 5 días" para un SLA).

Regla práctica: si el WOW necesita "llevar X días en esta situación", la opción más robusta es un
**campo de fecha propio** que tú cargas. Declararlo como 🔵 cuesta una fila y elimina el riesgo.

---

## 3. Fechas relativas

Todas las fechas y horas de `DAT` se escriben como offsets respecto al día de carga:

- `TODAY` · `TODAY-40` · `TODAY+7` → Date
- `NOW` · `NOW-3h` · `NOW+30m` · `NOW-2d` → DateTime

Nunca `2026-03-15`. Una fecha fija hace que el dashboard "en riesgo" deje de estarlo una semana
después, que las oportunidades aparezcan en el trimestre equivocado y que el forecast se vacíe.
Las fórmulas con `TODAY()` son la otra cara del mismo problema: **recarga los datos semilla antes
de cada ensayo y de cada demo** (sección 6).

Cuidado con el trimestre: si el WOW es de forecast, pon las `CloseDate` dentro del trimestre en
curso con offsets cortos (`TODAY+5` … `TODAY+25`) y revisa que no crucen de trimestre el día de la
demo; anótalo en Supuestos.

---

## 4. Especificar datos semilla en el manifiesto

Dos niveles en la tabla `DAT`:

- **Registros WOW** → **una fila por registro**, con todos los valores que hacen que el momento
  ocurra, referencia (`ref`) para relacionarlos y la historia a la que alimentan.
- **Relleno de contexto** → una fila agregada ("20 Accounts de distribución en Murcia y Valencia,
  mix de tamaños"), porque su valor exacto no cambia la demo.

Datos creíbles pero sintéticos: nombres españoles verosímiles, CIF/NIF con formato válido pero
inventado, direcciones de calles reales solo si hay Maps (nunca datos de personas reales), emails
en dominios de ejemplo (`@example.com` o dominio inventado del cliente ficticio) para que ninguna
automatización envíe correos reales.

---

## 5. Generar ficheros de carga

`scripts/build_seed.py` convierte una especificación JSON con offsets relativos en ficheros para
`sf data import tree --plan`, con fechas materializadas al día de carga, referencias entre objetos
resueltas y comprobación de campos prohibidos.

Especificación de entrada (`seed-spec.json`):

```json
{
  "client_slug": "frutas-levante",
  "objects": [
    {"sobject": "Account", "records": [
      {"ref": "ACC1", "Name": "Frutas del Levante SL", "Industry": "Retail", "BillingCity": "Murcia"}
    ]},
    {"sobject": "Opportunity", "records": [
      {"ref": "OPP1", "Name": "Frutas del Levante - Renovación 2026", "AccountId": "@ACC1",
       "StageName": "Negotiation/Review", "Amount": 85000, "CloseDate": "TODAY+20",
       "Stage_Entered_Date__c": "TODAY-45"}
    ]}
  ]
}
```

Reglas: `ref` único por registro; lookups como `"@REF"`; objetos ordenados de padre a hijo; valores
de fecha como offsets. Uso:

```bash
python3 <skill-dir>/scripts/build_seed.py seed/seed-spec.json --out seed/out [--var SE_EMAIL=<email>]
sf data import tree --plan seed/out/seed-plan.json --target-org <alias> --json > seed/import-result.json
```

El script falla si aparece un campo de sistema no cargable, avisa si hay campos de auditoría (para
que `SET`/`PS` los habiliten) y divide en ficheros de ≤200 registros.

---

## 6. Ensayo y reset

En la sección `REHEARSAL & RESET` del manifiesto:

- **Carga con un usuario dedicado** ("Demo Loader"), distinto del protagonista. El reset es borrar
  lo creado por ese usuario (`WHERE CreatedById = '<loader>'`) y volver a cargar con fechas
  recalculadas. En scratch orgs, el reset es recrear la org.
- **Checklist de ensayo por WOW**: qué pantalla, qué registro, qué debe verse, y el plan B.
- **Antes de cada demo**: recargar semilla (fechas frescas), vaciar notificaciones y tareas
  generadas en el ensayo, comprobar login del protagonista y de usuarios externos, comprobar que
  ninguna automatización envía emails a direcciones reales (Deliverability = System email only si
  no se necesita correo).
- **Qué no tocar tras ensayar**: cualquier registro que alimente un WOW; si se modifica en el
  ensayo, se recarga.
