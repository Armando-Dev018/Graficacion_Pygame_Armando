import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Movimiento con Límites y Color")

# --- Colores ---
COLOR_FONDO = (0, 0, 0)
COLOR_NORMAL = (255, 255, 255) # Blanco
COLOR_BORDE = (255, 0, 0)      # Rojo
color_actual = COLOR_NORMAL    # Variable de estado para el color

# --- Configuración del "jugador" (Rectángulo) ---
# Usamos un pygame.Rect para facilitar el manejo de posiciones y colisiones
rect_jugador = pygame.Rect(375, 275, 50, 50) # (x, y, ancho, alto)
VELOCIDAD = 5

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    # Controlar la velocidad del bucle (60 frames por segundo)
    reloj.tick(144)

    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de Movimiento (Usando get_pressed para movimiento continuo)
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        rect_jugador.x -= VELOCIDAD
    if teclas[pygame.K_RIGHT]:
        rect_jugador.x += VELOCIDAD
    if teclas[pygame.K_UP]:
        rect_jugador.y -= VELOCIDAD
    if teclas[pygame.K_DOWN]:
        rect_jugador.y += VELOCIDAD

    # --- NUEVA SECCIÓN: LÍMITES Y CAMBIO DE COLOR ---
    
    # Creamos una bandera para saber si tocamos un borde en este frame
    toco_borde = False
    
    # 1. Asegurarse de que no se salga de la ventana (Clamping)
    # 2. Si se sale, marcar la bandera 'toco_borde'
    
    # Límites horizontales (Izquierda y Derecha)
    if rect_jugador.left < 0:
        rect_jugador.left = 0  # Corrección: Ponerlo en el borde 0
        toco_borde = True
    elif rect_jugador.right > ANCHO_VENTANA:
        rect_jugador.right = ANCHO_VENTANA # Corrección: Ponerlo en el borde derecho
        toco_borde = True
        
    # Límites verticales (Arriba y Abajo)
    if rect_jugador.top < 0:
        rect_jugador.top = 0 # Corrección: Ponerlo en el borde 0
        toco_borde = True
    elif rect_jugador.bottom > ALTO_VENTANA:
        rect_jugador.bottom = ALTO_VENTANA # Corrección: Ponerlo en el borde inferior
        toco_borde = True

    # 3. Cambiar el color basado en la bandera
    if toco_borde:
        color_actual = COLOR_BORDE
    else:
        color_actual = COLOR_NORMAL

    # --- FIN DE NUEVA SECCIÓN ---

    # 4. Lógica de dibujado
    # Limpiar la pantalla
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar el rectángulo con su color actual
    pygame.draw.rect(pantalla, color_actual, rect_jugador)

    # 5. Actualizar la pantalla
    pygame.display.flip()

# 6. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()