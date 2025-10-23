import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---

# ■ Cambiar el tamaño de la ventana a 1000x800 píxeles.
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
# Crear la superficie de la pantalla (la ventana)
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# ■ Establecer un título personalizado
pygame.display.set_caption("Mi primer programa gráfico")

# ■ Cambiar el color de fondo a un color RGB personalizado.
#    (R, G, B) - Valores entre 0 y 255
#    Ejemplo: Un azul oscuro (R=45, G=80, B=120)
COLOR_FONDO = (45, 80, 120)


# --- Bucle principal del "juego" ---
# Se ejecutará indefinidamente hasta que el usuario cierre la ventana
ejecutando = True
while ejecutando:
    
    # 2. Manejo de eventos
    # Revisa todos los eventos que han ocurrido
    for evento in pygame.event.get():
        # Si el usuario hace clic en el botón 'X' de la ventana
        if evento.type == pygame.QUIT:
            ejecutando = False # Salimos del bucle

    # 3. Lógica de dibujado
    # Rellena la pantalla con el color de fondo definido
    # Esto borra todo lo que había en el fotograma anterior
    pantalla.fill(COLOR_FONDO)

    # 4. Actualizar la pantalla
    # Pygame usa doble búfer: dibujas en una pantalla oculta
    # y 'flip()' la muestra al usuario.
    pygame.display.flip()

# 5. Salir del programa
# Cuando el bucle 'while' termina, salimos de Pygame y cerramos el script
pygame.quit()
sys.exit()