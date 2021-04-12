from pynput.keyboard import Controller, Key

print('Typing')
keyboard = Controller()
f = open('test_read.readfile', 'r')
tmp = f.read()
f.close()
keyboard.type(tmp)