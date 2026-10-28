# Changelog

## Sin publicar — endurecimiento del validador, trazabilidad y documentación

### Validador (`validate_manifest_poc.py`)
- `Fuentes consultadas (rlm-skill)`, 3.1 y 3.2 son ERROR siempre (antes solo con `--gate`); 3.3 es
  ERROR si hay filas `ESTÁNDAR A VALIDAR` o `CUSTOM REAL`.
- Aprobación ligada al contenido: `--approve "Nombre"` escribe estado, fecha y `Hash de aprobación`
  (sha256 sin las líneas de aprobación); `--gate` falla si el hash no coincide o falta. Poner
  `APROBADO` a mano ya no abre la puerta.
- `--org ALIAS`: comprueba que la `Org objetivo` declarada incluya el alias y sea sandbox/scratch/SDO.
- `--strict` (implícito en `--gate` y `--approve`): convierte en ERROR los marcadores `<completar>`,
  la falta de pre-vuelo (R2) y de casos `CASO-n` con valor esperado (R14), `CUSTOM REAL` sin
  alternativa (R12) y fuentes externas sin confirmar con describe.
- Reglas nuevas: trazabilidad HIP→NEC/EXP y NEC no cubiertas, DOC con fuente externa, DOC/DERIVADO
  sin fuente reconocible, DOC/DERIVADO con rlm-skill no disponible, avisos R6 y R8.
- Parser de tablas que respeta `\|` y barras dentro de `backticks`; una sola línea `Estado de
  revisión` anclada a inicio de línea.
- `--json` y `--export-cases`. Los valores de API incorrectos salen de
  `references/api-correcciones.json` (antes, un diccionario en el código).

### Generador (`scan_to_poc.py`)
- La numeración `NEC-n` es la misma en `intake` y en `poc`; cada `HIP-n` cita su `NEC-n`.
- Las filas de riesgo siempre aparecen (antes el modo poc solo listaba filas verdes).
- Texto del scan escapado en celdas de tabla; no sobrescribe sin `--force`; plantilla en el orden
  3, 3.1, 3.2, 3.3 con cabecera `Supuestos clave` y línea de pre-vuelo.

### Nuevos
- `scripts/compare_results.py` (casos esperados vs observados), `scripts/check_deps.py`,
  `tests/` y `.github/workflows/ci.yml`.
- `assets/ejemplo-MANIFIESTO-POC-APROBADO.md`.

### Documentación y ejemplos
- Reglas de modelado unificadas con la copia del Project (sección 7, fila de `ParentSellingModelId`,
  fuente externa para nombres de API); DERIVADO pasa a ser comprobable en lugar de prohibido.
- README, SKILL y COMO-PROBAR corregidos: ya no afirman que el ejemplo ni Prosegur pasan `--gate`.
- El caso Prosegur se mueve a `ejemplos/legacy-v1/` sin modificarlo.
