# Proyecto de Graficación con Pygame - Jorge Armando Castan Reyes

Este repositorio contiene los ejercicios y mini-proyectos desarrollados para la materia de Graficación, enfocados en el aprendizaje de la biblioteca Pygame en Python.

##  Contenido del Repositorio

Esta sección detalla el propósito de cada archivo `.py` incluido en el repositorio.

### Sesión 1: Introducción a Pygame y Configuración

* `sesion1_ej1.py`: Programa básico que inicializa Pygame y muestra una ventana de 800x600 con un título y color de fondo personalizados.
* `sesion1_ej2.py`: Modificación del anterior que permite cerrar la aplicación al presionar la tecla **Esc**.
* `sesion1_ej3.py`: Imprime un contador de frames en la terminal y se detiene automáticamente al alcanzar los 300 frames.
* `sesion1_mini.py`: Mini-proyecto que cambia el color de fondo de la ventana (de blanco a azul) al presionar la tecla **C**.

### Sesión 2: Dibujando Primitivas Gráficas

* `sesion2_ej1.py`: Dibuja un tablero de ajedrez de 8x8 utilizando bucles anidados y la función `pygame.draw.rect`.
* `sesion2_ej2.py`: Muestra 5 círculos concéntricos con diferentes colores y radios crecientes.
* `sesion2_mini.py`: Mini-proyecto que dibuja una casa simple usando primitivas (rectángulos, polígonos). Permite cambiar el color de la casa al presionar las teclas **R** (rojo) y **B** (azul).

### Sesión 3: Transformaciones 2D

* `sesion3_ej1.py`: Un rectángulo se mueve con las teclas de flecha. El rectángulo cambia a color rojo cuando toca los bordes de la ventana y tiene límites para no salirse.
* `sesion3_ej2.py`: Un rectángulo sigue una trayectoria circular predefinida alrededor del centro de la ventana, usando `math.cos` y `math.sin` para el movimiento.
* `sesion3_mini.py`: Mini-proyecto donde el usuario mueve un rectángulo con el teclado, y este deja un "rastro" de pequeños círculos en su trayectoria, almacenados en una lista.
