import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Rastro del Jugador (Trail)")

# --- Colores ---
COLOR_FONDO = (10, 10, 30)       # Azul oscuro
COLOR_JUGADOR = (255, 255, 255)  # Blanco
COLOR_RASTRO = (0, 150, 255)     # Azul cian

# --- Configuración del "jugador" (Rectángulo) ---
rect_jugador = pygame.Rect(375, 275, 50, 50) # (x, y, ancho, alto)
VELOCIDAD = 7

# --- NUEVO: Configuración del Rastro ---
lista_rastro = []                # La lista que almacenará las posiciones
LONGITUD_MAX_RASTRO = 100        # Cuántos círculos dejará
RADIO_CIRCULO = 8                # El tamaño de los círculos del rastro

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    # Controlar la velocidad del bucle (60 frames por segundo)
    reloj.tick(60)

    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de Movimiento (Teclado)
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        rect_jugador.x -= VELOCIDAD
    if teclas[pygame.K_RIGHT]:
        rect_jugador.x += VELOCIDAD
    if teclas[pygame.K_UP]:
        rect_jugador.y -= VELOCIDAD
    if teclas[pygame.K_DOWN]:
        rect_jugador.y += VELOCIDAD

    # (Opcional pero recomendado) Límites de la ventana
    if rect_jugador.left < 0:
        rect_jugador.left = 0
    if rect_jugador.right > ANCHO_VENTANA:
        rect_jugador.right = ANCHO_VENTANA
    if rect_jugador.top < 0:
        rect_jugador.top = 0
    if rect_jugador.bottom > ALTO_VENTANA:
        rect_jugador.bottom = ALTO_VENTANA

    # --- NUEVA SECCIÓN: Lógica del Rastro ---
    
    # 1. Añadir la posición actual del centro del jugador a la lista
    lista_rastro.append(rect_jugador.center)
    
    # 2. Mantener la lista en su tamaño máximo
    # Si la lista es más larga que el máximo...
    if len(lista_rastro) > LONGITUD_MAX_RASTRO:
        lista_rastro.pop(0) # Elimina el elemento más antiguo (el primero)

    # --- FIN DE NUEVA SECCIÓN ---


    # 4. Lógica de dibujado
    # Limpiar la pantalla
    pantalla.fill(COLOR_FONDO)
    
    # --- DIBUJAR EL RASTRO ---
    # Iteramos sobre todas las posiciones guardadas y dibujamos un círculo
    for posicion in lista_rastro:
        pygame.draw.circle(pantalla, COLOR_RASTRO, posicion, RADIO_CIRCULO)
        
    # Dibujar el rectángulo del jugador (encima del rastro)
    pygame.draw.rect(pantalla, COLOR_JUGADOR, rect_jugador)

    # 5. Actualizar la pantalla
    pygame.display.flip()

# 6. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()