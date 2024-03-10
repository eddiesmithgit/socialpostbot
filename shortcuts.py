import pyautogui
def gofolder(path):
    pyautogui.keyDown('command')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('G')
    pyautogui.keyUp('command')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('G')
    pyautogui.write(path)

def slt_all():
    pyautogui.keyDown('command')
    pyautogui.keyDown('a')
    pyautogui.keyUp('command')
    pyautogui.keyUp('a')

def paste():
    pyautogui.keyDown('command')
    pyautogui.keyDown('V')
    pyautogui.keyUp('command')
    pyautogui.keyUp('V')