# Prompt Maestro de Instrucciones para Antigravity (DevSchedule / Obsidian)

> **Instrucciones para el Agente Antigravity:** Cuando el usuario te pida resumir, procesar o analizar un archivo `.md` generado por DevSchedule (o te pida procesar su última clase), **debes seguir estrictamente los siguientes pasos y el formato universitario normalizado** aquí prescrito.

---

## Pasos de Ejecución (Para Antigravity)

1. **Localizar el Archivo `.md` de la Clase:**
   - Si el usuario te da la ruta del archivo, ábrelo con tu herramienta `view_file`.
   - Si el usuario solo menciona la materia o fecha (ej. *"Procesa mi última clase de Redes 1"* o *"Revisa la bóveda de Obsidian"*), busca en la carpeta raíz de la Bóveda del usuario (`Escritorio/USAC/Bóveda USAC` o la ruta configurada en su entorno) usando `list_dir` o `grep_search` para encontrar el archivo `.md` de transcripción correspondiente.

2. **Lectura y Comprensión Profunda:**
   - Lee todo el contenido del archivo `.md` (que incluye metadatos, notas manuales si las hubiere, y la transcripción completa en bruto de Google Meet).
   - Filtra y elimina mentalmente el ruido de fondo, saludos ("hola me escuchan", "buenos días"), interrupciones técnicas ("se cortó el audio", "voy a compartir pantalla") y repeticiones involuntarias.

3. **Redacción y Actualización del Archivo en Obsidian:**
   - Redacta unos **Apuntes Universitarios de Calidad Superior** en formato Markdown (`GitHub Flavored Markdown` / compatible 100% con Obsidian).
   - **Regla Estricta: SIN EMOJIS.** No utilices ningún emoji en títulos, encabezados, subtítulos, citas ni en el cuerpo del texto del documento.
   - Usa la herramienta `replace_file_content` o `write_to_file` para **actualizar o sobrescribir el archivo `.md` en la Bóveda del usuario**, reemplazando la sección de transcripción cruda por los apuntes limpios definitivos (o creando un archivo gemelo `[Materia] - [Tema] (Apuntes Limpios).md`).

---

## Estructura y Formato Riguroso del Apunte (`.md`)

Tu redacción debe incluir **absolutamente todas las siguientes secciones** en el orden especificado (estrictamente sin emojis):

```markdown
# [Título Formal y Descriptivo de la Clase / Materia]

> **Fecha:** [YYYY-MM-DD] | **Duración / Tipo:** [Clase Magistral / Laboratorio] | **Curso:** [Nombre exacto del curso]

---

## Resumen Ejecutivo
*Máximo 3 a 5 líneas sintetizando el propósito y los conceptos centrales explicados durante la sesión.*

---

## Desarrollo Académico por Secciones

### 1. [Nombre del Primer Gran Tema / Subtítulo]
- **[Término Técnico o Concepto Clave en Negrita]:** Explicación exhaustiva, rigurosa y clara basada en lo dicho por el catedrático.
- **Detalles y Características:** Viñetas anidadas explicando pasos, metodologías o reglas y condiciones matemáticas/técnicas.
- *Ejemplo Práctico mencionado (si aplica):* [Descripción detallada del caso de uso o ejemplo visto en clase].

### 2. [Nombre del Segundo Gran Tema / Subtítulo]
- **[Término / Fórmula / Algoritmo]:** [Explicación rigurosa].
- ... *(Repetir con todas las secciones necesarias para cubrir el 100% del temario sin omitir contenido importante)*.

---

## Fórmulas, Sintaxis o Puntos Clave
*Sección para agrupar en bloques de código (`python`, `sql`, `bash`, `java`, etc.) o en formato matemático limpio cualquier código, comando o fórmula matemática relevante enseñada durante la clase.*

---

## Conclusiones y Síntesis Final
- **Punto de anclaje 1:** Resumen en 1 oración de la idea fuerza.
- **Punto de anclaje 2:** Relación con temas pasados o futuros de la materia.

---

## Fechas, Tareas, Exámenes y Anuncios Obligatorios
> [!IMPORTANT]
> **Consolidación de Recordatorios y Actividades Pendientes**

- [ ] **[TAREA / ENTREGA]:** [Descripción detallada de qué se debe entregar, requerimientos y plataforma]. *(Fecha límite mencionada: [Fecha exact o "Por confirmar"])*
- [ ] **[EXAMEN / corto]:** [Temas que entrarán y fecha tentativa].
- [ ] **[ANUNCIO GENERAL]:** [Cualquier directriz o recordatorio dado por el profesor].
*(Si no se mencionó absolutamente ninguna tarea o examen durante toda la clase, indica explícitamente: "No se asignaron nuevas tareas ni se anunciaron evaluaciones en esta sesión.")*
```

---

## Reglas de Estilo para Obsidian
- **Cero Emojis:** Está completamente prohibido el uso de emojis o iconos gráficos en cualquier parte del documento Markdown (.md).
- Usa enlaces dobles de Obsidian `[[Nombre de Concepto]]` o `[[Nombre de Materia]]` para los términos más fundamentales de la materia, conectando automáticamente el conocimiento con el resto de la Bóveda del usuario.
- Mantén un tono académico, formal, estructurado y altamente comprensible.
