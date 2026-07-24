---
tags:
  - USAC
  - devschedule
  - apuntes
  - modelacion_y_simulacion_1
  - clase_magistral
curso: "MODELACION Y SIMULACION 1"
tipo: "Clase Magistral"
fecha: 2026-07-22
creado: 2026-07-22T08:36:57
---

# MODELACION Y SIMULACION 1 — Sesión de MODELACION Y SIMULACION 1

> [!INFO] Detalles de la Sesión
> - **Fecha:** 2026-07-22
> - **Curso:** [[MODELACION Y SIMULACION 1]]
> - **Tipo:** #clase_magistral
> - **Resumen:** Generado por DevSchedule AI

---

## Resumen Ejecutivo
La sesión se enfocó en un repaso de conceptos fundamentales de estadística aplicada a sistemas de colas, específicamente la esperanza matemática, la varianza y la moda. Se enfatizó la importancia práctica de la varianza mediante un caso real de importación de carbón, demostrando el impacto financiero de una alta dispersión en los tiempos de entrega.

---

## Desarrollo Académico por Secciones

### 1. Esperanza Matemática y Varianza
- **Esperanza Matemática:** Número que expresa el valor medio del fenómeno que representa una variable aleatoria. Si es discreta, es la sumatoria de la probabilidad por el valor del suceso. Si es continua, es la integral.
- **[[Varianza]]:** Medida de dispersión de una variable aleatoria sobre su media. Se denota por Sigma al cuadrado.
- *Ejemplo Práctico mencionado:* Importación de carbón desde Colombia para una generadora. Se acordó un rango permisible de llegada de barcos de más o menos 15 días, lo cual generó un impacto financiero altísimo por el exceso de inventario. Se renegoció a más o menos 7 días para reducir la varianza.

### 2. Moda y Distribuciones Teóricas
- **[[Moda]]:** En el caso discreto, es el valor que ocurre con más frecuencia. En el continuo, es el valor en el que se maximiza la función de densidad de probabilidad.
- **Diferenciación Crítica:** Es vital distinguir entre media y moda en la recolección de datos de campo para no alterar drásticamente los modelos estadísticos.
- **Modelos para Sistemas de Colas:** Los tiempos entre llegadas y de servicio son probabilísticos. Se utiliza software como Expert Fit para aproximar datos de campo a distribuciones teóricas, aunque la validez final del modelo recae en el analista.

---

## Fórmulas, Sintaxis o Puntos Clave
```math
Esperanza (Discreta): E(X) = \sum x_i \cdot P(x_i)
Esperanza (Continua): E(X) = \int_{-\infty}^{\infty} x \cdot f(x) dx
Varianza: \sigma^2 = E(X - \mu)^2 = E(X^2) - \mu^2
```

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** Reducir la varianza en los procesos logísticos y operativos es vital para evitar costos financieros innecesarios.
- **Punto de anclaje 2:** La correcta identificación de la moda y la media es el paso previo esencial para la construcción de modelos de simulación precisos en sistemas de colas.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

No se asignaron nuevas tareas ni se anunciaron evaluaciones en esta sesión.

---
*Exportado automáticamente hacia **Bóveda Obsidian USAC***
