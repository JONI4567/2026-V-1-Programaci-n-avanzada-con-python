# Sistema de Gestión de Pañol - Taller Técnico

Trabajo final para el curso **Programación Avanzada con Python** (CeNET).

## Descripción
Proyecto de consola desarrollado bajo el paradigma de **Programación Orientada a Objetos (POO)** para el registro y control de insumos y herramientas técnicas escolares.

## Estructura del proyecto
- `main.py`: punto de entrada de la aplicación y menú interactivo.
- `panol/`: paquete que contiene las entidades de dominio:
  - `insumo.py`: clase base general para insumos.
  - `electrica.py`: subclase con herencia simple y métodos de consumo eléctrico.

## Requisitos y ejecución
- Python 3.10 o superior.
- Ejecución desde la raíz del proyecto:
  ```bash
  py main.py