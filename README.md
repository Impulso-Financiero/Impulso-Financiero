# 💰 Impulso Financiero  
Versión 1.0 — Proyecto Socio-Comunitario y Educativo

Impulso Financiero es una aplicación desarrollada por estudiantes de la **Tecnicatura Superior en Desarrollo de Software (Córdoba, Argentina)**.  
Su objetivo es **ayudar a las personas a mejorar la administración de sus finanzas personales**, promover el ahorro y prevenir el endeudamiento, a través de una herramienta simple, educativa y accesible.

---

## 🚀 Objetivo General

Brindar una **herramienta digital práctica y educativa** que permita:

- Registrar ingresos y gastos.
- Planificar presupuestos mensuales.
- Recibir alertas cuando el gasto se descontrola.
- Fijar metas de ahorro y simular proyecciones.
- Aprender conceptos básicos de educación financiera.

---

## 🧩 Estructura del Proyecto

El sistema está desarrollado en **Python** con estructura modular y orientación a objetos.  
Cada módulo representa un componente clave de la vida financiera del usuario:

| Módulo | Descripción principal |
|--------|------------------------|
| `usuario.py` | Maneja el registro y perfil de cada usuario. |
| `perfil_financiero.py` | Gestiona ingresos, gastos, presupuestos y salud financiera. |
| `ingreso.py` | Registra y calcula los ingresos mensuales. |
| `gasto.py` | Administra los egresos y categorías de gasto. |
| `ahorro.py` | Crea metas de ahorro y calcula su progreso. |
| `presupuesto.py` | Define límites por categoría y controla desvíos. |
| `alerta.py` | Genera y gestiona notificaciones automáticas. |
| `categoria.py` | Clasifica los tipos de ingreso y gasto. |
| `main.py` | Punto de entrada principal del sistema (interfaz por consola). |

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Impulso-Financiero/Impulso-Financiero.git
cd Impulso-Financiero

2. Crear entorno virtual (opcional pero recomendado)
bash
Copiar código
python -m venv venv
source venv/bin/activate     # En Linux/Mac
venv\Scripts\activate        # En Windows

3. Instalar dependencias
bash
Copiar código
pip install -r requirements.txt

4. Ejecutar la aplicación
bash
Copiar código
python main.py

🧠 Cómo usar Impulso Financiero

1. Crear tu usuario
Al iniciar, el sistema te pedirá:
Nombre
Email
Contraseña
Tu perfil financiero se creará automáticamente con saldo inicial en 0.

2. Registrar ingresos
Desde el menú principal, elegí Registrar ingreso.
Podés ingresar datos como:
- Monto
- Fecha
- Categoría (Ej.: sueldo, comisiones, extra)
- Descripción
El sistema calculará automáticamente tu total mensual de ingresos.

3. Registrar gastos
Seleccioná Registrar gasto e ingresá:
- Monto
- Fecha
- Categoría (Ej.: alimentación, servicios, transporte, ocio, deudas)
- Descripción
Si tus gastos superan el 80 % de tus ingresos, se generará una alerta crítica automática.

4. Crear presupuesto mensual
Desde Gestión de presupuesto, podés definir límites por categoría.
Ejemplo:
Alimentación: $150.000
Servicios: $80.000
Transporte: $40.000
Ahorro: $50.000
Otros: $180.000
Cada vez que registres un gasto, el sistema descontará su monto del presupuesto y te mostrará cuánto te queda disponible.

5. Definir metas de ahorro
Entrá en el módulo de Ahorro y fijá objetivos, como:
Meta: $100.000
Plazo: 6 meses
Aporte mensual: $20.000
El sistema simulará tu progreso mediante sucesiones aritméticas y te mostrará cuánto habrás ahorrado al final del período.

6. Recibir alertas automáticas
El sistema emite alertas según reglas lógicas:
🔴 “Tus gastos superan el 80 % de tus ingresos.”
🟠 “Tu saldo se está reduciendo rápidamente.”
🟢 “Podés activar tu fondo de ahorro.”
Cada alerta tiene justificación basada en lógica proposicional (ejemplo: (gastos > ingresos) → alerta_de_ajuste).

7. Consultar reportes
Usá Ver resumen mensual para obtener:
Balance total (ingresos - gastos)
Porcentaje de gasto por categoría
Nivel de salud financiera (óptimo / en riesgo / crítico)
Evolución de ahorro mensual (gráfico)

📊 Modelo Matemático
El sistema aplica principios de Matemática y Lógica para procesar datos:

Concepto y Aplicación práctica
Teoría de conjuntos	- Agrupar ingresos, egresos y categorías.
Lógica proposicional - Generar alertas y sugerencias automáticas.
Sucesiones aritméticas - Proyectar ahorros o deudas en el tiempo.
Funciones lineales - Modelar la evolución de ingresos y gastos.
Derivadas - Detectar velocidad de cambio del saldo (alertas proactivas).
Matrices y vectores - Estructurar transacciones por períodos.

👥 Ejemplos de perfiles de usuario
Javier (empleado joven)	Controlar gastos y evitar deuda - Alertas y presupuestos automáticos
Ana (estudiante con ingresos variables)	Manejar ingresos irregulares - Presupuestos flexibles + metas simples
Carlos (endeudado crónico)	Salir del ciclo de préstamos - Estrategia guiada de pago de deudas

🧪 Pruebas y validaciones
El sistema incluye una carpeta tests/ con pruebas unitarias para verificar:

Registro de ingresos y gastos
Cálculo de balances
Alertas automáticas
Progreso de metas de ahorro

Podés correrlas con:
bash
pytest

🛠️ Tecnologías usadas
Python 3.12+
VS Code
Git / GitHub
PyTest

🌱 Enfoque Socio-Comunitario
Impulso Financiero busca reducir la vulnerabilidad económica en jóvenes y familias mediante educación financiera práctica.
No pretende reemplazar una formación formal, sino servir como puente entre la teoría y la acción diaria, empoderando a los usuarios para tomar decisiones informadas.

🤝 Autores
Grupo 20 – Tecnicatura Superior en Desarrollo de Software
Ariel Nicolás Romano – Programación y Desarrollo
Luis Nicolás Asensio Lubrano – Lógica y Matemática

📂 Repositorio oficial: https://github.com/Impulso-Financiero/Impulso-Financiero
