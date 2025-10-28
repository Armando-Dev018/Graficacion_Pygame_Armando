# Proyecto de Graficación con Pygame - Jorge Armando Castan Reyes

Este repositorio contiene los ejercicios y mini-proyectos desarrollados para la materia de Graficación, enfocados en el aprendizaje de la biblioteca Pygame en Python.

##  Descripción del Repositorio

El proyecto cubre los fundamentos de la graficación 2D utilizando Pygame, comenzando desde la configuración inicial de una ventana hasta la manipulación de objetos y transformaciones 2D.

[cite_start]Los ejercicios están organizados por sesión, cada uno en su propio archivo `.py`[cite: 56].

## 💻 Tecnologías Utilizadas

* **Python 3**
* **Pygame:** La biblioteca principal para el desarrollo de los gráficos y la interactividad.
* [cite_start]**Módulo `math`:** Utilizado en la Sesión 3 para cálculos trigonométricos[cite: 46].

## ⚙️ Instalación y Ejecución

Para ejecutar cualquiera de los programas de este repositorio, sigue estos pasos:

1.  Asegúrate de tener **Python 3** instalado en tu sistema.
2.  Clona este repositorio:
    ```bash
    git clone [https://github.com/](https://github.com/)[TuUsuario]/Graficacion_Pygame_[TuNombre].git
    cd Graficacion_Pygame_[TuNombre]
    ```
3.  Instala la dependencia de Pygame (preferiblemente en un entorno virtual):
    ```bash
    pip install pygame
    ```
4.  Ejecuta el script deseado desde tu terminal:
    ```bash
    python sesion1_ej1.py
    ```
    o
    ```bash
    python sesion3_mini.py
    ```

##  Contenido del Repositorio

[cite_start]Esta sección detalla el propósito de cada archivo `.py` incluido en el repositorio[cite: 57].

### Sesión 1: Introducción a Pygame y Configuración

* [cite_start]`sesion1_ej1.py`: Programa básico que inicializa Pygame y muestra una ventana de 800x600 con un título y color de fondo personalizados[cite: 7, 8, 9].
* [cite_start]`sesion1_ej2.py`: Modificación del anterior que permite cerrar la aplicación al presionar la tecla **Esc**[cite: 12].
* [cite_start]`sesion1_ej3.py`: Imprime un contador de frames en la terminal y se detiene automáticamente al alcanzar los 300 frames[cite: 15, 16].
* [cite_start]`sesion1_mini.py`: Mini-proyecto que cambia el color de fondo de la ventana (de blanco a azul) al presionar la tecla **C**[cite: 19].

### Sesión 2: Dibujando Primitivas Gráficas

* [cite_start]`sesion2_ej1.py`: Dibuja un tablero de ajedrez de 8x8 utilizando bucles anidados y la función `pygame.draw.rect`[cite: 24].
* [cite_start]`sesion2_ej2.py`: Muestra 5 círculos concéntricos con diferentes colores y radios crecientes[cite: 28].
* [cite_start]`sesion2_mini.py`: Mini-proyecto que dibuja una casa simple usando primitivas (rectángulos, polígonos)[cite: 31]. [cite_start]Permite cambiar el color de la casa al presionar las teclas **R** (rojo) y **B** (azul)[cite: 32].

### Sesión 3: Transformaciones 2D

* `sesion3_ej1.py`: Un rectángulo se mueve con las teclas de flecha. [cite_start]El rectángulo cambia a color rojo cuando toca los bordes de la ventana y tiene límites para no salirse[cite: 39, 41].
* [cite_start]`sesion3_ej2.py`: Un rectángulo sigue una trayectoria circular predefinida alrededor del centro de la ventana, usando `math.cos` y `math.sin` para el movimiento[cite: 46].
* [cite_start]`sesion3_mini.py`: Mini-proyecto donde el usuario mueve un rectángulo con el teclado, y este deja un "rastro" de pequeños círculos en su trayectoria, almacenados en una lista[cite: 50].
