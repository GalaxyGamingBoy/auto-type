from pynput.keyboard import Key, KeyCode, Listener
from pynput.mouse import Controller, Button
mouse = Controller()


def function_1():
    temp_mouse_coords = mouse.position
    f = open("mouse_coords.mousecoords", "a")
    f.write(str(temp_mouse_coords[0]))
    f.write("\n")
    f.write(str(temp_mouse_coords[1]))
    f.close()

def function_2():
    print("HOW TO USE")
    print("----------")
    print("Select Mouse Location and press SHIFT+C")
    print("To Exit Press SHIFT+X")

def function_3():
    print("STOP")
    exit()





#--------------------------------------
# HOTKEYS COMMANDS
#--------------------------------------

# Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)
# Note the missing `()` after function_1 and function_2 as want to pass the function, not the return value of the function
combination_to_function = {
    frozenset([Key.shift, KeyCode(vk=67)]): function_1,  # shift + c
    frozenset([Key.shift, KeyCode(vk=86)]): function_2,  # shift + v
    frozenset([Key.shift, KeyCode(vk=88)]): function_3   # shift + x
}


# The currently pressed keys (initially empty)
pressed_vks = set()


def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk


def is_combination_pressed(combination):
    """ Check if a combination is satisfied using the keys pressed in pressed_vks """
    return all([get_vk(key) in pressed_vks for key in combination])


def on_press(key):
    """ When a key is pressed """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in combination_to_function:  # Loop through each combination
        if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
            combination_to_function[combination]()  # If so, execute the function


def on_release(key):
    """ When a key is released """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()