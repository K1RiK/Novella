import pygame as pg
from sys import exit

RES_X, RES_Y, FPS = 1366, 768, 60
FONT = 'fonts/Oswald-Regular.ttf'
DEBUG = 1

buttons_text = ('Привет!',
                'Пошел на*уй',
                'Трахни меня')
buttons_action = ('dialog1',
                  'dialog2',
                  'dialog3')

pg.init()

clock = pg.time.Clock()
win = pg.display.set_mode((RES_X, RES_Y))
pg.display.set_caption("Name")


class Timer:
    def __init__(self):
        pass


class Cursor:
    def __init__(self, debug: bool = DEBUG):
        self.debug = debug
        self.update()

    def update(self):
        self.pos = self.x, self.y = pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()
        self.rect = pg.Rect(self.pos, (1, 1))
        if self.debug:
            print(self.pos)


class TextDraw:
    def __init__(self, x: int, y: int, text: str):
        self.x, self.y = x, y
        self.center = (x, y)
        self.font = pg.font.Font(FONT, 32)
        self.update(text)

    def update(self, text: str):
        self.texts = text.split('\n')
        self.renders = [self.font.render(t, True, (0, 0, 0)) for t in self.texts]

    def show(self):
        for i, render in enumerate(self.renders):
            win.blit(render, (self.center[0], self.center[1] + i * 50))


class Location:
    def __init__(self, location: str = 'menu'):
        self.location = location
        self.menu_img = pg.transform.scale(pg.image.load('img/menu.png'), (RES_X, RES_Y))

    def draw(self):
        if self.location == 'menu':
            win.blit(self.menu_img, (0, 0))


class Button:
    def __init__(self, x: int, y: int, text: str = '', img: str = 'img/answer.png'):
        self.x, self.y = x, y
        self.center = (self.x / 2, self.y / 2)
        self.img = pg.image.load(img)
        self.rect = pg.Rect(self.x, self.y, 1024, 128)  #self.img.get_rect(center=self.center)
        self.textdraw = TextDraw(self.x + 250, self.y + 36, text)

    def set_text(self, text: str):
        self.textdraw.update(text)

    def set_action(self, action: str):
        self.action = action

    def draw(self):
        win.blit(self.img, (self.x, self.y))
        self.textdraw.show()

    def collide(self):
        pg.draw.rect(win, (0, 200, 0), self.rect, 5)

    def click(self):
        pass


class Dialog:
    def __init__(self, x: int, y: int, text: str = ""):
        self.x, self.y = x, y
        self.img = pg.image.load('img/dialog.png')
        self.textdraw = TextDraw(self.x + 200, self.y + 50, text)

    def set_text(self, text: str):
        self.textdraw.update(text)

    def draw(self):
        win.blit(self.img, (self.x, self.y))
        self.textdraw.show()
