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

# --- NUEVO: Inicializar el contador de frames ---
contador_frames = 0
LIMITE_FRAMES = 300

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
            # Comprueba si es 'Esc'
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de dibujado
    pantalla.fill(COLOR_FONDO)

    # 4. Actualizar la pantalla
    pygame.display.flip()

    # --- NUEVA SECCIÓN: Lógica del contador ---
    
    # Incrementar el contador en cada fotograma
    contador_frames += 1
    
    # Imprimir el frame actual en la terminal
    print(f"Frame: {contador_frames}")
    
    # Comprobar si hemos alcanzado el límite
    if contador_frames >= LIMITE_FRAMES:
        print(f"Límite de {LIMITE_FRAMES} frames alcanzado. Cerrando...")
        ejecutando = False # Esto detiene el bucle while
    
    # --- FIN DE NUEVA SECCIÓN ---


# 5. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()