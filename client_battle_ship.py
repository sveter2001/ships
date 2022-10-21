from pygame import *
from tkinter import Tk, Label, StringVar, Button, Entry

init()

shots = [[0 for r in range(10)] for d in range(10)]
size = (800, 600)
screen = display.set_mode(size)

ARIAL_30 = font.SysFont('arial', 50)


class Menu:
    def __init__(self):
        self._options = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._options.append(ARIAL_30.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._options) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._options):
            option_rect: Rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)


running = True


def quit_game():
    global running
    running = False


def formation():
    window = Tk()
    window.title("formation")
    window.geometry("550x400")
    window.configure(bg='bisque2')
    window.resizable(False, False)

    text_var = []
    entries = []

    def get_mat():
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                matrix[i].append(text_var[i][j].get())
                if matrix[i][j] == '':
                    matrix[i][j] = 0

        print(matrix)

    Label(window, text="Make a formation", font=('arial', 10, 'bold'),
          bg="bisque2").place(x=150, y=20)
    Label(window, text="◄⁞Θ⁞Θ⁞Θ⁞Θ⁞Ɒ - 1 ship", font=('arial', 10, 'bold'),
          bg="bisque2").place(x=370, y=150)
    Label(window, text="◄⁞Θ⁞Θ⁞Θ⁞Ɒ    - 2 ships", font=('arial', 10, 'bold'),
          bg="bisque2").place(x=370, y=200)
    Label(window, text="◄⁞Θ⁞Θ⁞Ɒ        - 3 ships", font=('arial', 10, 'bold'),
          bg="bisque2").place(x=370, y=250)
    Label(window, text="◄⁞Θ⁞Ɒ           - 4 ships", font=('arial', 10, 'bold'),
          bg="bisque2").place(x=370, y=300)


    x2 = 0
    y2 = 0
    rows, cols = (10, 10)
    for i in range(rows):

        text_var.append([])
        entries.append([])
        Label(window, text=i, font=('arial', 10, 'bold'), bg="bisque2").place(x=60+i*30+2, y=45)
        Label(window, text=i, font=('arial', 10, 'bold'), bg="bisque2").place(x=42, y=60 + i * 30 + 8)
        for j in range(cols):
            text_var[i].append(StringVar())
            entries[i].append(Entry(window, textvariable=text_var[i][j], width=3))
            entries[i][j].place(x=60 + x2, y=70 + y2)
            x2 += 30

        y2 += 30
        x2 = 0
    button = Button(window, text="Submit", bg='bisque3', width=15, command=get_mat)
    button.place(x=150, y=370)
    window.mainloop()


menu = Menu()
menu.append_option('Hello world!', lambda: print('Hello world!'))
menu.append_option('Your formation', formation)
menu.append_option('Quit', quit_game)

while running:
    for e in event.get():
        if e.type == QUIT:
            quit_game()
        if e.type == KEYDOWN:
            if e.key == K_w:
                menu.switch(-1)
            elif e.key == K_s:
                menu.switch(1)
            elif e.key == K_SPACE:
                menu.select()

    screen.fill((0, 0, 0))

    menu.draw(screen, 100, 100, 75)

    display.flip()