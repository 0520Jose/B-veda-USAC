---
tags:
  - USAC
  - devschedule
  - apuntes
  - redes_de_computadoras_2
  - clase_magistral
curso: "REDES DE COMPUTADORAS 2"
tipo: "Clase Magistral"
fecha: 2026-07-16
creado: 2026-07-16T19:15:00
---

# REDES DE COMPUTADORAS 2 — Protocolos de Enrutamiento, Modelo OSI, TCP/UDP y Diagnóstico por Capas

> **Fecha:** 2026-07-16 | **Duración / Tipo:** Clase Magistral | **Curso:** [[REDES DE COMPUTADORAS 2]]

---

## Resumen Ejecutivo
*La clase magistral impartida por el catedrático Allan Alberto Morataya Gómez profundiza en la importancia técnica y comercial del [[Modelo OSI]] para la estandarización, diagnóstico e independización de servicios en redes empresariales multimarcas. Se analiza el funcionamiento detallado de cada una de las siete capas, desde señales físicas hasta interfaces de aplicación, contrastando protocolos orientados a conexión como [[TCP]] frente a protocolos de streaming rápidos como [[UDP]]. Finalmente, se detallan las pautas metodológicas de laboratorio en [[Cisco Packet Tracer]], centradas en la construcción de redes LAN, verificación de tablas MAC y ARP, y resolución de problemas por aislamiento de capas.*

---

## Desarrollo Académico por Secciones

### 1. Protocolos Estándar y Enrutamiento Dinámico
- **[[Protocolos de Enrutamiento Dinámico]] (`RIP` y `OSPF`):** Explicación técnica sobre la utilización de protocolos de enrutamiento que permiten a los routers construir y actualizar de forma automática sus tablas de enrutamiento en función de los cambios en la topología de la red.
- **Detalles y Características:**
  - Garantizan la convergencia rápida de la red ante fallos en enlaces o dispositivos.
  - Sientan las bases para el diagnóstico estructurado, aislando la lógica de enrutamiento ([[Capa de Red]]) del transporte de datos.
- *Ejemplo Práctico mencionado:* Implementación en redes empresariales donde múltiples sucursales se interconectan mediante routers que deben reaccionar dinámicamente si una ruta principal deja de estar disponible.

### 2. Fundamentos y Propósito del [[Modelo OSI]]
- **Principio de "Dividir y Vencer":** El [[Modelo OSI]] funciona como un marco de referencia modular que permite descomponer un sistema de red complejo en siete capas independientes, evitando que los errores de una capa interfieran con la lógica de las demás.
- **Detalles y Características:**
  - **Ventaja Comercial y Multimarca:** Permite a los fabricantes de dispositivos basarse en estándares universales (como TCP/IP, Ethernet, etc.) para que equipos de diversas marcas interoperen sin fricciones en una misma organización.
  - **Diagnóstico Estructurado de Averías:** Facilita el aislamiento progresivo de problemas. Si un servicio en la nube o un servidor corporativo deja de responder, la resolución comienza invariablemente en las capas inferiores ([[Capa Física]] y [[Capa de Enlace de Datos]]) antes de ascender a configuraciones lógicas o de aplicación.
  - **Unidades de Datos de Protocolo (`PDU`):** Cada capa procesa la información bajo un nombre técnico específico:
    - Capa 1 (Física): Bits / Señales.
    - Capa 2 (Enlace de Datos): Tramas (`Frames`).
    - Capa 3 (Red): Paquetes (`Packets`).
    - Capa 4 (Transporte): Segmentos (`Segments`).
    - Capas 5 a 7 (Sesión, Presentación, Aplicación): Datos (`Data`).
- *Ejemplo Práctico mencionado:* Resolución de una falla donde un usuario no puede acceder a un servidor corporativo; en lugar de asumir la caída del servidor, el administrador verifica primero el cable de red, la negociación del puerto en el switch y la asignación de la dirección MAC antes de revisar la aplicación.

### 3. Análisis de las Capas Superiores (7, 6 y 5)
- **[[Capa de Aplicación]] (Capa 7):** Define la interfaz y los mecanismos para que las aplicaciones de usuario final soliciten y entreguen datos a través de la red (no es la aplicación en sí, sino el servicio de red que utiliza).
  - **Detalles y Características:** Opera con protocolos como [[HTTP]] (Puerto 80 en texto plano), [[HTTPS]] (Puerto 443 cifrado), [[FTP]], [[FTPS]], [[SMTP]], [[DNS]] y [[SSH]].
  - *Pregunta de Diagnóstico:* ¿El fallo en un portal web es intrínseco al servidor web o es consecuencia de la pérdida de conectividad en una capa inferior?
- **[[Capa de Presentación]] (Capa 6):** Responsable de la codificación, formateo, compresión y cifrado de los datos para garantizar que sean inteligibles por el sistema receptor.
  - **Detalles y Características:** Utiliza estándares criptográficos y de compresión como [[TLS]], [[SSL]], JPEG, PNG, ASCII y UTF-8.
- **[[Capa de Sesión]] (Capa 5):** Encargada de establecer, gestionar y finalizar las sesiones de comunicación y los sockets entre equipos cliente y servidor.
  - **Detalles y Características:** Un socket se compone de la combinación de una dirección IP y un número de puerto (`IP:Puerto`). Los clientes utilizan rangos de puertos efímeros dinámicos para conectarse a puertos de escucha fijos en los servidores (por ejemplo, el puerto 443 para HTTPS).
  - *Comando de Diagnóstico:* Uso del comando `netstat` para verificar en tiempo real los sockets abiertos, puertos a la escucha y conexiones establecidas en un host.

### 4. [[Capa de Transporte]] (Capa 4): [[TCP]] vs [[UDP]]
- **Protocolos de Transporte Core:** Diferenciación arquitectónica entre comunicación orientada a conexión y comunicación sin conexión en el transporte extremo a extremo.
- **Detalles y Características:**
  - **[[TCP]] (Transmission Control Protocol):** Protocolo orientado a conexión. Requiere la apertura de sesión previa confirmación, garantiza la entrega ordenada y verificada de los segmentos mediante acuses de recibo (`ACK`) y retransmite datos perdidos. Es el estándar para servicios que exigen precisión absoluta (HTTP, HTTPS, FTP, SMTP).
  - **[[UDP]] (User Datagram Protocol):** Protocolo no orientado a conexión que prioriza la velocidad y la simplicidad sobre la confiabilidad. No espera confirmaciones ni establece sesiones previas; funciona bajo un esquema de flujo continuo (`Streaming`), siendo ideal para transmisiones en vivo, voz y video donde la baja latencia es crítica.
- *Ejemplo Práctico mencionado:* La transmisión de una clase magistral en vivo por Google Meet opera principalmente sobre UDP para evitar retrasos por retransmisión, mientras que la descarga de un archivo de documento desde la plataforma utiliza TCP para asegurar que ningún bit se corrompa.

### 5. [[Capa de Red]] (Capa 3) y Enrutamiento Lógico
- **Direccionamiento Lógico y Selección de Rutas:** Gestión del direccionamiento jerárquico mediante el protocolo [[IP]] (`IPv4` e `IPv6`), determinando la ruta óptima entre redes heterogéneas.
- **Detalles y Características:**
  - Separa los dominios de difusión (`Broadcast Domains`) mediante routers y subredes lógicas.
  - Implementa protocolos de control y enrutamiento como [[ICMP]], [[OSPF]] y [[EIGRP]].
  - *Pregunta de Diagnóstico:* Si un servidor tiene su interfaz de red activa pero no es accesible desde otra subred, se debe verificar la tabla de enrutamiento y posibles bloqueos en el cortafuegos para la dirección IP.

### 6. [[Capa de Enlace de Datos]] (Capa 2) y Conmutación LAN
- **Direccionamiento Físico y Tablas de Conmutación:** Operación de los switches y tarjetas de interfaz en el ámbito local mediante direcciones físicas inmutables ([[MAC Address]]).
- **Detalles y Características:**
  - **Aprendizaje de la Tabla CAM / MAC Address Table:** El switch aprende de forma dinámica la dirección MAC de origen de cada trama recibida y la asocia al número de puerto físico de ingreso (`Puerto 1 -> MAC A`, `Puerto 2 -> MAC B`).
  - **Envío Unicast vs Broadcast:** Cuando el switch conoce el puerto exacto de la MAC de destino, envía la trama únicamente por ese puerto (`Unicast`). Si la dirección no está en la tabla (o si el switch se reinicia), realiza una inundación (`Broadcast`) por todos los puertos excepto el de entrada para localizar al dispositivo.
  - Implementa tecnologías como [[VLAN]], enlaces troncales, [[STP]] (Spanning Tree Protocol) y [[ARP]].
- *Ejemplo Práctico mencionado:* Comunicación entre dos computadoras (`PCA` y `PCB`) dentro de un mismo switch; el switch consulta su tabla interna para dirigir la trama sin generar tráfico innecesario en los puertos de otros usuarios conectados.

### 7. [[Capa Física]] (Capa 1) y Hardware
- **Transmisión de Señales en el Medio Físico:** Definición de especificaciones eléctricas, mecánicas y funcionales del cableado de cobre, fibra óptica e interfaces de radiofrecuencia (Wi-Fi 802.11 / PHY).
- **Detalles y Características:**
  - Convierte las tramas de la capa 2 en flujos de bits puros (`0` y `1`) codificados mediante voltajes o pulsos de luz.
  - *Problemas Típicos de Capa 1:* Cables de red dañados, fibra óptica quebrada por doblez excesivo, conectores defectuosos, interfaces apagadas administrativamente (`Shutdown`) o interferencia electromagnética.

### 8. Metodología de Prácticas en [[Cisco Packet Tracer]]
- **Flujo de Trabajo y Evidencias de Laboratorio:** Las prácticas experimentales se ejecutan sobre el emulador [[Cisco Packet Tracer]] para consolidar los conceptos teóricos mediante la simulación de redes locales.
- **Detalles y Características:**
  - **Actividades Clave:** Construcción de topologías LAN con switches y computadoras, asignación de direcciones IP estáticas y dinámicas, y configuración básica de routers.
  - **Verificación Técnica:** Ejecución obligatoria de pruebas de conectividad (`ping`), inspección de tablas de conmutación MAC en switches y verificación de tablas ARP en hosts.
  - **Formato de Entrega Riguroso:** Toda entrega práctica se compila en un único documento PDF estructurado que debe contener capturas de pantalla obligatorias, tablas de comprobación paso a paso, respuestas breves a preguntas técnicas y un análisis crítico de resolución.

---

## Fórmulas, Sintaxis o Puntos Clave

```bash
# Comandos esenciales para diagnóstico por capas y comprobación de servicios

# 1. Verificación de conexiones activas, sockets y puertos a la escucha en el anfitrión (Capa 5 / Capa 4)
netstat -an

# 2. Comprobación de conectividad lógica y tiempo de respuesta extremo a extremo (Capa 3 / ICMP)
ping 192.168.1.254

# 3. Consulta y verificación de la tabla de resolución de direcciones (ARP) en el host (Capa 2 / Capa 3)
arp -a

# 4. Verificación de la tabla de direcciones MAC (CAM Table) en la CLI del Switch Cisco (Capa 2)
show mac address-table

# 5. Consulta del estado e indicadores lógicos y físicos de las interfaces (Capa 1 / Capa 2)
show interfaces status
show ip interface brief
```

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** El modelo de referencia OSI constituye la herramienta conceptual más robusta para aislar y diagnosticar fallas en infraestructuras de red, permitiendo al ingeniero identificar con precisión si una incidencia radica en el nivel de hardware físico, en la conmutación de tramas o en los protocolos de aplicación.
- **Punto de anclaje 2:** La comprensión rigurosa de las diferencias operativas entre TCP y UDP, así como el funcionamiento de las tablas de enrutamiento y conmutación, sienta las bases teóricas directas para la resolución de laboratorios en Packet Tracer sobre segmentación de subredes y protocolos de ruteo dinámico.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[TAREA / ENTREGA]:** Primera Práctica de Laboratorio en [[Cisco Packet Tracer]]. Consiste en armar una topología LAN con switches, configurar direcciones IP y generar evidencias completas (capturas de pantalla, tablas de comprobación y respuestas breves de análisis), consolidando todo en un único archivo PDF. *(Fecha límite mencionada: Por confirmar en plataforma web del curso)*
- [ ] **[ANUNCIO GENERAL]:** La asistencia y participación en las prácticas es de carácter obligatorio. Las sesiones se distribuyen de manera equilibrada entre teoría conceptual magistral y ejecución práctica de laboratorios.
*(No se anunciaron evaluaciones cortas ni parciales en esta sesión magistral).*

---
*Exportado automáticamente hacia **Bóveda Obsidian USAC***
