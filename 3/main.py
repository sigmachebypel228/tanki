
from tank import Tank
from tkinter import*
import world
KEY_W= 87
KEY_A= 83
KEY_S= 65
KEY_D= 68
KEY_UP =38
KEY_DOWN=40
KEY_RIGHT=39
KEY_LEFT = 37

FPS = 90
def update():
    player.update()
    enemy.update()
    w.after(1000//FPS,update)
    check_collision()
    neutral.update()
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2+player.get_size()//2,player.get_y()-world.SCREEN_HEIGHT//2+player.get_size())
def check_collision():
    player.intersects(enemy)

    enemy.intersects(player)



def key_press(event):
    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_A:
        player.backward()
    elif event.keycode == KEY_S:
        player.left()

    elif event.keycode == KEY_D:


        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(delta_x=0,delta_y=-5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(delta_x=0,delta_y= 5)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(delta_x=5,delta_y= 0)

    elif event.keycode == KEY_LEFT:
        world.move_camera(delta_x=-5, delta_y=0)
    check_collision()
w = Tk()
w.title('Таник на минималках 2.0')

canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT,bg = 'alice blue')
canv.pack()
player = Tank(canvas = canv, x = 100, y =50, ammo = 100,speed=2, bot = False)
enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=2, bot=True)
neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=False)
neutral.stop()
enemy.set_target(player)
w.bind('<KeyPress>',key_press)
update()
w.mainloop()
