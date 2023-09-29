import pyautogui
# def draw_pyramid(height):

#     for i in range(1, height + 1):
#         row = "#" * i

#         pyautogui.typewrite(row, interval=0.05)
#         pyautogui.typewrite('\n')
#         # pyautogui.typewrite(row, interval=0.05)


# pyautogui.click()

# draw_pyramid(5)

# n = int(input())
# for i in range(1, n+1):
#     s = "#" * 1
#     print(s)
#     pyautogui.typewrite(s, interval=0.05)
# pyautogui.click()

import pyautogui

# Get the number of rows for the pyramid from the user
num_rows = int(input("Enter the number of rows for the pyramid: "))

# Loop through each row and draw the pyramid using PyAutoGUI
for i in range(1, num_rows + 1):
    # Generate the string for the current row
    row_string = "#" * i
    # Print the row string
    print(row_string)
    # Use PyAutoGUI to type the row string
    pyautogui.typewrite(row_string)
    # Press Enter to move to the next line
    pyautogui.press("enter")
