import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.display.set_caption("Mi primer programa gráfico")

COLOR_FONDO = (45, 80, 120)

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    # 2. Manejo de eventos
    for evento in pygame.event.get():
        # Evento: El usuario hace clic en el botón 'X' de la ventana
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        # --- NUEVA SECCIÓN ---
        # Evento: El usuario presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Comprueba si la tecla presionada es 'Esc'
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
        # --- FIN DE NUEVA SECCIÓN ---

    # 3. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)

    # 4. Actualizar la pantalla
    pygame.display.flip()

# 5. Salir del programa
pygame.quit()
sys.exit()