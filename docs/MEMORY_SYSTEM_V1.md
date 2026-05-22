# MEMORY SYSTEM V1

## Objetivo
Permitir continuidad contextual del asistente.

## Memoria V1 almacenará:

- nombre usuario,
- preferencias,
- tareas,
- recordatorios,
- notas importantes,
- contexto reciente,
- historial útil.

## Memoria V1 NO almacenará:

- todas las conversaciones,
- datos innecesarios,
- información sensible sin consentimiento.

## Arquitectura inicial

Usuario
↓
Chat
↓
Memory Manager
↓
SQLite
↓
Recuperación contexto

## Prioridades

1. simplicidad
2. velocidad
3. bajo coste
4. privacidad
5. utilidad real

## Evolución futura

- memoria vectorial,
- embeddings,
- contexto semántico,
- perfiles personalizados.
