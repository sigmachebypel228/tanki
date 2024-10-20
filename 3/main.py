from tank import Tank
from tkinter import*
KEY_W= 87
KEY_A= 83
KEY_S= 65
KEY_D= 68
def check_collision():
    if player.intersects(enemy):
        print('Столкновение танков')
def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    if event.keycode == KEY_A:
        player.backward()
    if event.keycode == KEY_S:
        player.left()

    if event.keycode == KEY_D:

        player.right()
    check_collision()
w = Tk()
w.title('Таник на минималках 2.0')
canv = Canvas(w, width = 800, height = 600,bg = 'alice blue')
canv.pack()
player = Tank(canvas = canv, x = 100, y =50, ammo = 100)
enemy = Tank(canvas=canv, x=300, y=300, ammo=100)
w.bind('<KeyPress>',key_press)
w.mainloop()