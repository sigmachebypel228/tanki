import world
import texture as skin
from hitbox import Hitbox
from tkinter import NW
from random import randint
class Unit:
    def __init__(self, x, y, canvas , speed,padding,bot,default_image):
        self._x = x
        self._y = y
        self._vx = 0
        self._vy = 0
        self._dx = 0
        self._dy = 0
        self._canvas = canvas
        self._speed = speed
        self._padding = padding
        self._bot = bot
        self._default_image = default_image
        self._image = default_image
        self._create()
        self.__hitbox = Hitbox(x, y, world.BLOCK_SIZE, world.BLOCK_SIZE, padding=padding)
    def __del__(self):
        try:
            self.__canvas.delete(self.__id)
        except Exception:
            pass

    def forvard(self):
        self._vx = 0
        self._vy = -1
        self._canvas.itemconfig(self._id,
                                     image=skin.get(self._forward_image))

    def backward(self):
        self._vx = 0
        self._vy = 1
        self._canvas.itemconfig(self._id,
                                     image=skin.get(self._backward_image))

    def left(self):
        self._vx = -1
        self._vy = 0
        self._canvas.itemconfig(self._id,
                                     image=skin.get(self._left_image))

    def right(self):
        self._vx = 1
        self._vy = 0
        self._canvas.itemconfig(self._id,
                                     image=skin.get(self._right_image))

    def stop(self):
        self.__vx = 0
        self.__vy = 0


    def update(self):

        if self.__bot:
            self.__AI()
        self._dx = self._vx *self._speed
        self._dy = self._vy * self._speed
        self._x += self._dx
        self._y +=  self._dy

    def AI(self):
        pass

        # self.__id = self.__canvas.create_image(self.__x, self.__y, image = self.__default_image, anchor = NW)
        self.__hitbox = Hitbox(x,y ,world.BLOCK_SIZE,world.BLOCK_SIZE,padding = padding )
    def _create (self):
        self.__id = self._canvas.create_image(self._x, self._y, image = self._default_image, anchor = NW)