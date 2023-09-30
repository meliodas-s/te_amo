"""
animacion de flor con cordenadas polares
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Crear un conjunto de valores theta (ángulos)
theta = np.linspace(0, 2 * np.pi, 800)

# Crear una figura de Matplotlib para el gráfico polar
fig = plt.figure(figsize=(6, 6))

# Definir la función en coordenadas polares (por ejemplo, una espiral)
r =5 - 9 * np.sin(5 * theta)

# Crear una función para la inicialización del gráfico
def init():
    line.set_data([], [])
    return line,

# Crear una función de actualización para la animación
def animate(frame):
    line.set_data(theta + frame * (2 * np.pi / 100), r)  # Gira el gráfico
    return line,

# Crear el gráfico polar inicial
line, = plt.polar([], [], 'c-')  # 'b-' para una línea azul sólida

# Configurar límites y título
plt.xlim(0, 2 * np.pi)
plt.ylim(0, np.max(r))
plt.title('')

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=100, interval=100, blit=True)

# Configurar el renderizador de video FFMpegWriter
writer = FFMpegWriter(fps=20)  # Establecer la velocidad de fotogramas

# Renderizar la animación en un archivo de video (en este caso, en formato MP4)
ani.save('grafico_polar_giratorio.mp4', writer=writer)

# Mostrar la animación
plt.show()

