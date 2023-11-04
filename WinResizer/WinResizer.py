import win32gui         #Resize window
import tkinter as tk
import keyboard


def resize():
    root = tk.Tk()

    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen', False)
    
    screen_w = root.winfo_screenwidth()     #Larghezza dello schermo
    screen_h = root.winfo_screenheight()    #Altezza dello schermo   


    window_w = int(screen_w*7/8)    #Larghezza della finestra
    window_h = int(screen_h*7/8)    #Altezza della finestra

    window_x = int((screen_w/2) - (window_w/2))     #Posizione orizzontale della finestra
    window_y = int((screen_h/2) - (window_h/2))     #Posizione verticale della finestra

    currentWindow = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(currentWindow, window_x, window_y, window_w, window_h, True)  #7/8 = 0.875

def main():
    key_combination = "ctrl+alt+m"
    keyboard.add_hotkey(key_combination, resize)
    keyboard.wait()

if __name__ == "__main__":
    main()