# Playbook — Data Cloud (Data 360)

## Org y licencias
Org con Data Cloud provisionado (SDO o org con licencia). Pre-flight: `PermissionSetLicense` con
"Data Cloud" o "CDP". El aprovisionamiento (Data Cloud Setup → Get Started) puede tardar hasta una
hora: si hace falta, es lo primero.

## Escenas canónicas
| # | Escena | Qué enseña | Wow | Plan B |
|---|---|---|---|---|
| 1 | **Fuentes conectadas** | CRM + una segunda fuente (compras online / tienda / app) en streams | Los silos entran sin proyecto de integración | Streams ya ingeridos |
| 2 | **Perfil unificado** | Identity resolution junta a la misma persona de dos fuentes | ⭐ "Ana García" de CRM y "a.garcia" de la web son una sola persona | Perfil unificado ya calculado |
| 3 | **Insight calculado** | Valor de vida del cliente o compras últimos 90 días | Métrica viva, no un Excel | Insight ya calculado |
| 4 | **Segmento y activación** | Segmento por insight activado hacia Marketing o CRM | ⭐ de dato a acción | Segmento publicado |
| 5 | **Dato en el CRM** | El insight visible en la ficha del contacto | El comercial ve lo que compra online | Componente en la record page |

Demo básica: **1 → 2 → 3 → 4**.

## Por CLI
- CRM: 20-30 Contacts con emails `@example.com`.
- Segunda fuente: el agente genera un CSV (`seed/compras-online.csv`) con 60-100 compras de los
  mismos clientes, con **variaciones intencionadas** (email con mayúsculas, nombre abreviado,
  teléfono con/sin +34) para que la identity resolution tenga algo que unir.

## Manual
Crear el data stream del CRM (conector Salesforce CRM) y el de la segunda fuente (subida de fichero
o Ingestion API, según disponibilidad en la org); mapear a DMOs (Individual, Contact Point Email,
Sales Order); ruleset de identity resolution (coincidencia por email normalizado y nombre + teléfono);
calculated insight; segmento. El agente redacta nombres, fórmulas y reglas exactas.

## Trampas
Un CDP sin dos fuentes no impresiona. Los procesos (ingesta, resolución, insights) no son
instantáneos: todo debe estar calculado antes de la demo; en directo se enseña el resultado.
