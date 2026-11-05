# Convenciones Nespon

## Idioma
- Parte A (narrativa, historias, mensajes de error visibles al usuario, datos de demo): español de España.
- Parte B (manifiesto), Gherkin, API names y nombres de plataforma: inglés, con los nombres reales
  (`Opportunity`, `StageName`, `Record-Triggered Flow`).
- Labels de campos y apps: en español si el cliente trabajará en español (lo normal); el API name
  siempre en inglés.

## Moneda y fiscalidad
- Moneda EUR. En Parte A, formato español (`85.000 €`); en el manifiesto y en datos semilla, número
  plano (`85000`).
- Impuesto según **zona fiscal del cliente**, indicada en la cabecera:

| Zona | Impuesto | Tipo general | Otros tipos habituales |
|---|---|---|---|
| Península y Baleares | IVA | 21% | 10% reducido · 4% superreducido |
| Canarias | IGIC (no IVA) | 7% | 0%, 3%, 9.5%, 15% según bien/servicio |
| Ceuta y Melilla | IPSI (no IVA) | variable por ciudad y operación | confirmar con el cliente |
| Portugal | IVA (PT) | 23% continente | 22% Madeira · 16% Azores |

  Si el cliente opera en varias zonas, modela el impuesto como dato (picklist de zona fiscal o tabla
  de tipos) en lugar de un porcentaje fijo en una fórmula. Si no hay certeza del tipo aplicable,
  anótalo en Supuestos.

## Cumplimiento (solo cuando aplique al caso, no como relleno)
- RGPD/LOPDGDD: consentimiento, base legal, derecho de supresión. Datos de demo siempre sintéticos.
- ENS: sector público. DORA: banca y seguros. IDD: distribución de seguros. MiFID II: inversión.
- Datos de salud: categoría especial; nunca reales, ni siquiera anonimizados "a mano".

## Personas y empresas ficticias
- Nombres y apellidos españoles verosímiles y variados; empresas con forma jurídica (SL, SA, SLU).
- CIF/NIF con formato válido e inventado. Emails en dominios de ejemplo. Teléfonos `+34 6xx`
  inventados. Nunca datos de personas reales ni del cliente real salvo que el SE los aporte.
- Si el SE da el nombre real del cliente, úsalo para la empresa "anfitriona" de la demo; sus
  clientes y contactos siguen siendo ficticios.

## Ficheros y versiones
- En el IDE (Agentforce Vibes / VS Code): todo en el proyecto `demo-<cliente-o-nube-slug>/`:
  `GUIA-DEMO.md`, `reset.sh`, `seed/seed-spec.json`, `force-app/` con la metadata desplegada.
  En modo a medida, además `demo-backlog-<slug>-v<N>.md`.
- Si se trabaja desde claude.ai sin IDE, los mismos ficheros van a `/mnt/user-data/outputs/`.
- Slug: minúsculas, sin tildes, guiones (`Frutas del Levante SL` → `frutas-del-levante`).
- Iteraciones sobre el mismo cliente en modo a medida: sube `v<N>`, nunca sobrescribas, añade
  `CHANGELOG` y conserva las `RESTRICCIONES FIJAS` salvo que el SE las cambie explícitamente.

## Transparencia
- La cabecera lista las skills usadas y para qué.
- Todo lo no confirmado por el cliente o el SE va en Supuestos.
