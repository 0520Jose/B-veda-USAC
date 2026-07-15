---
tags:
  - USAC
  - devschedule
  - apuntes
  - redes_de_computadoras_2
  - clase_magistral
curso: "REDES DE COMPUTADORAS 2"
tipo: "Clase Magistral"
fecha: 2026-07-15
creado: 2026-07-15T18:23:29
---

# REDES DE COMPUTADORAS 2 — Introducción al Curso y Repaso del Modelo OSI

> **Fecha:** 2026-07-15 | **Duración / Tipo:** Clase Magistral | **Curso:** [[REDES DE COMPUTADORAS 2]]

---

## Resumen Ejecutivo
Sesión introductoria del curso de [[REDES DE COMPUTADORAS 2]] impartida por el Ing. Allan Alberto Morataya Gómez junto al equipo de auxiliares de cátedra. Se establecieron las normativas, las pautas de evaluación y la metodología eminentemente práctica del curso basada en "aprender haciendo" mediante laboratorios guiados paso a paso y un proyecto integrador. Asimismo, se desarrolló un repaso panorámico sobre el [[Modelo OSI]] y las responsabilidades técnicas de sus siete capas, profundizando en la segmentación de redes mediante [[VLAN]], enrutamiento inter-VLAN (Router-on-a-Stick), protocolos de la [[Capa de Transporte]] y estrategias fundamentales de [[Ciberseguridad]] tales como listas de control de acceso y hardening de dispositivos.

---

## Desarrollo Académico por Secciones

### 1. Normativas y Metodología Operativa del Curso
- **Metodología Práctica y Asincrónica Guiada:** El curso adopta un enfoque práctico intensivo orientado al principio de "aprender haciendo". Cada sesión se divide estructuralmente en una primera fase de demostración conceptual por parte del catedrático y una segunda fase donde el estudiante ejecuta configuraciones paso a paso de manera autónoma. Las guías de laboratorio están diseñadas para que cada alumno avance a su propio ritmo, evitando desincronizaciones o bloqueos en las transmisiones en vivo.
- **Herramientas y Simulación de Redes:** Las prácticas se implementan sobre herramientas de emulación e virtualización de infraestructura (como [[Cisco Packet Tracer]] o [[GNS3]]), orientándose al diseño de topologías, configuración de servicios e identificación de fallas en cada capa de red.
- **Estructura de Ponderación y Evaluaciones:**
  - **Prácticas de Laboratorio:** Casos prácticos asignados en cada sesión para aprender a resolver requerimientos corporativos de segmentación, ruteo y seguridad.
  - **Evaluaciones Breves (Quizzes):** Cuestionarios aleatorios (con preguntas y variables dinámicas para cada estudiante) que evalúan la asimilación de las prácticas ejecutadas. Estos cuestionarios representan y reemplazan la ponderación formal de participación (10%).
  - **Proyecto Integrador de Clase:** Desarrollo de un proyecto transversal en la clase magistral que complementa el laboratorio y las evaluaciones parciales, enfocándose en la integración completa de servicios de red, enrutamiento y seguridad.
- **Equipo Docente y Auxiliares:**
  - *Catedrático:* Ing. Allan Alberto Morataya Gómez.
  - *Auxiliares de Cátedra:* Gonzalo Fernando Pérez Cazún, Dominic y Ángel.

### 2. Arquitectura de Red y las Capas Inferiores del Modelo OSI
- **[[Modelo OSI]] (Open Systems Interconnection):** Modelo conceptual de referencia compuesto por siete capas (Física, Enlace de Datos, Red, Transporte, Sesión, Presentación y Aplicación) que define los estándares de comunicación intersistemas. La transmisión fluye verticalmente de arriba hacia abajo al encapsular datos en el origen y de abajo hacia arriba al desencapsular en el destino.
- **Capa 1 — [[Capa Física]]:**
  - **Medios y Suministro Eléctrico:** Gestión del cableado estructurado, fibra óptica y transmisión de impulsos eléctricos. Destaca la implementación de tecnología [[PoE]] (Power over Ethernet), la cual suministra alimentación eléctrica y conectividad de datos simultáneamente a través de un único cable de par trenzado para dispositivos como teléfonos IP y puntos de acceso inalámbricos.
  - **Diagnóstico e Indicadores Hardware:** Monitoreo visual e interpretación técnica de los indicadores LED en los puertos físicos de switches y routers para identificar actividad normal, saturación por alto tráfico o caídas físicas del enlace.
- **Capa 2 — [[Capa de Enlace de Datos]]:**
  - **Componentes y Encapsulamiento:** Operación de las tarjetas de interfaz de red ([[NIC]]), direccionamiento físico inmutable mediante direcciones [[MAC]] (Media Access Control) y encapsulamiento de datos dentro de tramas (frames).
  - **Switches y Segmentación Lógica mediante VLANs:** Uso de switches administrables para organizar la topología corporativa. La implementación de [[VLAN]] (Virtual Local Area Network) divide físicamente una red en múltiples redes lógicas independientes, estableciendo una relación directa entre cada VLAN y las áreas funcionales de la empresa para facilitar su administración y seguridad.
  - *Ejemplo Práctico de Diseño de VLANs expuesto en clase:*
    - `VLAN 10`: Administración.
    - `VLAN 20`: Laboratorios.
    - `VLAN 30`: Invitados.
  - **Mitigación de Tormentas de Broadcast:** En redes planas o no segmentadas, la acumulación de dispositivos en un único dominio de difusión genera tormentas de broadcast (broadcast storms) que degradan o colapsan drásticamente el rendimiento global. Al aislar dominios de difusión independientes, las VLANs evitan la propagación descontrolada de estas tormentas.
  - **Enlaces Troncales (Trunk Links):** Configuración de interfaces en modo troncal (`switchport mode trunk`) bajo el estándar IEEE 802.1Q para permitir el transporte etiquetado del tráfico perteneciente a múltiples VLANs a través de un único enlace entre switches.

### 3. Enrutamiento, Transporte y Capas Superiores
- **Capa 3 — [[Capa de Red]]:**
  - **Direccionamiento e Interconexión:** Asignación jerárquica de direcciones mediante [[IPv4]], cálculo de máscaras de subred, puertas de enlace predeterminadas (Gateway) y técnicas de división de subredes ([[Subnetting]], FLSM y VLSM).
  - **Enrutamiento Inter-VLAN (Router-on-a-Stick):** Arquitectura que permite la comunicación y el tránsito controlado de paquetes entre diferentes VLANs utilizando un solo puerto físico del router conectado a un puerto troncal del switch, mediante la creación de subinterfaces virtuales (por ejemplo, `FastEthernet 0/0.10` para encapsulación 802.1Q de la VLAN 10).
  - **Tipos de Enrutamiento:**
    - *Enrutamiento Estático:* Configuración manual e ingreso explícito de rutas específicas y rutas por defecto hacia redes remotas.
    - *Enrutamiento Dinámico:* Implementación de protocolos como [[OSPF]] (Open Shortest Path First), donde los routers intercambian metadatos de estado de enlace para calcular automáticamente la ruta óptima en función de la topología y el costo de los enlaces.
  - **Diagnóstico y Trazabilidad:** Empleo de comandos de la CLI como `ping` para verificar la conectividad de extremo a extremo e identificación del salto exacto de interrupción mediante `traceroute` o `tracert`.
- **Capa 4 — [[Capa de Transporte]]:**
  - **[[TCP]] (Transmission Control Protocol):** Protocolo orientado a conexión que establece sesiones seguras mediante el protocolo de saludo de tres vías (Three-Way Handshake) y garantiza la entrega confiable, ordenada y verificada de datos mediante acuses de recibo (ACK).
  - **[[UDP]] (User Datagram Protocol):** Protocolo no orientado a conexión con mínima sobrecarga de encabezado, diseñado para aplicaciones donde la baja latencia y la velocidad de transmisión son críticas (por ejemplo, transmisiones en vivo, voz sobre IP y streaming de video).
  - **Multiplexación por Puertos:** Utilización de números de puerto lógicos (origen y destino) para diferenciar y dirigir el tráfico simultáneo hacia múltiples aplicaciones y servicios en un mismo anfitrión.
- **Capas 5, 6 y 7 — [[Capa de Sesión]], [[Capa de Presentación]] y [[Capa de Aplicación]]:**
  - **Servicios de Red Corporativos:** Configuración, despliegue y mantenimiento de protocolos de aplicación esenciales para la operación de la infraestructura de TI, tales como [[DHCP]] (asignación automática de direcciones IP y parámetros de red), [[DNS]] (resolución jerárquica de nombres de dominio a direcciones IP), [[HTTP]]/[[HTTPS]] (servicios de navegación y web), [[FTP]] (servidores de transferencia de archivos) y protocolos de mensajería/correo electrónico.

### 4. Ciberseguridad, Hardening y Diagnóstico de Infraestructura
- **Hardening de Dispositivos:** Aplicación de políticas y procedimientos de robustecimiento de seguridad directamente sobre el hardware y sistema operativo de switches y routers (`IOS`). Esto incluye la protección de líneas de consola y terminales virtuales (VTY), cifrado criptográfico de contraseñas de privilegio, deshabilitación de puertos no utilizados, activación de seguridad de puertos (Port Security) y configuración de pancartas de advertencia legal (banners).
- **Traducción de Direcciones y Cortafuegos:**
  - **Firewalls Perimetrales:** Dispositivos o servicios dedicados a inspeccionar, filtrar y autorizar el tráfico entrante y saliente entre la red interna de la organización y redes externas no confiables como Internet.
  - **[[NAT]] (Network Address Translation) y [[PAT]] (Port Address Translation):** Mecanismos que permiten enmascarar todo el direccionamiento IP privado interno detrás de una o varias direcciones IP públicas, ocultando la topología interna y optimizando el consumo de direcciones IPv4 públicas.
- **Control de Acceso e Identidad:**
  - **Listas de Control de Acceso ([[ACL]]):** Conjuntos secuenciales de condiciones de permiso o denegación aplicados a las interfaces de red para filtrar el tráfico en función de parámetros específicos como IP de origen/destino, protocolo de capa superior y números de puerto TCP/UDP.
  - **Modelo [[AAA]] (Authentication, Authorization, Accounting):** Marco arquitectónico de seguridad que estandariza la administración de identidades en la infraestructura:
    - *Autenticación:* Verificación fehaciente de la identidad del usuario o administrador antes de permitir el ingreso.
    - *Autorización:* Asignación granular de permisos, comandos permitidos y niveles de privilegio específicos tras una autenticación exitosa.
    - *Contabilización (Accounting):* Registro y monitoreo exhaustivo de todas las acciones, comandos ejecutados y tiempos de conexión para efectos de auditoría y trazabilidad.
- **Monitoreo y Triada de la Seguridad:**
  - **Triada de Seguridad de la Información:** Toda configuración de red debe orientarse a preservar la Confidencialidad, Integridad y Disponibilidad de los datos y servicios de la organización.
  - **Bitácoras y Registro de Eventos (`Syslog`):** Centralización de registros de eventos en servidores de monitoreo para detectar comportamientos anómalos, auditar fallos de autenticación, realizar análisis forense ante incidentes y garantizar la observabilidad en tiempo real de la red.

---

## Fórmulas, Sintaxis o Puntos Clave

```bash
# Comandos de verificación y configuración en modo CLI de Cisco IOS

# 1. Verificación del estado de las interfaces físicas y lógicas
show interfaces
show ip interface brief

# 2. Verificación de la base de datos y asignación de VLANs en switches
show vlan brief

# 3. Configuración de un puerto de switch en modo acceso para una VLAN específica
configure terminal
interface FastEthernet 0/1
 switchport mode access
 switchport access vlan 10
 exit

# 4. Configuración de un puerto en modo troncal (Trunk) para interconexión de switches
interface FastEthernet 0/24
 switchport mode trunk
 exit

# 5. Configuración de subinterfaces en el router para enrutamiento Inter-VLAN (Router-on-a-Stick)
interface GigabitEthernet 0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 exit

# 6. Verificación de la tabla de enrutamiento del equipo de Capa 3
show ip route

# 7. Diagnóstico de conectividad de extremo a extremo y trazabilidad de saltos
ping 192.168.10.254
traceroute 8.8.8.8
```

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** El dominio técnico integral del [[Modelo OSI]] y la correcta implementación de la segmentación jerárquica mediante [[VLAN]] y enrutamiento inter-VLAN constituyen la piedra angular para evitar la saturación por tormentas de broadcast y garantizar un rendimiento estable y escalable.
- **Punto de anclaje 2:** Los conceptos conceptuales de direccionamiento, subredes y segmentación repasados en esta introducción sirven como base directa para los laboratorios en vivo sobre protocolos de enrutamiento dinámico ([[OSPF]]), diseño de cortafuegos perimetrales e implementación de políticas de control mediante [[ACL]] a desarrollarse durante el curso.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[ANUNCIO GENERAL]:** Inicio formal de los laboratorios y primera práctica guiada en la sesión magistral del día jueves. Se recomienda repasar los conceptos fundamentales de subnetting vistos en Redes 1.
- [ ] **[ANUNCIO GENERAL]:** La asistencia a las sesiones es fundamental; el 10% de la nota de participación del curso se evaluará a través de cuestionarios breves (quizzes) aleatorios sobre cada práctica de laboratorio en desarrollo.
*(No se asignaron nuevas tareas ni se anunciaron evaluaciones en esta sesión.)*

---
*Exportado automáticamente hacia **Bóveda Obsidian USAC***
