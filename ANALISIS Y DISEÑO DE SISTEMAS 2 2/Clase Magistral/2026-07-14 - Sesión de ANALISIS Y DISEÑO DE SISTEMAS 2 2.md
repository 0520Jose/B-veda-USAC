---
tags:
  - USAC
  - devschedule
  - apuntes
  - analisis_y_dise_o_de_sistemas_2_2
  - clase_magistral
curso: "ANALISIS Y DISEÑO DE SISTEMAS 2 2"
tipo: "Clase Magistral"
fecha: 2026-07-14
creado: 2026-07-14T08:14:52
---

# Introducción a la Ingeniería de Software, Evolución de la Computación y Metodología del Curso

> **Fecha:** 2026-07-14 | **Duración / Tipo:** Clase Magistral | **Curso:** ANALISIS Y DISEÑO DE SISTEMAS 2 2

---

## Resumen Ejecutivo
La sesión inaugural del curso de [[Análisis y Diseño de Sistemas 2]] abarcó la presentación general del programa académico, la metodología de trabajo y los fundamentos históricos de la computación hasta la actualidad. Se profundizó en el rol del ingeniero de software frente a la evolución tecnológica constante, contrastando paradigmas tradicionales con tecnologías modernas como [[Cloud Computing]], [[Inteligencia Artificial]], [[Computación Cuántica]] y [[DNA Computing]]. Finalmente, se establecieron las reglas de evaluación, normativas de asistencia, metodologías grupales y el papel del laboratorio en la formación práctica del estudiante.

---

## Desarrollo Académico por Secciones

### 1. Evolución de la Computación y Paradigmas Tecnológicos
- **[[Historia de la Computación]] y Primeras Generaciones:** La computación evolucionó desde instrumentos de cálculo manuales como el ábaco (Asia menor) y la pascalina de Blaise Pascal (1642, diseñada para el cálculo de ingresos fiscales en Francia) hasta la primera computadora comercial Univac 1 (1951-1952, empleada en el recuento de votos presidenciales en Estados Unidos) y las máquinas IAS de John von Neumann.
- **Transición del Hardware (1ª a 4ª Generación):**
  - **Primera y Segunda Generación (1951-1963):** Uso de tubos al vacío, alto consumo eléctrico, gran generación de calor y lentitud extrema. Posteriormente, la introducción de transistores permitió reducir tamaño, mejorar confiabilidad y desarrollar lenguajes como COBOL y FORTRAN, así como el primer simulador de vuelo militar (Whirlwind).
  - **Tercera y Cuarta Generación (1964-1983):** Integración de circuitos en pastillas de silicio (ej. PDP-8 de Digital Equipment Corporation) y la aparición del microprocesador (LSI y VLSI), unificando la unidad de control y la unidad aritmético-lógica en un solo chip, dando origen a la computadora personal (PC) e IBM 360.
- **Quinta a Séptima Generación (1984 hasta la actualidad):**
  - **[[Cloud Computing]] (Nube):** Desplazamiento del almacenamiento y procesamiento desde discos duros locales hacia servidores remotos distribuidos globalmente, permitiendo servicios masivos en línea y escalabilidad elástica.
  - **[[Inteligencia Artificial]] y Unidades de Procesamiento Gráfico (GPU):** Las GPUs pasaron de ser tarjetas dedicadas exclusivamente a videojuegos a integrarse en los microprocesadores como hardware esencial para procesar millones de parámetros en redes neuronales y modelos de aprendizaje profundo (ej. chips neuromórficos).
  - **[[Computación Cuántica]]:** Paradigma basado en principios mecánicos cuánticos (superposición de estados) diseñado para solucionar cuellos de botella en bases de datos masivas que el hardware clásico no es capaz de procesar eficientemente.
  - **[[DNA Computing]] (Computación Biológica):** Línea de vanguardia tecnológica que utiliza moléculas biológicas y cadenas de ADN para almacenar información digital y ejecutar operaciones lógicas complejas con una densidad de datos y eficiencia energética muy superiores al silicio tradicional.
- *Ejemplo Práctico mencionado:* Comparación entre la gestión de fotografías en discos duros locales de hace dos décadas frente al almacenamiento moderno en la nube (ej. Google Fotos con clasificación automática y procesamiento por categorías).

### 2. Fundamentos de la [[Ingeniería de Software]] y Diseño
- **Concepto de Ingeniería:** Aplicación del ingenio, las matemáticas, las ciencias y un conjunto de reglas, estándares y herramientas validadas para la resolución sistemática de problemas complejos de la humanidad. El foco supremo siempre debe ser el usuario final, a quien se debe el diseño y funcionamiento de los sistemas.
- **Diferencia entre Análisis y Diseño:**
  - **Análisis:** Proceso de descomponer un sistema complejo o un problema integral en sus partes constituyentes y requerimientos elementales para comprender su comportamiento y límites.
  - **Diseño:** Proceso de estructurar, componer y definir la arquitectura, componentes, interfaces y patrones necesarios para construir la solución tecnológica que cumpla con los requerimientos analizados.
- **El Cambio como Constante de la Profesión:** La tecnología de software evoluciona rápidamente (ej. transición del JavaScript estático de 2007 al ecosistema moderno con Node.js y frameworks avanzados). Por ello, diseñar software requiere anticipar y gestionar el cambio arquitectónico mediante el dominio sólido de los fundamentos teóricos y las bases formales.
- **Uso Crítico de la Inteligencia Artificial en el Desarrollo:** Aunque la IA generativa optimiza la redacción de código, el profesional debe comprender a fondo la lógica y las bases teóricas. Un uso desmedido sin análisis crítico o sin especificar correctamente los requerimientos (tanto funcionales como no funcionales) provoca alucinaciones, código deficiente y vulnerabilidades estructurales en las organizaciones.

### 3. Estructura, Normativa y Metodología de [[Análisis y Diseño de Sistemas 2]]
- **Objetivos y Enfoque del Curso:** Situar al estudiante en el rol de arquitecto de software, capacitándolo para identificar, evaluar y aplicar estilos arquitectónicos, patrones de diseño y tácticas para garantizar [[Atributos de Calidad]] y [[Requerimientos No Funcionales]] (rendimiento, escalabilidad, mantenibilidad, seguridad).
- **Metodología e Hibridez Académica:**
  - Clases magistrales virtuales/híbridas con duración de 2 períodos, martes y jueves.
  - Realización de ejercicios y hojas de trabajo en tiempo real (ej. hoja de trabajo programada para los primeros 30 minutos de la próxima clase del jueves).
  - Trabajo colaborativo obligatorio en grupos para presentaciones y resolución de casos reales.
- **Reglamento de Asistencia y Evaluaciones:**
  - **Asistencia Mínima:** Es obligatorio acumular un 90% de asistencia (medida a través de la entrega de ejercicios y actividades en clase) para tener derecho a las evaluaciones parciales.
  - **Exposiciones Grupales:** El uso de cámara encendida es estrictamente obligatorio durante las exposiciones grupales para evaluar la gesticulación y desenvolvimiento profesional del estudiante.

---

## Fórmulas, Sintaxis o Puntos Clave
*A continuación se resumen los conceptos estructurales, estándares y clasificaciones arquitectónicas introducidas para el curso:*

```text
================================================================================
JERARQUÍA DEL DESARROLLO ARQUITECTÓNICO EN INGENIERÍA DE SOFTWARE
================================================================================
1. Requerimientos Funcionales (RF)  --> Lo que el sistema DEBE HACER (lógica de negocio).
2. Requerimientos No Funcionales (RNF) --> Cómo el sistema DEBE COMPORTARSE (Atributos de Calidad: rendimiento, seguridad, disponibilidad).
3. Tácticas Arquitectónicas           --> Decisiones específicas de diseño para alcanzar los RNF.
4. Patrones y Estilos de Arquitectura  --> Soluciones estructurales probadas para problemas comunes de diseño (UML como estándar universal de comunicación).
================================================================================
```

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** La ingeniería de software exige el dominio riguroso de principios teóricos fundamentales y estándares universales como [[UML]] y patrones arquitectónicos, permitiendo al arquitecto de sistemas adaptarse con agilidad a transformaciones disruptivas como la IA, la nube y la computación biológica.
- **Punto de anclaje 2:** El curso articula los conocimientos previos de recolección de requerimientos de [[Análisis y Diseño de Sistemas 1]] con la evaluación avanzada de atributos de calidad, preparando al estudiante para diseñar arquitecturas empresariales resilientes, medibles y orientadas a los objetivos de negocio.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[TAREA / ENTREGA]:** Hoja de Trabajo en Clase sobre principios y repaso de Análisis 1. Se realizará en los primeros 30 minutos de la sesión del jueves. *(Fecha límite mencionada: 2026-07-16 al inicio del período)*
- [ ] **[TAREA / ENTREGA]:** Inscripción obligatoria en el Formulario de Asignación de Laboratorio compartido por el auxiliar Juan Carlos Aragón. *(Fecha límite mencionada: Inmediata / Primera semana de clases)*
- [ ] **[EXAMEN / corto]:** Primer Examen Parcial del curso (10 puntos netos). Evaluación presencial o virtual sujeta a disposiciones de la facultad por situación universitaria. *(Fecha límite mencionada: 2026-08-11)*
- [ ] **[EXAMEN / corto]:** Segundo Examen Parcial del curso (13 puntos netos) y Tercer Examen Parcial (13 puntos netos). *(Fecha límite mencionada: Por confirmar en calendario de la facultad)*
- [ ] **[ANUNCIO GENERAL]:** Las exposiciones grupales de casos requieren obligatoriamente cámara encendida de todos los integrantes del grupo. No se aceptan entregas extemporáneas ni exposiciones individuales.

---

## Archivo de Transcripción y Referencia Cruda

> [!NOTE]- Ver Transcripción de Google Meet (Desplegable)
> *(La sesión magistral inaugural fue impartida por la Inga. Mirna Ivonne Aldana Larrazábal con la participación del Auxiliar de Laboratorio Juan Carlos Aragón Bamaca. La discusión abarcó desde la evolución del hardware desde 1642 hasta DNA Computing y la metodología formal y sistema de calificación de la materia Análisis y Diseño de Sistemas 2).*
