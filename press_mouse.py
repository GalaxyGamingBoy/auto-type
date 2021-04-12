from pynput.mouse import Controller, Button
import time

mouse = Controller()
tmp = [0, 0]
f = open('mouse_coords.mousecoords')
tmp[0] = int(f.readline())
tmp[1] = int(f.readline())
f.close()

mouse.position = (tmp)

time.sleep(0.25)

mouse.press(Button.left)
mouse.release(Button.left)
