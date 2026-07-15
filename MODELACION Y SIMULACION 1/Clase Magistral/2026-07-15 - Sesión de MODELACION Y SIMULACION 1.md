---
tags:
  - USAC
  - devschedule
  - apuntes
  - modelacion_y_simulacion_1
  - clase_magistral
curso: "MODELACION Y SIMULACION 1"
tipo: "Clase Magistral"
fecha: 2026-07-15
creado: 2026-07-15T08:50:54
---

# Gestión de Incertidumbre, Gemelos Digitales, Componentes del Sistema y Análisis del Entorno Exógeno

> **Fecha:** 2026-07-15 | **Duración / Tipo:** Clase Magistral | **Curso:** MODELACION Y SIMULACION 1

---

## Resumen Ejecutivo
La segunda sesión magistral de [[Modelación y Simulación 1]] abordó el manejo riguroso de la [[Incertidumbre]] y el [[Ruido]] en los modelos de simulación, enfatizando la necesidad de someter toda asunción a una verificación estricta y a una memoria de cálculo para mantener los errores dentro de márgenes tolerables. Se profundizó en el concepto de [[Gemelo Digital]] (*Digital Twin*) y sus componentes, las ventajas y costos de las plataformas especializadas como [[Simio]] y [[SPSS]], y la aplicación de [[Design Thinking]] para desarrollar herramientas orientadas a usuarios finales reales. Finalmente, se definieron los componentes estructurales de todo sistema de simulación ([[Entidades]], [[Atributos]], [[Actividades]], [[Estado del Sistema]] y [[Eventos]]) y se ilustró con un caso de estudio real de logística marítima el impacto crítico de las variables del entorno ([[Eventos Exógenos]]) sobre la precisión y validez operativa de un modelo.

---

## Desarrollo Académico por Secciones

### 1. Gestión de Incertidumbre, Ruido y Escepticismo Metodológico en Simulación
- **[[Incertidumbre]] y [[Ruido]] como Realidades Inevitables:** Al simular cualquier fenómeno físico u organizacional, la incertidumbre y el ruido estadístico existen de manera inherente. El objetivo del modelador no es intentar eliminarlos mágicamente, sino calcular su magnitud y acotarlos dentro de niveles de tolerancia permisibles (por ejemplo, una desviación de ±5% es operativamente tolerable, mientras que un margen de error del 70% resulta inadmisible y descarta la utilidad de la herramienta).
- **Escepticismo Metodológico y Análisis de Datos:**
  - **No Creer a Ciegas en los Modelos:** Existe la máxima de que "en los modelos de simulación no se debe creer a ciegas". Es indispensable someter el sistema a un riguroso [[Análisis de Datos de Entrada]] y [[Análisis de Datos de Salida]], verificando la calidad de la información alimentada y contrastando los resultados generados.
  - **Documentación Estricta de [[Supuestos del Modelo]]:** Todo modelo se construye sobre un conjunto de simplificaciones e hipótesis previas. Es obligatorio redactar y registrar formalmente cada supuesto asumido durante el diseño arquitectónico.
  - **Memoria de Cálculo de Incertidumbre:** A partir de los supuestos documentados, se debe calcular matemáticamente la incertidumbre del sistema y elaborar una memoria de cálculo técnica que demuestre ante la auditoría o la gerencia que las variaciones esperadas se mantienen en un rango tolerable.
- **Involucramiento del Experto Técnico (*Subject Matter Expert*):** El ingeniero en sistemas o modelador raras veces es el especialista total del dominio operativo (ej. física espacial, refinación, manufactura). Por ello, es condición obligatoria identificar e integrar desde el primer día al experto en el tema dentro del equipo de modelación para validar lógica, flujos y asunciones.

### 2. Arquitectura de [[Gemelo Digital]] (*Digital Twin*) y Casos de Estudio en la Industria
- **Concepto y Componentes de un [[Gemelo Digital]]:** Introducido como preludio a los contenidos de [[Modelación y Simulación 2]], un gemelo digital constituye la representación y réplica virtual en tiempo real de un sistema físico o maestro. Se divide en dos componentes fundamentales:
  - **[[Digital Master]] (Maestro Digital):** El sistema físico, maquinaria, planta o activo real operativo en el mundo tangible.
  - **[[Digital Shadow]] (Sombra Digital):** El modelo virtual o de simulación que se alimenta continuamente con datos telemétricos en tiempo real provenientes del maestro físico para predecir comportamientos, evaluar riesgos y ejecutar mantenimiento predictivo.
- **Caso de Estudio Aeronáutico y Aeroespacial (Transbordador Espacial de la [[NASA]]):**
  - Cuando la NASA requiere determinar si un daño sufrido en la capa de protección térmica de un transbordador espacial representa un riesgo letal al reingresar a la atmósfera terrestre, la prueba no es factible en el mundo real ni se puede esperar hasta el momento del descenso (si se espera a evaluar en el reingreso, el accidente y la pérdida de vidas humanas ya habrían ocurrido).
  - A través del *Digital Shadow*, la NASA alimenta la simulación con datos de sensores en tiempo real para verificar si la nave puede ingresar de manera segura o si es imperativo ejecutar una maniobra de reparación orbital previa.
- **Caso de Estudio en Manufactura y Ampliación de Capacidad:**
  - Experiencia profesional del docente en la evaluación técnica de ampliación de una planta industrial donde equipos críticos de manufactura se compartían entre múltiples líneas de producción.
  - El modelo de simulación permitió integrar las proyecciones de demanda de nuevos productos para determinar con precisión si la maquinaria existente era suficiente, en qué momento exacto se presentaría un cuello de botella (*bottle-neck*) y cuándo resultaba financieramente necesario adquirir nuevos activos fijos.

### 3. Ventajas Estratégicas, Desventajas Económicas y Resistencia Organizacional
- **Ventajas Operativas de la Simulación:**
  - **Flexibilidad y Análisis de Escenarios (*What-If*):** Una vez validado y construido el modelo base, se pueden modificar parámetros y políticas logísticas de forma inmediata y sistemática para evaluar múltiples estrategias sin interrumpir la operación real.
  - **Economía y Seguridad:** Mejorar el rendimiento de un sistema experimental mediante simulación es órdenes de magnitud más económico y seguro que realizar ensayos de prueba y error en el mundo físico (ej. probar políticas de evacuación o evaluar cargas extremas en aviones sin poner en riesgo vidas humanas).
  - **Resolución de Sistemas Complejos:** Cuando un sistema presenta alta variabilidad e interdependencias, las soluciones analíticas puras (ecuaciones matemáticas cerradas) se vuelven inviables; la simulación es el único medio viable para obtener respuestas confiables.
  - **Detección de Cuellos de Botella y Optimización de Inventarios:** Facilita el análisis del flujo del Trabajo en Proceso (*WIP - Work in Process*), el movimiento de materiales y el dimensionamiento de bodegas, previniendo inversiones de capital innecesarias o deficitarias.
- **Desventajas y Barreras de Implementación:**
  - **Costo en Tiempo y Recursos:** El desarrollo, programación y validación rigurosa de modelos consume tiempo y requiere personal altamente calificado.
  - **Costo de Licenciamiento de Software:** Herramientas analíticas y de simulación de nivel industrial como [[SPSS]] y [[Simio]] tienen costos de adquisición elevados. Sin embargo, su valor se justifica plenamente por su potencia computacional y precisión analítica ("valen lo que cuestan"); la selección de la herramienta siempre debe obedecer a una evaluación de factibilidad económica ("si la chamarra da o no da").
  - **Intensidad Computacional:** Evaluar combinaciones complejas de escenarios para alcanzar soluciones óptimas exige una gran cantidad de corridas computacionales y capacidad de procesamiento.
- **Resistencia al Cambio y Escepticismo Gerencial ("Cuando Cristo empieza a padecer"):**
  - En el ámbito corporativo guatemalteco e internacional, es frecuente que las organizaciones contraten consultorías de simulación con la expectativa preconcebida de que el modelo confirme y justifique decisiones que la gerencia ya tomó de antemano.
  - Si el modelo está bien construido y sus corridas demuestran que la decisión gerencial deseada es errónea o genera pérdidas ("cuando el modelo no da las respuestas que uno quisiera"), surge una fuerte resistencia psicológica: la gerencia tiende a desacreditar la herramienta argumentando que "el modelo está malo o no funciona".
  - La credibilidad del modelo se gana demostrando rigor en la recopilación de datos de calidad, transparencia en los supuestos y coherencia en las memorias de cálculo.
- **Unicidad del Modelo y Etica Profesional:**
  - La construcción de modelos es un arte técnico que se perfecciona con la experiencia práctica.
  - **Principio de Diversidad en Modelación:** Si dos ingenieros o analistas competentes abordan un mismo problema de forma independiente, sus modelos compartirán similitudes en la lógica fundamental del sistema, pero es estadísticamente improbable que sean idénticos. Esto refuerza la advertencia académica del curso sobre la estricta originalidad de los proyectos semestrales y la prohibición del plagio.

### 4. Áreas de Aplicación de la Simulación en la Era de la [[Industria 5.0]]
- **Manufactura y Producción:** Optimización de líneas de ensamble, balanceo de cargas de trabajo y dimensionamiento de planta.
- **Modelación de Negocios (*Business Modeling*):** Evaluación de estrategias de mercado, proyecciones financieras y comportamiento de corporaciones (tema central en la continuación de la materia).
- **Ingenería Civil y Construcción:** Gestión de proyectos complejos, programación de obra y análisis estructural utilizando herramientas como *Civil 3D* y software de elementos finitos.
- **Logística, Transporte y [[Supply Chain Management]]:** Optimización de rutas de distribución, redes de abastecimiento multimodal y gestión de inventarios en puertos y aeropuertos.
- **Aplicaciones Militares y Aeroespaciales:** Simulación de combates, logística de defensa y evaluación aerodinámica y térmica de vehículos espaciales.
- **Sector Médico y de Salud:** Planificación hospitalaria, simulación de flujos de emergencias, entrenamiento de cirugías invasivas y modelos epidemiológicos.
- **Evolución Tecnológica ([[Industria 4.0]] e [[Industria 5.0]]):** Transición desde el enfoque de automatización y conectividad total de la Industria 4.0 hacia el nuevo paradigma de la [[Industria 5.0]] (liderado por gigantes tecnológicos como Huawei), donde la inteligencia artificial, los gemelos digitales y la simulación se centran en la resiliencia operativa y la sinergia humanocéntrica.

### 5. El Factor Humano y la Aplicación de [[Design Thinking]] en Modelación
- **Diseño Centrado en el Usuario Final:** Al construir una herramienta de simulación, el ingeniero no debe diseñar el modelo pensando en sí mismo como usuario, sino en el cliente, consultor o analista de negocios que interactuará con la interfaz y ejecutará las corridas.
- **Lecciones de *The Design of Everyday Things* de Don Norman:**
  - El docente referenció las clásicas "puertas de Norman", donde un mal diseño industrial provoca confusión instantánea en las personas sobre si deben empujar o jalar, pese a que para el diseñador parecía "obvio".
  - En la modelación computacional ocurre el mismo fenómeno: un panel de parámetros o una visualización de escenarios que resulta evidente para el desarrollador puede ser incomprensible o propicia al error para el usuario final.
- **Empatía Operativa:** Es indispensable aplicar los principios de [[Design Thinking]] para ponerse en los zapatos del usuario del modelo, garantizando que el ingreso de variables y la interpretación de reportes estadísticos sean intuitivos, claros y libres de ambigüedades.

### 6. Taxonomía Estructural y Componentes Fundamentales del Sistema
Para formalizar matemáticamente y conceptualmente una simulación, se definen los siguientes elementos canónicos dentro de la teoría de sistemas:
- **[[Entidades]] (*Entities*):** Objetos de interés que poseen dinamismo, fluyen o son transformados a través de la red del sistema. Típicamente representan activos como clientes en una sucursal bancaria, piezas mecanizadas en una línea de producción, solicitudes de crédito, vehículos o paquetes de datos en una red.
- **[[Atributos]] (*Attributes*):** Propiedades o variables individuales locales adheridas a cada entidad específica para almacenar y transportar información histórica o de estado durante su trayectoria.
  - *Ejemplos prácticos:* El saldo disponible en la cuenta bancaria de un cliente, la hora exacta de llegada (*arrival time*) de una entidad al sistema, la prioridad de atención o la categoría del producto.
- **[[Actividades]] (*Activities*):** Tareas, procesos u operaciones que ejecutan las entidades dentro del sistema y que consumen un período de tiempo de duración conocida, probabilística o especificada.
  - *Ejemplos prácticos:* El tiempo que tarda un cajero en procesar un depósito o retiro, el mecanizado de una pieza en un torno o el pago en una terminal punto de venta.
- **[[Estado del Sistema]] (*System State*):** Colección instantánea de todas las variables de estado estrictamente necesarias para describir la situación del sistema en un punto específico del tiempo, siempre en directa correspondencia con los objetivos del estudio.
  - *Ejemplos prácticos:* El número exacto de clientes esperando en la cola, el estado operativo de los cajeros o máquinas (ocupado, desocupado, en mantenimiento) y el nivel actual de inventario en bodega.
- **[[Eventos]] (*Events*):** Ocurrencias instantáneas y puntuales en el eje del tiempo que provocan una transición o cambio formal en el estado del sistema. En la simulación orientada al tiempo discontinuo o discreto (*Discrete-Event Simulation*), el reloj avanza saltando directamente de un evento al siguiente (ej. llegada de una entidad, finalización de un servicio).
- **Clasificación de Ocurrencias por su Origen:**
  - **[[Eventos Endógenos]] (*Endogenous Events*):** Actividades, cambios u ocurrencias generadas internamente por la propia dinámica y las reglas de interacción dentro de las fronteras del sistema.
    - *Ejemplo práctico:* Un cliente termina de ser atendido por el cajero automático y pasa al área de salida; la liberación del cajero es un evento interno del modelo.
  - **[[Eventos Exógenos]] (*Exogenous Events*):** Actividades, perturbaciones u ocurrencias originadas en el entorno o ambiente externo (*Environment*), fuera de las fronteras del modelo, pero cuyos efectos impactan directamente y modifican el estado interno del sistema.
    - *Ejemplo práctico:* La tasa y patrón con que llegan nuevos clientes desde la calle hacia el banco, los cortes imprevistos en el suministro eléctrico o variaciones macroeconómicas.

### 7. El Peso Crítico del Entorno Exógeno: Caso de Estudio Real en Logística Marítima y Generación Eléctrica
El docente compartió una experiencia técnica detallada en la **Generadora San José** (la primera central termoeléctrica de generación de energía a base de carbón mineral en Centroamérica), ilustrando de manera magistral cómo un evento exógeno y ambiental no contemplado en una planificación puede desmoronar una cadena de suministro perfectamente calculada:
- **Contexto Logístico y Abastecimiento:**
  - Al carecer de yacimientos locales de carbón mineral en Guatemala, el combustible debía importarse vía marítima. Tras un exhaustivo estudio de costo-beneficio comparando proveedores globales (China, Canadá, Estados Unidos, Colombia), se adjudicó el suministro a una mina a cielo abierto en Colombia.
  - La operación anual de generación requería planificar la importación continua de aproximadamente 10 buques graneleros autodescargables clase [[Panamax]] (con capacidad individual superior a 48,000 toneladas de carbón) programados a intervalos de 5 semanas.
- **La Paradoja Geográfica de Infraestructura:**
  - Aunque la mina de carbón colombiana se encontraba físicamente más cerca de la costa del Océano Pacífico, por decisiones históricas de diseño de infraestructura exportadora de ese país, el terminal de carga portuaria fue construido en la costa del Océano Atlántico.
  - Esta configuración obligaba inexorablemente a que cada buque partiera del Atlántico colombiano, navegara hacia el sur, atravesara el Canal de Panamá y ascendiera por el Pacífico hasta atracar en Puerto Quetzal, Guatemala. En aquella época, el Canal de Panamá aún no contaba con su ampliación de esclusas y operaba tramos críticos de un solo carril, lo que convertía la coordinación de ventanas de tránsito en un cuello de botella logístico severo.
- **Diferencia Fundamental entre Planificación Aérea y Marítima:**
  - A diferencia del transporte aéreo (donde los horarios de salida y llegada se programan con precisión de horas o minutos), la logística marítima opera bajo **intervalos o ventanas de llegada** (*arrival windows*), debido a variables climáticas, corrientes marítimas y congestiones en canales de navegación.
  - Inicialmente se manejaban ventanas logísticas de ±15 días, las cuales posteriormente se lograron afinar a intervalos de ±7 días.
- **El Cisne Negro Exógeno (El Huracán en Hawái):**
  - Con toda la planificación financiera, de patios de carbón y de combustible ejecutada desde octubre del año anterior con una naviera de clase mundial con casa matriz en Londres, un evento ambiental improbable desencadenó una crisis en la madrugada.
  - La flota de buques autodescargables del proveedor realizaba entregas en distintos puertos internacionales. El buque específico asignado para viajar a Colombia a cargar el carbón guatemalteco se encontraba realizando previamente una descarga de carbón en una isla de Hawái.
  - Debido a que en una isla volcánica como Hawái no es físicamente posible dragar playas para construir muelles de aguas profundas adosados a la tierra, los buques graneleros deben anclarse en altamar y descargar utilizando muelles flotantes e infraestructura mar adentro.
  - Durante dicha maniobra, un violento huracán impactó las islas de Hawái. Por protocolos de seguridad marítima, el capitán del buque se vio obligado a suspender la descarga, levar anclas y retirarse a altamar durante 4 días para evitar el naufragio de la nave, reanudando la descarga una vez disipado el ciclón.
- **Efecto Dominó en la Cadena de Suministro:**
  - Esos 4 días de retraso provocado por un ciclón en el medio del Océano Pacífico (Hawái) generaron un efecto dominó incontrolable: aunque la mina en el Atlántico colombiano logró reajustar sus turnos para recibir al buque demorado, la estricta **ventana de paso por las esclusas del Canal de Panamá se perdió por completo**.
  - El buque quedó varado en espera de un nuevo cupo de cruce interoceánico, alterando drásticamente el cronograma de llegada del carbón a Guatemala y amenazando la continuidad de la generación eléctrica.
- **Lección Fundamental de Ingeniería de Sistemas:**
  - Al modelar y simular cualquier sistema, el analista jamás debe concentrarse exclusivamente en el interior de las paredes de la planta o de la empresa.
  - Es un mandato técnico dar siempre un paso atrás y analizar con visión holística el **entorno exógeno** (fenómenos atmosféricos, huracanes, crisis geopolíticas como conflictos bélicos que impactan el precio del petróleo y aranceles, cambios regulatorios en subsidios de combustibles o pandemias globales como el COVID-19 que alteraron el funcionamiento industrial mundial durante años).
  - Solo incorporando la robustez y resiliencia ante perturbaciones del entorno exógeno se logran construir modelos de simulación creíbles y preparados para la realidad.

---

## Fórmulas, Sintaxis o Puntos Clave
*A continuación se resumen los criterios matemáticos, de validación y de taxonomía de sistemas:*

```text
================================================================================
CRITERIOS METODOLÓGICOS Y ESTRUCTURALES EN MODELACIÓN DE SISTEMAS
================================================================================
1. VERIFICACIÓN Y MEMORIA DE CÁLCULO DE INCERTIDUMBRE:
   Sea E el error relativo estimado del modelo respecto al sistema físico real:
   Si |E| <= Margen_Tolerable (ej. ±5%), EL MODELO ES OPERATIVAMENTE ACEPTABLE.
   Si |E| >> Margen_Tolerable (ej. 70%), EL MODELO DEBE SER REEVALUADO O RECHAZADO.
   
   Regla de Auditoría: Todo modelo M requiere un vector explícito de Supuestos S:
   M = f(S, Data_Entrada) -> Análisis de Salida (Con memoria de cálculo adjunta).

2. TAXONOMÍA CANÓNICA DE COMPONENTES DE SISTEMA DE SIMULACIÓN:
   +-------------------+-------------------------------------------------------+
   | Componente        | Definición y Dominio                                  |
   +-------------------+-------------------------------------------------------+
   | Entidad (Entity)  | Objeto dinámico que transita y es procesado.          |
   | Atributo          | Variable local (clave-valor) adherida a una entidad.  |
   | Actividad         | Operación o tarea con duración temporal conocida t>0. |
   | Estado del Sistema| Vector de variables globales que describen la planta. |
   | Evento            | Punto instantáneo t_e que cambia el estado global.    |
   +-------------------+-------------------------------------------------------+

3. CLASIFICACIÓN DE EVENTOS EN SIMULACIÓN DE EVENTOS DISCRETOS (DES):
   - Evento Endógeno: e_t in Frontera_Sistema (Generado internamente por flujos).
   - Evento Exógeno:  e_t in Entorno_Externo  (Perturbación exterior que afecta).

4. PRINCIPIO DE ARQUITECTURA DE GEMELO DIGITAL (DIGITAL TWIN):
   Digital_Twin = [Digital_Master (Activo Físico Real)] <--> [Digital_Shadow (Simulador)]
   * El Digital_Shadow recibe telemetría en tiempo real para predecir fallas o reingresos.
================================================================================
```

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** La validez y utilidad de un modelo de simulación no dependen de la fe ciega ni del costo de las herramientas, sino de la capacidad técnica del modelador para documentar supuestos, calcular y acotar la incertidumbre mediante memorias de cálculo formales, y diseñar la interfaz pensando siempre en el usuario final.
- **Punto de anclaje 2:** Los sistemas organizacionales e industriales operan inmersos en un entorno ambiental y macroeconómico altamente incierto; tal como lo demostró el caso de la logística marítima de carbón afectada por un huracán en Hawái y el cierre de ventanas en el Canal de Panamá, ignorar las perturbaciones exógenas durante la construcción del modelo conduce invariablemente al fracaso operativo.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[TAREA / ENTREGA]:** Continuar con el desarrollo progresivo del proyecto de curso utilizando la plataforma de simulación [[Simio]] (o herramientas autorizadas por la cátedra), integrando análisis de datos de entrada y salida, y applying buenas prácticas de usabilidad centradas en el usuario final. *(Fecha límite mencionada: Por confirmar / A lo largo del semestre)*
- [ ] **[TAREA / ENTREGA]:** Desarrollo y entrega de los ejercicios prácticos asignados en el Laboratorio del curso bajo la coordinación del Auxiliar. *(Fecha límite mencionada: Según calendario de laboratorio)*
- [ ] **[EXAMEN / corto]:** Evaluaciones Parciales del curso y revisión de memorias de cálculo de los modelos semestrales. *(Fecha límite mencionada: Por confirmar en calendario de la facultad)*
- [ ] **[ANUNCIO GENERAL]:** Todos los modelos desarrollados en [[Simio]] serán supervisados bajo la regla de unicidad y auditoría antiplagio; dos modelos construidos por estudiantes distintos jamás son idénticos, por lo que la copia en proyectos o laboratorios implica sanción automática de 0 puntos.
- [ ] **[ANUNCIO GENERAL]:** Próxima sesión magistral programada para el martes de la siguiente semana en el mismo horario y enlace habitual de la clase.

---

## Archivo de Transcripción y Referencia Cruda

> [!NOTE]- Ver Transcripción de Google Meet (Desplegable)
> *(La sesión magistral fue impartida por el Ing. César Augusto Fernández Cáceres. Los temas centrales abarcaron la gestión técnica de la incertidumbre y el ruido con memorias de cálculo, el escepticismo metodológico en simulación, la arquitectura de los Gemelos Digitales (Digital Master y Digital Shadow), las ventajas y costos de plataformas como Simio y SPSS, los principios de usabilidad y Design Thinking en la modelación de interfaces para usuarios finales, la taxonomía canónica de los componentes de un sistema (Entidades, Atributos, Actividades, Estado del Sistema y Eventos) y la importancia del entorno y los eventos exógenos ilustrada mediante el caso real de importación de carbón mineral en buques Panamax de la Generadora San José, cuyo tránsito por el Canal de Panamá se vio alterado por un huracán en Hawái).*
