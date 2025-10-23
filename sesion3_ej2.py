import pygame
import sys
import math  # ¡Necesitamos importar math para cos y sin!

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Trayectoria Circular (Trigonométrica)")

# --- Colores ---
COLOR_FONDO = (0, 0, 0)
COLOR_OBJETO = (50, 150, 255) # Un azul
COLOR_CENTRO = (255, 0, 0)    # Rojo (para ver el pivote)

# --- Configuración del "jugador" (Rectángulo) ---
# Creamos el rectángulo (su posición inicial no importa, se recalculará)
rect_objeto = pygame.Rect(0, 0, 40, 40)

# --- Parámetros del movimiento circular ---
# El centro (pivote) de la trayectoria
CENTRO_X = ANCHO_VENTANA // 2  # 400
CENTRO_Y = ALTO_VENTANA // 2  # 300
RADIO = 150                   # El radio (distancia desde el centro)

# Variables de estado para el movimiento
angulo = 0.0                  # Ángulo actual (en radianes)
VELOCIDAD_ANGULAR = 0.03      # Qué tan rápido gira (radianes por frame)

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    # Controlar la velocidad del bucle (60 frames por segundo)
    reloj.tick(60)

    # 2. Manejo de eventos (Solo para cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de Movimiento (¡Aquí ocurre la magia!)

    # Incrementamos el ángulo en cada frame
    angulo += VELOCIDAD_ANGULAR
    
    # (Opcional) Reseteamos el ángulo después de una vuelta completa
    # para evitar que el número crezca indefinidamente.
    if angulo > 2 * math.pi: # 2*PI radianes = 360 grados
        angulo -= 2 * math.pi

    # Calcular la nueva posición (x, y) usando trigonometría
    # Esto calcula dónde debe estar el CENTRO del rectángulo
    pos_x = CENTRO_X + RADIO * math.cos(angulo)
    pos_y = CENTRO_Y + RADIO * math.sin(angulo)

    # Actualizamos el centro del rectángulo.
    # Usamos int() porque las posiciones de los rectángulos deben ser enteros.
    rect_objeto.centerx = int(pos_x)
    rect_objeto.centery = int(pos_y)

    # 4. Lógica de dibujado
    # Limpiar la pantalla
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar el punto central (opcional, para referencia)
    pygame.draw.circle(pantalla, COLOR_CENTRO, (CENTRO_X, CENTRO_Y), 5)

    # Dibujar el rectángulo en su nueva posición
    pygame.draw.rect(pantalla, COLOR_OBJETO, rect_objeto)

    # 5. Actualizar la pantalla
    pygame.display.flip()

# 6. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()