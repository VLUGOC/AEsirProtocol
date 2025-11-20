# AEsir Protocol – Arquitectura por Capas (v0.1)

## 0. Nodos e Infraestructura
- Nodo principal: PC Linux (AEsir-Protocol)
- Nodo móvil: Teléfono Android con Termux
- Comunicación:
  - LAN hogar (192.168.20.x)
  - Posible Tailscale para acceso remoto

## 1. Interfaces de Entrada
- ChatGPT (operador humano → instrucciones en lenguaje natural)
- Termux (scripts: alias a, herramientas móviles)
- Futuro: voz, UI gráfica, integraciones con reuniones y herramientas de trabajo.

## 2. Capa de Transporte (Mensajería)
- Listener Linux:
  - aesir_listener.py escuchando en TCP 9001
  - Recibe órdenes desde Termux (por ahora texto plano, luego JSON)
- Listener Termux:
  - termux_listener.py escuchando en TCP 9002
  - Recibe órdenes desde Linux para tareas móviles
- Protocolo objetivo:
  - Mensajes en JSON con campos:
    - source, intent, priority, payload, timestamp

## 3. Planner / Orquestador
- Componente en Linux encargado de:
  - Leer mensajes del listener
  - Interpretar intención (intent)
  - Decidir qué agente debe actuar
- Conecta con:
  - engineer (análisis y mejora de código)
  - code_repair (reparación automática)
  - priority_agent (clasificación de urgencia)
  - Futuros agentes: architect, research, tasks, etc.

## 4. Agentes Especializados
- Engineer:
  - Objetivo: analizar archivos, detectar mejoras, conectar con reparador.
- Code Repair:
  - Objetivo: aplicar autopep8 y reglas propias para reparar código.
- Priority Agent:
  - Objetivo: clasificar tareas por criticidad (CRÍTICO / ALTO / MEDIO / BAJO).
- Futuro:
  - Architect Agent: diseño de proyectos y módulos.
  - Research Agent: investigación técnica y búsqueda de recursos.
  - Task Agent: conexión con Notion / sistemas de tareas.

## 5. Logging y Memoria Operativa
- Logs por componente:
  - logs/listener.log
  - logs/engineer.log
  - logs/priority.log
- Pipeline log:
  - Archivo logs/pipeline.log para registrar:
    - Qué se recibió
    - A qué agente se envió
    - Resultado
    - Errores y decisiones
- Este pipeline servirá para:
  - Retroalimentar a ChatGPT
  - Mejorar prompts, planes y arquitectura

## 6. Seguridad y Control
- Lista negra de comandos peligrosos (ej. rm -rf /, operaciones destructivas con sudo).
- Límite de reintentos automáticos:
  - Si una tarea falla varias veces, se marca para revisión manual.
- Validación de mensajes:
  - JSON bien formado
  - intent válido y soportado

## 7. Visión Evolutiva
- A corto plazo:
  - Estandarizar mensajes Termux → Linux en JSON.
  - Implementar un Planner funcional.
  - Conectar Engineer y Code Repair como flujo continuo.
- A mediano plazo:
  - Architect Agent para diseñar proyectos completos.
  - Integración con Notion / herramientas de gestión.
- A largo plazo:
  - Sistema agentic que:
    - Diseña, ejecuta, repara y reporta.
    - Se conecta a nubes, APIs y fuentes externas de conocimiento.
