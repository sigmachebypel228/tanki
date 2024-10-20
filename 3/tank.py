from tkinter import PhotoImage
from hitbox import Hitbox
class Tank:
    __count=0
    __SIZE = 100
    def __init__(self,canvas,x,y,model = 'Т-14 Армата',ammo= 100, speed= 10, file_up= '../forward.png',file_down= '../down.png',file_left= '../left.png',file_right= '../right.png'):
        Tank.__count+=1
        self.__hitbox = Hitbox(x, y, Tank.__SIZE, Tank.__SIZE)
        self.__skin_up = PhotoImage(file = file_up)
        self.__skin_down = PhotoImage(file=file_down)
        self.__skin_left = PhotoImage(file=file_left)
        self.__skin_right = PhotoImage(file=file_right)
        self.__canvas = canvas
        self.__model = model
        self.__hp = 100
        self.__xp = 0
        self.__fuel = 100
        self.__ammo = ammo
        self.__speed = speed
        self.__x = x
        self.__y = y
        if self.__x<0:
            self.__x = 0
        if self.__y<0:
            self.__y=0

        self.__create()

    def fire(self):
        if self.__ammo>0:
            self.__ammo -=1
            print('Стреляю')
    def info(self):
        print(f'Модель:{self.model},Опыт:{self.__xp},Здоровье:{self.__hp},Патроны:{self.__ammo},Топливо:{self.__fuel},Координаты:{self.__x},{self.__y}')
    def forward(self):
        if self.__fuel >0:
            self.__y+=-self.__speed
            self.__update_hitbox()
            self.__canvas.itemconfig(self.id,image =self.__skin_up)
            self.__fuel-=1
            print('Ход вверх')

            self.__repaint()
    def backward(self):
        if self.__fuel >0:
            self.__y+=self.__speed
            self.__update_hitbox()
            self.__fuel-=1
            self.__canvas.itemconfig(self.id, image=self.__skin_down)
            print('Ход вниз')
            self.__repaint()
    def left(self):
        if self.__fuel >0:
            self.__x+=-self.__speed
            self.__update_hitbox()
            self.__fuel-=1
            self.__canvas.itemconfig(self.id, image=self.__skin_left)
            print(' Ход влево')
            self.__repaint()
    def right(self):
        if self.__fuel >0:
            self.__x+=self.__speed
            self.__update_hitbox()
            self.__fuel-=1
            self.__canvas.itemconfig(self.id, image=self.__skin_right)
            print('Ход вправо')
            self.__repaint()

    def __create(self):
        self.id = self.__canvas.create_image(self.__x, self.__y, image=self.__skin_up, anchor='nw')

    def __repaint(self):
        self.__canvas.moveto(self.id, x=self.__x, y=self.__y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

    def intersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return self.__xp

    def get_fuel(self):
        return self.__fuel

    def get_speed(self):
        return self.__speed

    @staticmethod
    def get_count():
        return Tank.__count

    @staticmethod
    def get_size():
        return Tank.__SIZE

    def __str__(self):
        return(f'Координаты:{self.__x , self.__y},модель:{self.model},Здоровье:{self.__hp},Боеприпасы:{self.__ammo},опыт({self.__xp}')