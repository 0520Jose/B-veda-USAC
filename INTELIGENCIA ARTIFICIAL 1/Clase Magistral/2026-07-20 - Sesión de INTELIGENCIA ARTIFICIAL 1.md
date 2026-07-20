---
tags:
  - USAC
  - devschedule
  - apuntes
  - inteligencia_artificial_1
  - clase_magistral
curso: "INTELIGENCIA ARTIFICIAL 1"
tipo: "Clase Magistral"
fecha: 2026-07-20
creado: 2026-07-20T10:40:59
---

# Introducción al Aprendizaje Automático y Sistemas Legacy

> **Fecha:** 2026-07-20 | **Duración / Tipo:** Clase Magistral | **Curso:** INTELIGENCIA ARTIFICIAL 1

---

## Resumen Ejecutivo
La sesión introdujo los conceptos fundamentales de [[Machine Learning]], diferenciando entre [[Aprendizaje Supervisado]] y [[Aprendizaje No Supervisado]]. Además, se abordaron problemáticas históricas y futuras en la computación relacionadas con sistemas legacy y limitaciones de hardware, como el problema del año 2038, el uso de IPv6 y la evolución de los estándares de criptografía.

---

## Desarrollo Académico por Secciones

### 1. Tipos de Aprendizaje Automático
- **[[Aprendizaje Supervisado]]:** Se basa en la identificación de patrones en datos que ya están etiquetados. Esto significa que el modelo entrena con un historial de variables de entrada y sus correspondientes variables de salida (etiquetas).
  - *Clasificación:* Cuando la variable de salida es categórica (ej. aprobación de un crédito: sí o no). Puede ser binaria o de múltiples clases.
  - *Regresión:* Cuando la variable de salida es numérica (ej. predicción de ventas futuras basada en el historial de ventas).
- **[[Aprendizaje No Supervisado]]:** En este tipo de aprendizaje, los datos no poseen etiquetas previas. La máquina debe descubrir estructuras y crear agrupaciones por sí misma.
  - *Agrupamiento (Clustering):* Busca similitudes en los datos. Un algoritmo destacado es [[K-Means]], el cual calcula centroides (el k-ésimo promedio) y agrupa los puntos de datos más cercanos a ellos basándose en un principio análogo a la atracción gravitacional.

### 2. Limitaciones de Hardware y Sistemas Legacy
- **Problema Y2K:** Surgió debido a que en los años 70 los desarrolladores guardaban los años con solo dos dígitos por las severas limitaciones de almacenamiento y procesamiento de la época.
- **Problema del Año 2038 (Y2K38):** Deriva de la creación de UNIX. El tiempo se definió como una variable entera con signo de 32 bits contando los segundos desde 1970. Estos 32 bits se desbordarán (overflow) en el año 2038, provocando fallos en cualquier sistema que no haya migrado a 64 bits.
  - *Sistemas Afectados:* Seguros a largo plazo, bases de datos antiguas y dispositivos integrados (IoT) que aún utilizan microcontroladores de 16 o 32 bits.
- **Evolución del Protocolo IP:** A pesar de que [[IPv6]] (de 64 bits) fue introducido hace aproximadamente 25 años para solucionar la escasez de direcciones de [[IPv4]] (de 32 bits), su adopción pública mundial es lenta debido a los altísimos costos de reemplazo del equipamiento de los proveedores de red.

### 3. Criptografía y Resistencia al Cambio Tecnológico
- **Estándares de Cifrado:** El estándar actual es [[AES]] (Advanced Encryption Standard), introducido a finales de los años 90. Sin embargo, muchos sistemas de gestión de bases de datos continúan ofreciendo soporte para el obsoleto y vulnerable [[DES]] (Data Encryption Standard) por cuestiones de compatibilidad con inversiones millonarias pasadas de la industria.

---

## Fórmulas, Sintaxis o Puntos Clave

```c
// Ejemplo conceptual del problema Y2K38 causado por el desbordamiento de enteros de 32 bits
int32_t tiempo_unix_segundos = 2147483647; // Valor máximo para un entero de 32 bits con signo
tiempo_unix_segundos++; // En el año 2038 esto causará un desbordamiento a un valor negativo
```

- La migración de arquitecturas de 32 bits a 64 bits no solo depende del procesador, sino también de que el Sistema Operativo y los tipos de variables definidos a nivel de software soporten nativamente los 64 bits.

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** El aprendizaje automático requiere definir correctamente si el problema involucra datos etiquetados (supervisado) o si requiere descubrir la estructura oculta (no supervisado).
- **Punto de anclaje 2:** Las decisiones de diseño tomadas hace décadas (como variables temporales de 32 bits) siguen impactando el mantenimiento de software actual, forzando constantes migraciones para prevenir caídas sistémicas.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[TAREA / ENTREGA]:** No se asignaron nuevas tareas ni se anunciaron evaluaciones en esta sesión.
- [ ] **[EXAMEN / corto]:** No hay exámenes anunciados.
- [ ] **[ANUNCIO GENERAL]:** No se mencionaron.

*(No se asignaron nuevas tareas ni se anunciaron evaluaciones en esta sesión.)*
