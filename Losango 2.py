import tkinter as tk
import random

def draw_random_diamonds(canvas, count):
    """Desenha vários losangos em posições, tamanhos e cores aleatórios."""
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    for _ in range(count):
        # Coordenadas e tamanho do losango
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        size = random.randint(20, 100)

        # Coordenadas dos vértices do losango
        points = [
            x1, y1 - size // 2,  # Topo
            x1 - size // 2, y1,  # Esquerda
            x1, y1 + size // 2,  # Base
            x1 + size // 2, y1   # Direita
        ]

        # Cor aleatória
        color = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Desenhar o losango
        canvas.create_polygon(points, fill=color, outline="black")

def main():
    # Configuração da janela principal
    root = tk.Tk()
    root.title("Losangos Aleatórios")

    # Canvas onde os losangos serão desenhados
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    # Atualiza o tamanho do canvas para cálculos
    canvas.update()

    # Quantidade aleatória de losangos
    count = random.randint(5, 20)

    # Desenha os losangos
    draw_random_diamonds(canvas, count)

    # Loop principal da aplicação
    root.mainloop()

if __name__ == "__main__":
    main()
