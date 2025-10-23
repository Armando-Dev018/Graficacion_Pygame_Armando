import pygame
import sys

# 1. Inicializar Pygame
pygame.init()

# --- Configuración de la ventana ---
ANCHO_VENTANA = 600
ALTO_VENTANA = 600
# Calculamos el centro exacto de la ventana
CENTRO_VENTANA = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Círculos Concéntricos")

# --- Definición de colores ---
COLOR_FONDO = (10, 10, 30) # Un fondo azul muy oscuro
# 5 colores diferentes para los círculos
COLOR_1 = (255, 0, 0)     # Rojo
COLOR_2 = (255, 255, 0)   # Amarillo
COLOR_3 = (0, 255, 0)     # Verde
COLOR_4 = (0, 255, 255)   # Cian
COLOR_5 = (255, 0, 255)   # Magenta

# --- Listas de datos para el bucle ---

# Los radios pedidos (20, 40, 60, 80, 100)
lista_radios = [20, 40, 60, 80, 100]

# Los 5 colores que definimos
lista_colores = [COLOR_1, COLOR_2, COLOR_3, COLOR_4, COLOR_5]

# Grosor del contorno de los círculos
GROSOR_LINEA = 4 # 4 píxeles de grosor

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
    # Rellenamos el fondo en cada frame
    pantalla.fill(COLOR_FONDO)

    # --- DIBUJAR LOS CÍRCULOS ---
    
    # Usamos 'zip' para tomar un elemento de 'lista_radios'
    # y uno de 'lista_colores' en cada iteración.
    for radio, color in zip(lista_radios, lista_colores):
        
        # Dibujamos el círculo en la pantalla
        # Sintaxis: pygame.draw.circle(superficie, color, centro, radio, grosor)
        pygame.draw.circle(pantalla, color, CENTRO_VENTANA, radio, GROSOR_LINEA)

    # 4. Actualizar la pantalla
    pygame.display.flip()

# 5. Salir del programa
print("Saliendo del programa.")
pygame.quit()
sys.exit()