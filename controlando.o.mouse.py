import pyautogui # impotando a biblioteca pyautogui

for i in range(10):
    #movendo o mouse em um quando que se nome 
    pyautogui.moveTo(100 + 10 *i,100 + 10 * i, duration=0.25) # 'moveTo' indica a onde o mouse ira se mover
    pyautogui.moveTo(200 + 10 *i,100 + 10 * i, duration=0.25) 
    pyautogui.moveTo(200 + 10 *i,200 + 10 * i, duration=0.25) 
    pyautogui.moveTo(100 + 10 *i,200 + 10 * i, duration=0.25) 