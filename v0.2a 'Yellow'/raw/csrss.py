import pygame
import sys
import time
import keyboard
import os

"""Welcome to the code! If you wish to build yourself, be sure to read the WHOLE readme in Github."""
"""Please respect the GPLv3 lisense and give credit where it is due ;)"""

def resource_path(relative_path):
    #get absolute path to resource, works for dev and for PyInstaller
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

image_path = resource_path('img.jpg')

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
    bg_image = pygame.image.load(image_path).convert()
    bg_image = pygame.transform.scale(bg_image, (infoObject.current_w, infoObject.current_h))

    def print_number(num):
        print(num)

    #key blockers
    keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
    keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
    keyboard.add_hotkey("win + tab", lambda: None, suppress =True)
    keyboard.add_hotkey("ctrl + esc", lambda: None, suppress =True)
    keyboard.add_hotkey("win", lambda: None, suppress =True)
    keyboard.add_hotkey('ctrl+alt+f4', lambda: None, suppress=True)
    keyboard.add_hotkey('ctrl+shift+esc', lambda: None, suppress=True)
    keyboard.add_hotkey('f11', lambda: None, suppress=True)
    keyboard.add_hotkey('win+ctrl+d', lambda: None, suppress=True)
    keyboard.add_hotkey('win+l', lambda: None, suppress=True)
    keyboard.add_hotkey('win+r', lambda: None, suppress=True)
    keyboard.add_hotkey('win+g', lambda: None, suppress=True)
    #loop to register each hotkey from 'win+1' to 'win+0'
    for i in range(1, 10):
        keyboard.add_hotkey(f'win+{i}', lambda i=i: print_number(i), suppress=True)
    keyboard.add_hotkey('win+0', lambda: print_number(0), suppress=True)
    keyboard.add_hotkey('win+shift+0', lambda: print_number(0), suppress=True)


    #keyboard.add_hotkey("ctrl + alt + delete", lambda: None, suppress =True)

    #get the center of the screen
    center_x, center_y = infoObject.current_w // 2, infoObject.current_h // 2

    #time want to stop locking the mouse in the center
    unlock_time = time.time() + 4  #4 seconds from nowd


    running = True
    while running:
        current_time = time.time()

        #lock the mouse in the center for the first 5 seconds to stop user from clicking off
        if current_time < unlock_time:
            pygame.mouse.set_pos(center_x, center_y)
            pygame.event.set_grab(True)  #grab the mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.ACTIVEEVENT and event.gain == 0:
                    running = False  #stop the program if window loses focus
                    continue
                
        else:
            pygame.event.set_grab(False)  #release the mouse after 5 seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.ACTIVEEVENT and event.gain == 0:
                    running = False

        screen.blit(bg_image, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
