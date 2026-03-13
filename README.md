# 💰 Personal Finance Tracker & Analyzer
**Un motor de gestión financiera end-to-end construido con Python y SQL.**

![Estatus del Proyecto](https://img.shields.io/badge/Status-Finalizado-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![SQL](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)

## 🎯 Propósito del Proyecto
Este proyecto nace de la necesidad de centralizar y analizar gastos personales sin depender de aplicaciones de terceros que comprometan la privacidad. Es una herramienta técnica que transforma entradas de datos manuales en **información estratégica** mediante visualizaciones automáticas.

## 🚀 Funcionalidades Clave
* **Persistencia de Datos:** Uso de SQLite para un almacenamiento ligero y eficiente de transacciones.
* **Operaciones CRUD:** Interfaz de consola (CLI) completa para crear, leer y eliminar registros de gastos.
* **Business Intelligence (BI):** Generación de gráficos de tarta dinámicos mediante **Pandas** y **Matplotlib**.
* **Gestión de Presupuestos:** Algoritmo de validación que compara gastos acumulados vs. límites mensuales definidos por el usuario.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python (Lógica de negocio y procesamiento de datos).
* **Base de Datos:** SQLite3 (Motor relacional).
* **Análisis de Datos:** Pandas (Estructuración de DataFrames).
* **Visualización:** Matplotlib (Generación de reportes gráficos).

## 📊 Demo Visual

Así es como se vería la interfaz del menú en la consola:

> <img width="335" height="164" alt="menu" src="https://github.com/user-attachments/assets/1536de48-85ba-4ba2-bea4-93656c64388c" />

Cuando ejecutas el reporte de gastos, el sistema procesa los datos de SQL y genera visualizaciones como esta:

> <img width="1585" height="1332" alt="grafico_gastos" src="https://github.com/user-attachments/assets/05090837-8659-4dce-b62c-aac1848a78c8" />

## 🏗️ Arquitectura Técnica
Para este proyecto apliqué conceptos profesionales de ingeniería de software:
1.  **Seguridad SQL:** Implementación de consultas parametrizadas para evitar ataques de *SQL Injection*.
2.  **Entornos Virtuales:** Aislamiento de dependencias mediante `venv`.
3.  **Modularización:** Separación de responsabilidades entre el motor de la base de datos y la interfaz de usuario.
