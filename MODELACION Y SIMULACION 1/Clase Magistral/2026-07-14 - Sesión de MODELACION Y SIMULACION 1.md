---
tags:
  - USAC
  - devschedule
  - apuntes
  - modelacion_y_simulacion_1
  - clase_magistral
curso: "MODELACION Y SIMULACION 1"
tipo: "Clase Magistral"
fecha: 2026-07-14
creado: 2026-07-14T10:40:46
---

# Fundamentos de Simulación, Selección de Distribuciones y Validación de Modelos

> **Fecha:** 2026-07-14 | **Duración / Tipo:** Clase Magistral | **Curso:** MODELACION Y SIMULACION 1

---

## Resumen Ejecutivo
La sesión inaugural de [[Modelación y Simulación 1]] se centró en la metodología científica y técnica para construir modelos de simulación válidos, creíbles y con un nivel de detalle alineado estrictamente a los objetivos organizacionales. Se profundizó en el análisis crítico y selección de [[Distribución de Probabilidad]] para datos de entrada, la discriminación de ajustes erróneos del software, el manejo de distribuciones truncadas por límites físicos y la modelación bajo escasez de datos históricos. Asimismo, se introdujo el uso de la plataforma [[Simio]], la evolución hacia la [[Industria 5.0]] y las normas académicas estrictas de evaluación y política antiplagio del curso.

---

## Desarrollo Académico por Secciones

### 1. Análisis y Selección Crítica de Distribuciones de Entrada
- **Discriminación de Ajustes del Software:** Las herramientas de ajuste estadístico de curvas sugieren distribuciones teóricas basándose en [[Pruebas de Bondad de Ajuste]] matemáticas puras, pero desconocen la naturaleza lógica y física del fenómeno en estudio.
  - **Limitación de la [[Distribución Normal]]:** Si un software sugiere una distribución normal para variables temporales (como tiempos de servicio en planta o tiempos de transporte), el modelador debe rechazarla o restringirla de inmediato. La distribución normal tiene un dominio que incluye valores negativos, lo cual es físicamente imposible para mediciones de tiempo y genera inconsistencias graves en el motor de simulación.
- **Distribuciones Truncadas o Desplazadas (*Shifted Distributions*):** Se aplican cuando el sistema real posee un límite físico o logístico mínimo infranqueable. La función de densidad de probabilidad debe iniciar con un desplazamiento en el eje temporal.
  - *Ejemplo Práctico mencionado:* Modelación del tiempo de transporte de carga pesada entre la Ciudad de Guatemala y Puerto Quetzal por la autopista en construcción (concesión público-privada). Si el modelo arroja traslados de 1 o 1.5 horas, el dato se descarta por ser físicamente imposible en condiciones reales de tráfico y topografía. Tras la investigación de campo, se determina un umbral de inicio de al menos 2 horas como tiempo mínimo de tránsito, desplazando la distribución de probabilidad a partir de dicho punto de partida.
- **Modelación con Ausencia o Disrupción de Datos:** Ante cisnes negros o transformaciones estructurales (como la pandemia de COVID-19), los datos históricos pierden validez debido a cambios en el sistema (restricciones de aforo, sistemas por citas programadas). El modelador debe establecer supuestos transitorios robustos y recalcular los parámetros de la distribución (como la media de una [[Distribución de Poisson]]) en cuanto se normalice la toma de muestras de la nueva realidad.

### 2. Validez, Credibilidad y Alcance del Modelo de Simulación
- **Diferenciación entre Validez y Credibilidad:**
  - **Validez del Modelo (*Model Validity*):** Demostración rigurosa mediante pruebas estadísticas y matemáticas de que el comportamiento del modelo refleja con fidelidad el sistema real en estudio.
  - **Credibilidad (*Model Credibility*):** Confianza que los tomadores de decisiones (Gerencia General, Junta Directiva) depositan en la herramienta para invertir capital en base a sus resultados. Un modelo válido sin credibilidad directiva es inútil para la organización.
- **Alcance Arquitectónico y Nivel de Detalle (*Model Scope*):**
  - Todo modelo representa únicamente el subconjunto de variables estrictamente necesarias para responder al objetivo planteado; es un error intentar modelar el 100% de la realidad operativa.
  - *Ejemplo Práctico mencionado:* Simulación de una panadería industrial que adquirió un contrato masivo de producción de pan. El objetivo exclusivo del modelo era optimizar la utilización de maquinaria en planta y determinar el momento exacto para invertir en un nuevo horno industrial. Por lo tanto, se asumió suministro continuo e ideal de materia prima en la entrada y empaque/reparto instantáneo en la salida. No se modeló la logística externa porque no aportaba al objetivo central de capacidad instalada.
  - **Control del Alcance (*Anti-Scope Creep*):** Si el objetivo original requiere un diseño tipo "vehículo 4x4" enfocado en planta, no debe transformarse arbitrariamente en un "Fórmula 1" incorporando bodegas, compras y rutas de reparto, ya que esto compromete el rendimiento y el enfoque analítico.

### 3. Generación de [[Variables Aleatorias]] y Análisis de Salida
- **Generación de Variables y Escenarios:** El motor de simulación evalúa escenarios mediante la generación pseudoaleatoria de variables continuas, discretas, vectores aleatorios y variables correlacionadas. La validación requiere sustento estadístico formal más allá de la calidad visual de las animaciones en 3D.
- **Estratificación de Escenarios (*Confounding Factors*):** Mezclar poblaciones heterogéneas en un solo conjunto de datos distorsiona la forma de las curvas de probabilidad y oculta el comportamiento real.
  - *Ejemplo Práctico mencionado:* Modelar el flujo de ingreso vehicular y estudiantil al Campus Central de la Universidad de San Carlos de Guatemala (USAC). Si se aglomeran todos los datos de ingreso, el modelo falla. Es obligatorio estratificar por variables de corte: 1er o 2do semestre, cursos de vacaciones de junio o diciembre, puerta de ingreso (Avenida Petapa vs. Periférico) y jornada horaria (matutina, vespertina o nocturna).
- **Análisis de Salida y Estado Estable:** Distinción entre simulaciones de sistemas terminantes (*Terminating Simulations*) y simulaciones en estado estable (*Steady-State Simulations*). Aplicación de [[Técnicas de Reducción de Varianza]] para afinar la precisión en los intervalos de confianza sin multiplicar el costo computacional.
- **Evolución hacia la [[Industria 5.0]]:** Con herramientas avanzadas como [[Simio]] en el sistema operativo Windows, la simulación trasciende el [[Gemelo Digital]] de la [[Industria 4.0]] para integrarse en paradigmas de [[Industria 5.0]] (promovidos por líderes tecnológicos mundiales como Huawei), centrados en la resiliencia y la interacción humano-máquina.

### 4. Estructura Académica, Metodología y Normativa de Evaluación
- **Ponderación Formal de la Clase Magistral (65 puntos netos de Zona + 35 de Final):**
  - **Tres Exámenes Parciales:** 10 puntos netos cada uno (30 puntos en total).
  - **Tareas, Ejercicios en Clase y Asistencia:** 10 puntos netos.
  - **Proyecto de Simulación (Teoría):** 35 puntos netos.
  - **Examen Final:** 25 puntos netos para completar los 100 puntos de promoción del curso.
- **Laboratorio y Práctica Específica:** El laboratorio es coordinado de manera independiente y exclusiva por el Auxiliar Alben Adrián Ramírez Gómez. Cuenta con su propio proyecto de laboratorio y ponderación, siendo requisito obligatorio para tener derecho a examen final.
- **Política Estricta de Cero Plagio en Simulación:** Está absolutamente prohibida la duplicidad o copia de modelos de simulación en [[Simio]] entre estudiantes o grupos. Al detectarse dos modelos idénticos, la calificación es 0 automático para todos los involucrados sin excepción.

---

## Fórmulas, Sintaxis o Puntos Clave
*A continuación se resumen los criterios matemáticos y lógicos para el ajuste de distribuciones temporales y análisis de salidas:*

```text
================================================================================
CRITERIOS DE SELECCIÓN Y VALIDACIÓN DE DISTRIBUCIONES EN SIMULACIÓN
================================================================================
1. REGLA DEL DOMINIO FÍSICO:
   Para variables de tiempo (T >= 0):
   [RECHAZAR] Distribución Normal pura N(mu, sigma^2) si P(T < 0) > 0 es significativo.
   [APLICAR]  Distribuciones no negativas: Exponencial, Weibull, Log-Normal, Gamma.

2. DISTRIBUCIONES DESPLAZADAS (SHIFTED DISTRIBUTIONS):
   Si existe un tiempo mínimo logístico inevitable T_min > 0:
   f_desplazada(t) = f(t - T_min) para t >= T_min (0 para t < T_min).

3. PROCESO DE VALIDACIÓN DE 3 ETAPAS:
   A) Verificación de Independencia (Autocorrelación de la muestra).
   B) Selección de Familia de Distribución (ej. Poisson para llegadas).
   C) Pruebas de Bondad de Ajuste (Chi-Cuadrado, Kolmogorov-Smirnov) sobre parámetros estimados.
================================================================================
```

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** La construcción de un modelo de simulación exitoso requiere la combinación indisociable de rigurosidad estadística en las distribuciones de entrada, control estricto del nivel de detalle según el objetivo y la capacidad de demostrar credibilidad ante la alta dirección.
- **Punto de anclaje 2:** El curso prepara al futuro ingeniero no solo en el uso técnico de plataformas avanzadas como [[Simio]] dentro de la [[Industria 4.0]] e [[Industria 5.0]], sino en el juicio crítico para discriminar resultados computacionales que contradigan la realidad física y logística del entorno.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[TAREA / ENTREGA]:** Solicitud y activación de la licencia académica para estudiantes de la plataforma de simulación [[Simio]] utilizando el correo institucional de la universidad (instalación en entorno Windows para el laboratorio). *(Fecha límite mencionada: Inmediata / Primera semana de laboratorio)*
- [ ] **[EXAMEN / corto]:** Primer Examen Parcial del curso (ponderación de 10 puntos netos sobre 100). *(Fecha límite mencionada: Por confirmar en calendario de la facultad)*
- [ ] **[EXAMEN / corto]:** Segundo Examen Parcial (10 puntos netos) y Tercer Examen Parcial (10 puntos netos, mencionado para el 14 de octubre según calendario programado). *(Fecha límite mencionada: 2026-10-14 para el 3er Parcial)*
- [ ] **[ANUNCIO GENERAL]:** Todos los modelos y proyectos desarrollados en [[Simio]] están sujetos a auditoría cruzada antiplagio. Modelos idénticos o copiados entre grupos obtienen una calificación de 0 sin derecho a apelación.
- [ ] **[ANUNCIO GENERAL]:** Las consultas y gestión de proyectos de laboratorio deben realizarse directamente con el Auxiliar Alben Adrián Ramírez en horarios prudenciales y respetando el calendario del laboratorio.

---

## Archivo de Transcripción y Referencia Cruda

> [!NOTE]- Ver Transcripción de Google Meet (Desplegable)
> *(La sesión magistral inaugural fue impartida por el Ing. César Augusto Fernández Cáceres con la participación del Auxiliar de Laboratorio Alben Adrián Ramírez Gómez. La clase se centró en la selección de distribuciones de probabilidad, validez y credibilidad de modelos en Simio, y el sistema formal de calificación y normativas del curso).*
