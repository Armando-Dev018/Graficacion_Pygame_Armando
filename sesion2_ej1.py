import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 600
ALTO_VENTANA = 600
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tablero de Ajedrez 6x6")

# --- Constantes del tablero ---
FILAS = 8
COLUMNAS = 8
# Calculamos el tamaño de la casilla automáticamente
TAMANO_CASILLA = ANCHO_VENTANA // COLUMNAS 

# --- Definición de colores ---
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
# (Puedes cambiar el negro a un gris si lo prefieres, ej: (120, 120, 120))


# --- Bucle principal del "juego" ---
ejecutando = True
while ejecutando:
    
    # 2. Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # 3. Lógica de dibujado
    
    # Bucle externo para las filas (eje Y)
    for fila in range(FILAS):
        # Bucle interno para las columnas (eje X)
        for col in range(COLUMNAS):
            
            # --- Lógica para alternar color ---
            # Si (fila + col) es par, usamos blanco
            if (fila + col) % 2 == 0:
                color = COLOR_BLANCO
            # Si es impar, usamos negro
            else:
                color = COLOR_NEGRO
                
            # --- Calcular posición y tamaño de la casilla ---
            # Posición X = columna * ancho de la casilla
            x = col * TAMANO_CASILLA
            # Posición Y = fila * alto de la casilla
            y = fila * TAMANO_CASILLA
            
            # Crear el rectángulo para esta casilla
            rectangulo_casilla = pygame.Rect(x, y, TAMANO_CASILLA, TAMANO_CASILLA)
            
            # Dibujar el rectángulo en la pantalla
            pygame.draw.rect(pantalla, color, rectangulo_casilla)

    # --- FIN DE DIBUJAR EL TABLERO ---

    # 4. Actualizar la pantalla
    pygame.display.flip()

# 5. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()