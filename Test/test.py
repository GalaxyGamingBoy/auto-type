from pynput.mouse import Button, Controller
import os

mouse = Controller()

tmp = [0, 0]
f = open('mouse_coords.mousecoords')
tmp[0] = int(f.readline())
tmp[1] = int(f.readline())
f.close()

print(tmp)
mouse.position = tmp
mouse.press(Button.left)
mouse.release(Button.left)
os.system(("type.py"))