import pyautogui


def draw_pyramid(height):
    screen_width, screen_height = pyautogui.size()
    pyramid_width = height * 2 - 1
    starting_x = (screen_width - pyramid_width * 10) // 2

    for i in range(1, height + 1):
        row = "#" * i
        pyautogui.moveTo(starting_x, screen_height - i * 20)
        pyautogui.typewrite(row, interval=0.05)


draw_pyramid(int(input()))
