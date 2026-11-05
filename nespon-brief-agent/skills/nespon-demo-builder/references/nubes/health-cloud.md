# Playbook — Health Cloud / Life Sciences

## Org y licencias
Trial de Health Cloud / Life Sciences Cloud o SDO. Pre-flight: `PermissionSetLicense` con "Health"
o "Life Sciences". Descubre objetos con `sf sobject list` (varían según versión y paquete).

## Escenas canónicas
| # | Escena | Qué enseña | Wow |
|---|---|---|---|
| 1 | **Ficha del paciente** | Timeline clínico, condiciones, equipo de cuidado | ⭐ toda la historia en una línea de tiempo |
| 2 | **Plan de cuidados** | Care plan con objetivos, tareas y responsables | La coordinación deja de ir por teléfono |
| 3 | **Cita y seguimiento** | Programar la cita y la tarea de seguimiento automática | Nadie se queda sin seguimiento |
| 4 | **Servicio al paciente** | Caso de paciente con contexto clínico | El agente no pregunta lo que ya se sabe |
| (LS) | **Visita médica** | Visitador con histórico de interacciones con el médico | Preparación de visita en un clic |

Demo básica: **1 → 2 → 3**.

## Por CLI
Datos 100% sintéticos (categoría especial RGPD): 5 pacientes, condiciones genéricas, care team,
1 care plan por paciente, citas en `TODAY+N`.

## Manual
Plantillas de care plan y configuración del timeline si la org no las trae.

## Trampas
Nunca datos reales ni "anonimizados a mano". Terminología clínica prudente.
