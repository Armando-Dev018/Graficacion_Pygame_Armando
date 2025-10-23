import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Presiona 'C' para cambiar el color")

# --- Definición de colores ---
COLOR_BLANCO = (255, 255, 255)
COLOR_AZUL = (0, 0, 139) # (Usamos un azul oscuro para que no sea muy brillante)

# --- Variable de Estado ---
# Esta variable "recuerda" qué color estamos mostrando actualmente.
# Empezamos con blanco.
color_actual = COLOR_BLANCO

# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    # 2. Manejo de eventos
    for evento in pygame.event.get():
        # Evento: 'X' de la ventana
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        # Evento: Tecla presionada
        if evento.type == pygame.KEYDOWN:
            # Si es 'Esc'
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
                
            # --- NUEVA LÓGICA DE LA TAREA ---
            # Si la tecla presionada es 'C'
            if evento.key == pygame.K_c:
                print("¡Tecla C presionada! Cambiando color.")
                
                # Comprobamos el estado actual y lo alternamos (toggle)
                if color_actual == COLOR_BLANCO:
                    color_actual = COLOR_AZUL
                else: # (Significa que el color actual era AZUL)
                    color_actual = COLOR_BLANCO
            # --- FIN DE NUEVA LÓGICA ---

    # 3. Lógica de dibujado
    # Rellenamos la pantalla usando la variable 'color_actual'.
    # El color que usa dependerá de lo que haya pasado en el manejo de eventos.
    pantalla.fill(color_actual)

    # 4. Actualizar la pantalla
    pygame.display.flip()

# 5. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()