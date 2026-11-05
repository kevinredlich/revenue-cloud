# Formato de BRIEF-CLIENTE.md

Una página. Es lo primero que lee el SE tras dar los requerimientos y sirve para decidir **DEMO o
POC**. Se genera en la Fase 0 junto a `MANIFIESTO-NECESIDADES.md` (formato en
`revenue-cloud-poc/references/manifiesto-necesidades.md`), que contiene el detalle de cada `NEC-n`.
Español de España. Nada que no venga de la información aportada: lo que se deduce va como supuesto.

```markdown
# BRIEF DEL CLIENTE — <Cliente> — v<N>

**Origen de la información:** <documento, correo, notas, scan de CPQ Scout…> · **Fecha:** <fecha>
**Cliente:** … · **Sector:** … · **Zona fiscal:** …

## Contexto
<3-5 líneas: quién es, qué usa hoy, qué quiere conseguir>

## Necesidades (resumen)
| NEC | Necesidad | Semáforo | Fuente |
|-----|-----------|----------|--------|
| NEC-1 | … | 🟢/🟡/🔴 | Brief / Supuesto / Scan CPQ Scout |
(el detalle y las preguntas de refinamiento están en MANIFIESTO-NECESIDADES.md; la numeración es la misma)

## Restricciones y supuestos
- Restricciones del cliente / del SE (literales): …
- Supuestos (no confirmados): …

## Consultas a rlm-skill (Regla cero)
<sub-skills y artículos de Help 264 leídos para clasificar la viabilidad; "no disponible" si no se pudo>

## Recomendación: DEMO o POC
**Recomiendo:** DEMO | POC (migración si el origen es un scan)
**Por qué:** <1-3 líneas ligadas a los NEC; POC si hay 🟡/🔴 o una duda técnica a comprobar; DEMO si todo es 🟢 y el objetivo es mostrar el recorrido>
**Qué haría cada camino:** DEMO → manifiesto de demo, pitch y datos · POC → hipótesis, experimento e informe de viabilidad
**Decide el SE.** Hasta que no lo confirme no se genera nada más.

## Decisión
**Modalidad confirmada:** — · **Confirmado por:** — · **Fecha:** —
```
