''' 
encding: utf-8
made by KiRiK
design by L1za V.
'''
from objects import *

pg.init()


class Game:
    def __init__(self):
        self.cursor = Cursor()
        self.clicked = 0
        self.location = Location()
        self.buttons = [Button(1024 / 2 - 150, RES_Y - 5 - y) for y in range(384, 0, -128)]
        for i in range(len(buttons_text)):
            self.buttons[i].set_text(buttons_text[i])
            self.buttons[i].set_action(buttons_action[i])
        self.dialog = Dialog(100, 100, "Привет!\nМеня зовут фурия Делария.")
        while True:
            self.main()

    def code(self):
        self.cursor.update()
        self.location.draw()
        self.dialog.draw()
        for button in self.buttons:
            button.draw()
            if self.cursor.rect.colliderect(button.rect):
                button.collide()
                if self.clicked and self.cursor.click[0]:
                    if button.action == 'dialog1':
                        self.dialog.set_text('Слишком банально...')
                    elif button.action == 'dialog2':
                        self.buttons = tuple()
                        self.dialog.set_text('Вы погибли')
                    elif button.action == 'dialog3':
                        self.dialog.set_text('Люблю переходить\nсразу к делу ^_^')
        self.clicked = 0

    def main(self):
        win.fill((125, 125, 125))
        self.code()
        self.eventer()
        pg.display.update()
        clock.tick(FPS)

    def eventer(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(0)
            if event.type == pg.MOUSEBUTTONDOWN:
                self.clicked = 1
            if event.type == pg.MOUSEBUTTONUP:
                self.clicked = 0


if __name__ == '__main__':
    Game()
