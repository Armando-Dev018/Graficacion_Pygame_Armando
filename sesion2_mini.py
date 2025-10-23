import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mi Casa (Presiona R, G, B)")

# --- Definición de colores ---

# Colores estáticos
COLOR_FONDO_CIELO = (135, 206, 235) # Un azul cielo
COLOR_TEJADO = (139, 69, 19)      # Marrón
COLOR_VENTANA = (255, 255, 0)      # Amarillo (luz encendida)
COLOR_CESPED = (34, 139, 34)       # Verde césped

# Colores dinámicos para la casa
COLOR_ROJO = (220, 20, 60)
COLOR_AZUL = (0, 0, 205)
COLOR_VERDE = (0, 128, 0)
COLOR_BLANCO = (245, 245, 245)     # Color inicial

# --- Variable de Estado ---
# El color inicial del cuerpo de la casa será blanco
color_cuerpo_actual = COLOR_BLANCO

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        # Evento: Tecla presionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
                
            # --- LÓGICA DE CAMBIO DE COLOR ---
            # Si presionan 'R'
            if evento.key == pygame.K_r:
                print("Cambiando a ROJO")
                color_cuerpo_actual = COLOR_ROJO
            # Si presionan 'B'
            elif evento.key == pygame.K_b:
                print("Cambiando a AZUL")
                color_cuerpo_actual = COLOR_AZUL
            # Si presionan 'G'
            elif evento.key == pygame.K_g:
                print("Cambiando a VERDE")
                color_cuerpo_actual = COLOR_VERDE

    # 3. Lógica de dibujado
    
    # Dibujar el cielo (fondo)
    pantalla.fill(COLOR_FONDO_CIELO)
    
    # Dibujar el césped (un rectángulo grande en la parte inferior)
    pygame.draw.rect(pantalla, COLOR_CESPED, (0, 450, ANCHO_VENTANA, 150))

    # --- DIBUJAR LA CASA ---
    
    # 1. Cuerpo (Rectángulo)
    # Usamos la variable 'color_cuerpo_actual' para el color
    pygame.draw.rect(pantalla, color_cuerpo_actual, (300, 250, 200, 200))
    
    # 2. Tejado (Triángulo / Polígono)
    # (x1, y1), (x2, y2), (x3, y3)
    puntos_tejado = [(280, 250), (520, 250), (400, 150)]
    pygame.draw.polygon(pantalla, COLOR_TEJADO, puntos_tejado)
    
    # 3. Ventanas (Círculos)
    # (centro_x, centro_y), radio
    pygame.draw.circle(pantalla, COLOR_VENTANA, (350, 320), 30)
    pygame.draw.circle(pantalla, COLOR_VENTANA, (450, 320), 30)


    # 4. Actualizar la pantalla
    pygame.display.flip()

# 5. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()