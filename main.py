from uuid import uuid4

from PIL import ImageGrab

from pynput import mouse


def on_click(x, y, button, pressed):
    if pressed:
        global old_x, old_y
        old_x = x
        old_y = y
    else:
        if old_x == x:
            screen_capture()
        else:
            screen_capture((int(old_x), int(old_y), int(x), int(y)))
        return False


def listener_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


def screen_capture(bbox=None):
    image = ImageGrab.grab(bbox)

    image.save(f'./screenshots/{uuid4()}.png')


if __name__ == '__main__':
    listener_mouse()
