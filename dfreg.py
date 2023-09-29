import pyautogui
n = 5
for i in range(1, n+1):
    s = '#'*i
    print(s)
    pyautogui.typewrite(s, interval=0.05)
    pyautogui.typewrite('\n')
#
##
###
####
#####
